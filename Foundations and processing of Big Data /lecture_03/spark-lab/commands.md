# Lab 3 — PySpark (Beginner Friendly)

In Lab 2 you wrote a `mapper.py` and a `reducer.py` and ran them through Hadoop Streaming. It worked — but you had to do the **choreography** yourself: emit the key, then sort, then handle the group boundary. Even for "average per student" it was ~30 lines of Python.

Spark fixes that. You just say **"I want the average score per student"** and Spark figures out the rest.

---

## 1. The idea (read this first)

In MapReduce you tell the cluster *how* to do the job, step by step:
> "First label each row. Then sort. Then walk through the sorted list and watch for the key to change..."

In Spark you tell the cluster *what* you want:
> "Group these rows by student_id and give me the average of `score`."

Same job. Spark writes the map and the reduce for you behind the scenes.

```
MapReduce  (Lab 2):  mapper.py + reducer.py + sort logic + group boundary  →  ~30 lines
Spark      (Lab 3):  df.groupBy("student_id").avg("score")                  →  ~1 line
```

It's also **much faster** at scale, because Spark keeps data in memory between steps instead of writing to disk like MapReduce does. For now, just remember: same idea (split + combine), simpler code.

---

## 2. The DataFrame — Spark's main idea

A **DataFrame** is just a table. Rows and columns. If you've ever seen Excel, Pandas, or a SQL table, you already know what it looks like.

```
+----------+--------+--------+-------+
| student_id | name | course | score |
+----------+--------+--------+-------+
| S001     | Ali    | Math   | 82    |
| S001     | Ali    | Science| 76    |
| ...
```

In Spark, the table is **distributed** — its rows can live on many machines at once. But you talk to it as if it's one table:

```python
df.groupBy("student_id").avg("score")
```

Spark turns that into a parallel job under the hood. You don't write the parallel part — Spark does.

---

## 3. Our data (same as Lab 2)

`sample_data/students.csv`:
```
student_id,name,course,score,passed
S001,Ali,Math,82,1
S001,Ali,Science,76,1
S001,Ali,English,68,1
...
```

We'll compute the **same thing** as Lab 2 — average score per student — to show you the answer is identical, just the code is simpler.

---

## 4. The script — `avg_score.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, round

spark = SparkSession.builder.appName("AvgScore").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

df = spark.read.csv("/data/students.csv", header=True, inferSchema=True)

print("=== Raw data ===")
df.show()

result = (
    df.groupBy("student_id")
      .agg(round(avg("score"), 2).alias("avg_score"))
      .orderBy("student_id")
)

print("=== Average score per student ===")
result.show()

spark.stop()
```

Line by line:
- `SparkSession` — your entry point to Spark. Always start with this.
- `setLogLevel("WARN")` — quiets Spark's chatty INFO logs so you can see your output.
- `spark.read.csv(...)` — load the CSV into a DataFrame. `header=True` uses the first row as column names. `inferSchema=True` auto-detects that `score` is an integer.
- `df.show()` — print the table. Like `df.head()` in pandas.
- `groupBy("student_id").agg(...)` — group rows by student, aggregate.
- `round(avg("score"), 2)` — average, rounded to 2 decimals.
- `.alias("avg_score")` — rename the resulting column.
- `spark.stop()` — release resources.

The whole job is **~10 lines** of declarative code. Compare to Lab 2's mapper + reducer (~30 lines of stdin/stdout plumbing).

---

## 5. Get the Spark image (one-time)

Open **PowerShell** or **Git Bash** on Windows.

```bash
docker pull apache/spark:3.5.3
```

This downloads ~700 MB on first run; later runs are instant.

If you're on **Git Bash**, run this once per shell so paths don't get mangled:
```bash
export MSYS_NO_PATHCONV=1
```
(PowerShell users skip this — it's a Git Bash quirk only.)

---

## 6. Run the job

Move into the lab folder:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_03/spark-lab"
```

Run Spark in a one-shot container — no cluster to start, nothing to clean up:

```bash
docker run --rm \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_03/spark-lab/sample_data:/data" \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_03/spark-lab:/app" \
  apache/spark:3.5.3 /opt/spark/bin/spark-submit /app/avg_score.py
```

