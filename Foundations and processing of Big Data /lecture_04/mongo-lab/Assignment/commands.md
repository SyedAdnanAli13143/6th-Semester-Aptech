# Lab 4 — Assignment (Extended): Spark + MongoDB Together

The basic Lab 4 (in the parent folder) used MongoDB on its own. This assignment shows the **real-world pattern**: live data lives in MongoDB, but the heavy analytics run in Spark.

By the end of this assignment you'll have done both halves of the most common Big Data pipeline:

```
                   read
   MongoDB  ─────────────▶  Spark  (do analytics)
       ▲                       │
       │         write         │
       └───────────────────────┘
```

Two scripts, both already provided:
- `spark_from_mongo.py` — Spark reads documents from Mongo, computes results, prints them.
- `spark_to_mongo.py` — Spark reads Mongo, computes averages, writes them **back** as a new collection.

---

## 1. Why this matters

Real systems split work across two layers:

| Layer | Job | Example |
|---|---|---|
| **MongoDB** (online) | Fast reads/writes from the live app | "Show Ali's profile when he logs in" |
| **Spark** (offline) | Big-batch analytics over all the data | "Compute the leaderboard every night" |

The bridge is the **MongoDB Spark connector** — a JAR that lets Spark treat a Mongo collection as a DataFrame.

So far in Labs 2 and 3 we did analytics over a CSV. In real life, data sits in a database. This assignment closes that gap.

---

## 2. Prereqs

You should have already done the basic Lab 4. If you haven't, just go through sections 1–7 of the parent `commands.md` first to understand `mongosh`, documents, and aggregation.

You also need Docker running (Lab 1 setup).

---

## 3. The setup — networked containers

The basic lab ran one container (`mongo-lab`). For this assignment we need **two** containers (Mongo + Spark) that can find each other by name. Docker calls this a **user-defined network**.

If you still have the basic-lab `mongo-lab` running, stop it first:
```bash
docker stop mongo-lab 2>/dev/null
docker rm   mongo-lab 2>/dev/null
```

Create a network and start Mongo on it:
```bash
docker network create lab-net
docker run -d --name mongo-lab --network lab-net -p 27017:27017 mongo:7
```

Why a network? When Spark runs in another container, it needs to reach Mongo. With both on `lab-net`, Spark can connect to `mongodb://mongo-lab:27017` — Docker resolves the container name automatically.

Wait ~5 seconds for Mongo to be ready, then load the demo data (the same `seed.js` from the basic lab):
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_04/mongo-lab"
docker exec -i mongo-lab mongosh < seed.js
```

You should see `students inserted: 15` and `profiles inserted: 1`.

---

## 4. Part A — Spark reads from MongoDB

Move into the assignment folder:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_04/mongo-lab/assignment"
```

Look at `spark_from_mongo.py`. The key lines:

```python
SparkSession.builder
  .config("spark.mongodb.read.connection.uri", "mongodb://mongo-lab:27017/school.students")
  ...

df = spark.read.format("mongodb").load()
```

Two new things vs Lab 3:
- The connection URI tells Spark where Mongo lives (`mongo-lab` is the container name on `lab-net`).
- `format("mongodb")` instead of `format("csv")` — that's the connector at work.

Everything *after* `df` is identical to Lab 3 — once the data is a DataFrame, Spark doesn't care where it came from.

Run the job:
```bash
docker run --rm --network lab-net \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_04/mongo-lab/assignment:/app" \
  apache/spark:3.5.3 /opt/spark/bin/spark-submit \
  --conf spark.jars.ivy=/tmp/.ivy \
  --packages org.mongodb.spark:mongo-spark-connector_2.12:10.4.0 \
  /app/spark_from_mongo.py
```

What's new in the command:
- `--network lab-net` — put the Spark container on the same network as Mongo.
- `--packages org.mongodb.spark:mongo-spark-connector_2.12:10.4.0` — download and add the connector JAR. Maven coordinate; first run pulls it from the internet (~10 MB), later runs are cached.
- `--conf spark.jars.ivy=/tmp/.ivy` — fix for a known Ivy-cache permission error inside the Spark container.

Expected (last block):
```
=== Average score per student (Spark on Mongo data) ===
+----------+---------+
|student_id|avg_score|
+----------+---------+
|      S001|    75.33|
|      S002|    57.67|
|      S003|     57.0|
|      S004|    87.33|
|      S005|    42.67|
+----------+---------+

=== Pass count per course ===
+-------+---------------+
| course|students_passed|
+-------+---------------+
|English|              4|
|   Math|              3|
|Science|              4|
+-------+---------------+
```

Same answers as Labs 2 and 3. Different source — same pipeline.

---

## 5. Part B — Spark writes back to MongoDB

Now the other direction. `spark_to_mongo.py`:

```python
.config("spark.mongodb.write.connection.uri", "mongodb://mongo-lab:27017/school.student_averages")
...
result.write.format("mongodb").mode("overwrite").save()
```

This time we **write** the computed averages back into a **new collection** called `student_averages`. That's exactly how a nightly batch job would update a dashboard or a leaderboard table.

Run it:
```bash
docker run --rm --network lab-net \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_04/mongo-lab/assignment:/app" \
  apache/spark:3.5.3 /opt/spark/bin/spark-submit \
  --conf spark.jars.ivy=/tmp/.ivy \
  --packages org.mongodb.spark:mongo-spark-connector_2.12:10.4.0 \
  /app/spark_to_mongo.py
```