> PowerShell users: replace the trailing `\` line breaks with backticks `` ` ``, or just put the whole command on one line.

What the command does:
- `docker run --rm` — start a fresh Spark container, delete it when done.
- `-v ".../sample_data:/data"` — make the CSV visible inside the container at `/data/students.csv`.
- `-v ".../spark-lab:/app"` — make your scripts visible inside the container at `/app/`.
- `spark-submit /app/avg_score.py` — Spark's command to run a Python job.

Expected output (last block of the log):
```
=== Raw data ===
+----------+------+-------+-----+------+
|student_id|  name| course|score|passed|
+----------+------+-------+-----+------+
|      S001|   Ali|   Math|   82|     1|
...

=== Average score per student ===
+----------+---------+
|student_id|avg_score|
+----------+---------+
|      S001|    75.33|
|      S002|    57.67|
|      S003|     57.0|
|      S004|    87.33|
|      S005|    42.67|
+----------+---------+
```

**Same answers as Lab 2** — S001 = 75.33, S002 = 57.67, etc. That's the proof: Spark and MapReduce do the same thing, but Spark code is shorter.

You'll also see a lot of `INFO` log lines around your output. That's Spark being verbose. Look for the two `===` blocks — that's your result.

---

## 7. Second example — pass count per course

Same idea, different aggregation. `pass_count.py`:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

spark = SparkSession.builder.appName("PassCount").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

df = spark.read.csv("/data/students.csv", header=True, inferSchema=True)

result = (
    df.groupBy("course")
      .agg(_sum("passed").alias("students_passed"))
      .orderBy("course")
)

print("=== Students who passed, per course ===")
result.show()

spark.stop()
```

Run it (same command, different file at the end):
```bash
docker run --rm \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_03/spark-lab/sample_data:/data" \
  -v "c:/Users/Adnan/Desktop/ML/project/curriculum/lecture_03/spark-lab:/app" \
  apache/spark:3.5.3 /opt/spark/bin/spark-submit /app/pass_count.py
```

Expected:
```
+-------+---------------+
| course|students_passed|
+-------+---------------+
|English|              4|
|   Math|              3|
|Science|              4|
+-------+---------------+
```

Same answer Lab 2 gave with `mapper2.py` + `reducer2.py` — but in Spark it's literally one `groupBy(...).agg(sum(...))`.

---

## 8. The mental shift from Lab 2

| Lab 2 (MapReduce) | Lab 3 (Spark) |
|---|---|
| You write **how** to compute (label, sort, walk groups). | You write **what** you want (group by, average). |
| Two scripts: mapper, reducer. | One script. |
| Outputs go through HDFS between map and reduce. | Data stays in memory between steps. |
| Slow to start (seconds of YARN setup). | Fast to start. |
| Best for very large batch jobs. | Best for almost everything today (batch, ML, streaming). |

In modern jobs, **almost nobody writes raw MapReduce anymore.** Everyone uses Spark. You learned MapReduce in Lab 2 to understand the *idea*. Spark is what you'll actually use.

---

## 9. Common errors

- **"No such file or directory: /data/students.csv"**
  Your `-v` mount path is wrong. The path on the **left** of `:` must point to a real folder on your Windows disk. Double-check the path you copied.

- **"... C:/Program Files/Git/opt/spark/..."** (Git Bash only)
  Path got mangled by Git Bash. Run `export MSYS_NO_PATHCONV=1` in your shell once and try again.

- **Lots of red `INFO` / `WARN` text mixed with your output.**
  That's normal Spark logging. Your real output is under the `===` headers. To find it quickly, scroll up in the terminal.

- **First run is slow / hangs for a minute.**
  Spark JVM startup. About 30–60 seconds on first launch. Re-running is the same speed because the container is fresh — that's the trade-off of `--rm`. For interactive work, people use a Jupyter notebook with a long-lived Spark session.

---

## 10. Common student questions

### Q1. What is Spark, exactly?

**Spark is a fast distributed computing engine.** It takes a big job, splits it across many machines, runs the pieces in parallel, and combines the results. That's it — Spark is *just* the processing engine.

Why people love it:
- Keeps data in **memory** between steps (Hadoop MapReduce keeps writing to disk).
- 10–100× faster than MapReduce for most jobs.
- Friendly API: Python, Scala, SQL, Java.
- One tool for **batch jobs**, **streaming**, **machine learning**, and **graphs**.

---

### Q2. Does Spark work the same way as Hadoop?

**Same idea, different machinery.** Both follow "split the work, combine the results." But the implementation is different:

| | Hadoop MapReduce | Spark |
|---|---|---|
| Where intermediate data lives | Disk (HDFS) — slow | Memory (RAM) — fast |
| Code style | Imperative (write `mapper.py` + `reducer.py`) | Declarative (`df.groupBy().avg()`) |
| What it can do | Huge batch jobs only | Batch + ML + streaming + graphs |
| Speed | Slow startup, slow steps | Fast startup, fast steps |
| Lines of code for a typical job | 30–100+ | 5–10 |

So: same **concept**, much better **implementation**.

---

### Q3. Does Spark replace Hadoop?

This is the most-confused point in Big Data, because "Hadoop" actually means **three things bundled together**:

```
Hadoop = HDFS  +  YARN  +  MapReduce
         storage  scheduler  processing
```

Spark replaces **only MapReduce** — the processing part. It does **not** replace HDFS or YARN. In fact, in many companies Spark runs **on top of** HDFS and YARN:

```
Old:   HDFS  +  YARN  +  MapReduce      ← MapReduce does the work
New:   HDFS  +  YARN  +  Spark           ← Spark does the work, same storage and scheduler
```

So when people say *"Spark replaced Hadoop"* they almost always mean *"Spark replaced MapReduce."* HDFS and YARN are often still there.

**Modern reality (2025):** most new systems don't use HDFS at all anymore — they use **cloud storage** (S3, Google Cloud Storage, Azure Blob), which is cheaper and has no servers to manage. The common stack today is:

```
S3 / GCS / Azure  +  Kubernetes  +  Spark
   (storage)         (scheduler)    (processing)
```

No Hadoop in sight. Spark won precisely because it works **with or without** Hadoop.

---

### Q4. Do I still need Hadoop / HDFS for Spark?

No. Spark runs fine on your laptop, on a Spark cluster, on Kubernetes, or on cloud (Databricks, AWS EMR). It can **read from** HDFS, but it doesn't need it. In this lab we read from a normal folder mounted into the container — no HDFS in sight.

In production, Spark usually reads from S3 / GCS / HDFS / Delta Lake. The Python code stays the same — only the path changes (e.g., `s3://my-bucket/students.csv`).

### Q5. Why did we still learn MapReduce in Lab 2 if Spark replaces it?

Because the **idea** of split + combine is identical. MapReduce makes the choreography visible; Spark hides it. Without Lab 2 you'd treat `groupBy.avg` as magic. Now you know it's just a tidy wrapper over the same map/sort/reduce dance.

It's also still on a lot of legacy systems. You may not write new MapReduce jobs, but you'll read them.

### Q6. Is this faster than Pandas?

For our 15-row file? **No — Pandas wins.** Spark has a startup cost (the JVM, the session, the planner) that's overkill on tiny data.

The crossover is around the moment Pandas runs out of memory — typically a few GB on a laptop. Below that, Pandas. Above that, Spark.

### Q7. Why does Spark print so much INFO text?

Because by default it logs every internal step. We added `spark.sparkContext.setLogLevel("WARN")` to quiet most of it, but the Spark startup banner and a few WARN lines always survive. Your real output is between the `=== ... ===` headers we printed.

### Q8. Will I write `spark-submit` commands by hand at work?

Rarely. In real teams Spark jobs are run via:
- **Notebooks** (Databricks, Jupyter) — for interactive analysis.
- **Schedulers** (Airflow, Dagster) — for nightly batch jobs.
- **Streaming pipelines** — for jobs that run forever.

`spark-submit` is the building block underneath all of those. Knowing it once is enough.

---

## 11. The takeaway

Three sentences to remember:
1. **Spark is the modern Hadoop.** Same split + combine idea, much shorter code, much faster.
2. **A DataFrame is a table.** `groupBy`, `agg`, `filter`, `join` — same vocabulary as SQL or Pandas.
3. **You went from 30 lines of map/reduce plumbing (Lab 2) to one `groupBy.avg` (Lab 3).** That's why Spark won.