You should see the averages printed, ending with:
```
>>> Wrote results to MongoDB collection 'school.student_averages'
```

Verify it actually landed in Mongo:
```bash
docker exec -it mongo-lab mongosh
```
```js
use school
show collections        // you should see: profiles, students, student_averages
db.student_averages.find()
```

You'll see 5 fresh documents:
```
{ _id: ..., student_id: 'S001', avg_score: 75.33 }
{ _id: ..., student_id: 'S002', avg_score: 57.67 }
{ _id: ..., student_id: 'S003', avg_score: 57   }
{ _id: ..., student_id: 'S004', avg_score: 87.33 }
{ _id: ..., student_id: 'S005', avg_score: 42.67 }
```

That's the full pipeline. Spark read from one Mongo collection, aggregated, and wrote back to a new one — all without any intermediate CSV files.

---

## 6. The mental model

```
1. Live app  ──writes──▶  school.students        (raw data, fast)
                              │
                              │  read by Spark
                              ▼
                          DataFrame in memory
                              │
                              │  groupBy + agg
                              ▼
                          DataFrame of results
                              │
                              │  write by Spark
                              ▼
                       school.student_averages    (analytics output, also fast to read by app)
```

The app never has to compute the average itself. It just reads `student_averages` whenever it needs to show a leaderboard. Spark refreshes that collection on a schedule (e.g., every night).

---

## 7. Clean up

Stop and remove everything:
```bash
docker stop mongo-lab
docker rm   mongo-lab
docker network rm lab-net
```

(All Mongo data was inside the container; it's gone now.)

---

## 8. Common errors

- **`MongoSocketOpenException` / "Connection refused"** when Spark tries to read.
  Spark and Mongo are not on the same Docker network, or the container name is wrong. Both must be on `lab-net`, and the URI must say `mongo-lab` (the container name), not `localhost`. From inside a container, `localhost` means *that container*, not the host.

- **`FileNotFoundException: ... .ivy2/cache/...`** when running `--packages`.
  Add `--conf spark.jars.ivy=/tmp/.ivy` to the `spark-submit` command. The Spark image's home directory isn't writable for the Ivy resolver.

- **`unresolved dependency: org.mongodb.spark#mongo-spark-connector_2.12;...`**
  Internet hiccup during the first download. Try again. After one successful run the JAR is cached inside the container — but since we use `--rm`, every run re-downloads. To cache it permanently, add `-v ~/.ivy:/tmp/.ivy` so the cache survives between runs.

- **First run takes 1–2 minutes.**
  That's `--packages` downloading the connector and its dependencies. Subsequent runs in the same shell session don't re-download because of the volume cache (if you added one). With `--rm` only, every run is fresh.

- **`docker network create lab-net` says "already exists".**
  Fine — it was created in a previous run. Either reuse it or delete with `docker network rm lab-net`.

---

## 9. Common student questions

### Q1. Why do we need a Docker network just for this?

Because the Spark container talks to the Mongo container over TCP using the name `mongo-lab`. Docker only resolves container names **within a user-defined network**. Without `lab-net`, Spark would have no way to find Mongo.

In production, the same effect is achieved by Kubernetes services, ECS service discovery, or just plain DNS — but the idea is identical: containers find each other by name.

### Q2. Could we use `localhost:27017` instead?

From your Windows host, yes — `mongosh` on the host connects to `localhost:27017` because we exposed the port with `-p 27017:27017`. But from **inside a container**, `localhost` means *that container*, which has no Mongo. That's why Spark must use the network name `mongo-lab`.

### Q3. Is this how real companies move data between Mongo and Spark?

Yes — exactly this pattern. The real production stack adds:
- A scheduler (Airflow / cron) to run the Spark job every X hours.
- A cluster (not a one-shot container) so Spark has many workers.
- Authentication on Mongo (`mongodb://user:pass@host:27017`).
- Often, an intermediate stop in S3 / HDFS for cheap cold storage.

But the logic — "Spark reads Mongo, computes, writes back" — is the same.

### Q4. Why write back to Mongo instead of just printing?

Because the **app** needs to show the result to users. If the leaderboard lives in `student_averages`, the app just does `db.student_averages.find()` and gets it instantly. If Spark only printed to a terminal, the app couldn't see anything.

In practice, results often get written to **multiple** places — back to Mongo for the app, and to a data warehouse (Snowflake / BigQuery) for analysts. Spark can write to all of them in the same job.

### Q5. What's `--packages org.mongodb.spark:mongo-spark-connector_2.12:10.4.0` doing?

It's a Maven coordinate. Spark uses Maven-style dependency resolution to fetch JARs at runtime:
- `org.mongodb.spark` — group (the publisher).
- `mongo-spark-connector_2.12` — name (`_2.12` means built for Scala 2.12, which our Spark image uses).
- `10.4.0` — version.

Spark downloads it (and its dependencies) on first run, caches it, and adds it to the classpath. This is how Spark stays small — connectors are pulled in on demand.

---

## 10. The takeaway

Three sentences to remember:
1. **The Mongo Spark connector turns a Mongo collection into a Spark DataFrame** — and a DataFrame back into Mongo documents.
2. **Two containers, one Docker network** — that's the whole infrastructure trick. Containers find each other by name on `lab-net`.
3. **Read → process → write back is the most common production pipeline.** Live database serves the app; Spark does the heavy thinking and updates the database on a schedule.
