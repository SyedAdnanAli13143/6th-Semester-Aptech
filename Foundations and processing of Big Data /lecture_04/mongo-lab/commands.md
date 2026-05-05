# Lab 4 — MongoDB (Beginner Friendly)

So far in Labs 1–3 you stored data as **rows in CSV files** and processed them with Hadoop / Spark. Every row had to follow the same schema — the same columns in the same order.

Lab 4 is different. **MongoDB stores data as documents** — flexible, JSON-like, no fixed columns. This is called **NoSQL**, and it's what powers most modern apps: Instagram, Uber, eBay, Airbnb.

---

## 1. The idea (read this first)

In a SQL database (or a CSV), data is a table — same columns for every row:

```
student_id | name   | course | score
-----------+--------+--------+------
S001       | Ali    | Math   | 82
S002       | Sara   | Math   | 45
```

In MongoDB, data is a **collection of documents**. A document is just a JSON object:

```json
{ "student_id": "S001", "name": "Ali", "course": "Math", "score": 82 }
{ "student_id": "S002", "name": "Sara", "course": "Math", "score": 45 }
```

Same data — but each document **can have its own shape**. One student might have 5 fields, another might have 10. No `ALTER TABLE`, no migrations.

The big advantage: **nested data**. In SQL, if a student has multiple parents and multiple hobbies, you need 3 tables and JOINs. In MongoDB, you just write it inline:

```json
{
  "name": "Ali",
  "hobbies": ["cricket", "reading", "coding"],
  "parents": [
    { "relation": "father", "name": "Ahmed" },
    { "relation": "mother", "name": "Sara"  }
  ]
}
```

One document, no joins.

---

## 2. The vocabulary (super short)

| SQL world | MongoDB world |
|---|---|
| Database | Database |
| Table | **Collection** |
| Row | **Document** |
| Column | Field |
| `INSERT INTO ...` | `db.col.insertOne({...})` |
| `SELECT ... WHERE ...` | `db.col.find({...})` |
| `GROUP BY` | `aggregate([{ $group: ... }])` |

That's almost everything you need to read MongoDB code.

---

## 3. Start MongoDB

Open **PowerShell** or **Git Bash** on Windows.

Pull the image (one-time, ~250 MB):
```bash
docker pull mongo:7
```

Start a container with the standard port forwarded:
```bash
docker run -d --name mongo-lab -p 27017:27017 mongo:7
```

Check it's running:
```bash
docker ps --filter "name=mongo-lab"
```

You should see `mongo-lab` with status `Up ...`.

---

## 4. Load the demo data

The lab folder ships with `seed.js` — it inserts 15 student documents and 1 profile document.

Move into the lab folder:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_04/mongo-lab"
```

Pipe the seed script into the container's `mongosh`:
```bash
docker exec -i mongo-lab mongosh < seed.js
```

You should see at the end:
```
students inserted: 15
profiles inserted: 1
```

---

## 5. Open the interactive shell

```bash
docker exec -it mongo-lab mongosh
```

You're now inside MongoDB's shell. The prompt is `>` (or `test>`).

Switch to our database:
```js
use school
```

(In MongoDB, a database is created the moment you write to it. No `CREATE DATABASE` needed.)

List collections:
```js
show collections
```

You should see `students` and `profiles`.

---

## 6. Find queries (the basics)

### Find everything
```js
db.students.find()
```
Prints all 15 documents. Type `it` to see more if it stops mid-list.

### Find one
```js
db.students.findOne({ name: "Ali" })
```
Returns the first matching document.

### Filter by a field
```js
db.students.find({ course: "Math" })
```
Only Math rows.

### Filter with a comparison operator
```js
db.students.find({ score: { $gte: 80 } })
```
All students who scored ≥ 80. (`$gte` = greater than or equal.)

Other operators you'll use a lot:
- `$gt`, `$lt`, `$lte` — comparisons
- `$eq`, `$ne` — equal / not equal
- `$in: [a, b, c]` — value is one of these
- `$and`, `$or` — combine conditions

Example combining two:
```js
db.students.find({ course: "Math", passed: 1 })
```
(comma-separated conditions = AND.)

### Project only some fields
```js
db.students.find({ course: "Math" }, { _id: 0, name: 1, score: 1 })
```
The second `{}` is the **projection** — `1` = include, `0` = exclude. We hide `_id` and only keep `name` and `score`.

### Count
```js
db.students.countDocuments({ passed: 1 })
```
You should get **11**.

---

## 7. Aggregation — the GROUP BY equivalent

This is where MongoDB feels most like SQL. The **aggregation pipeline** is a list of stages, each transforming the data.

### Average score per student

```js
db.students.aggregate([
  { $group: { _id: "$student_id", avg_score: { $avg: "$score" } } },
  { $sort:  { _id: 1 } }
])
```

Expected (same answers as Labs 2 and 3):
```
{ _id: 'S001', avg_score: 75.33333333333333 }
{ _id: 'S002', avg_score: 57.666666666666664 }
{ _id: 'S003', avg_score: 57 }
{ _id: 'S004', avg_score: 87.33333333333333 }
{ _id: 'S005', avg_score: 42.666666666666664 }
```

How to read it:
- `$group` — bucket documents by `student_id`. The bucket key goes into `_id`.
- `$avg: "$score"` — for each bucket, average the `score` field. (The `$` in `"$score"` means "the value of this field".)
- `$sort: { _id: 1 }` — sort ascending by `_id`.

### Pass count per course

```js
db.students.aggregate([
  { $group: { _id: "$course", students_passed: { $sum: "$passed" } } },
  { $sort:  { _id: 1 } }
])
```

Expected:
```
{ _id: 'English', students_passed: 4 }
{ _id: 'Math',    students_passed: 3 }
{ _id: 'Science', students_passed: 4 }
```

`$sum: "$passed"` adds up the `passed` field (which is 1 or 0 in our data) — same trick as `SUM(passed)` in SQL.

---

## 8. The document advantage — nested data

Now the cool part. Look at the `profiles` collection:

```js
db.profiles.findOne()
```

You'll see something like:
```json
{
  "_id": ObjectId("..."),
  "student_id": "S001",
  "name": "Ali",
  "contact": { "email": "ali@school.edu", "phone": "0300-1234567" },
  "hobbies": ["cricket", "reading", "coding"],
  "parents": [
    { "relation": "father", "name": "Ahmed" },
    { "relation": "mother", "name": "Sara"  }
  ]
}
```

In SQL this would need 3–4 tables (`students`, `contacts`, `hobbies`, `parents`) and JOINs every time you read. In MongoDB, it's one document.

Query into nested fields with **dot notation**:
```js
db.profiles.findOne({ name: "Ali" }, { _id: 0, "contact.email": 1 })
```
Returns just the email:
```
{ "name": "Ali", "contact": { "email": "ali@school.edu" } }
```

Search inside an array — find anyone whose hobbies include "coding":
```js
db.profiles.find({ hobbies: "coding" })
```

That's the document database superpower.

---

## 9. Insert / update / delete

```js
// insert one new row
db.students.insertOne({ student_id: "S006", name: "Bilal", course: "Math", score: 95, passed: 1 })

// update a field
db.students.updateOne({ student_id: "S006" }, { $set: { score: 99 } })

// delete a row
db.students.deleteOne({ student_id: "S006" })
```

`updateMany` and `deleteMany` work the same way but apply to all matching documents.

To leave the shell:
```js
exit
```

---

## 10. Clean up

Stop and remove the container:
```bash
docker stop mongo-lab
docker rm mongo-lab
```
(All data was inside the container — it's gone now. To keep data across restarts, mount a volume: `-v mongo-data:/data/db`.)

---

## 11. Common errors

- **"name in use" when running `docker run`.** The container already exists from a previous run. Either reuse it (`docker start mongo-lab`) or remove it first (`docker rm -f mongo-lab`).

- **"Connection refused" on port 27017.** The container hasn't finished starting yet. Wait 3–5 seconds and try again, or check `docker logs mongo-lab`.

- **`db.students` is empty in the shell.** You probably forgot `use school` — by default mongosh uses the `test` database.

- **`SyntaxError` on the `$` character.** In **PowerShell**, `$` starts a variable. If you paste a multi-line aggregation into PowerShell directly, escape it as `` `$ `` or run it inside `mongosh` (where `$` is fine).

---

## 12. Common student questions

### Q1. What is MongoDB?

A **NoSQL database** that stores data as **documents** (JSON-like objects) instead of rows. It's the most popular non-relational database in the world. Used by Uber, eBay, Adobe, EA Games, the New York Times, and most modern app backends.

You don't define a schema up front. You just `insertOne(...)` and the document is saved. Each document in the same collection can have different fields.

### Q2. How is it different from SQL (MySQL / Postgres)?

| | SQL (MySQL, Postgres) | MongoDB |
|---|---|---|
| Data shape | Rigid tables, fixed columns | Flexible documents (JSON) |
| Schema | Defined up front | Optional, per-document |
| Joining tables | First-class — `JOIN` everywhere | Avoided — embed nested data instead |
| Query language | SQL | JavaScript-like methods (`.find`, `.aggregate`) |
| Strength | Complex relationships, strict consistency | Fast iteration, nested data, web-scale |
| Weakness | Rigid; schema changes are painful | No global JOINs; analytical queries are clunkier |

Rule of thumb: **SQL** for finance / banking / strict relational data; **MongoDB** for app data, user profiles, content management, IoT.

### Q3. Is MongoDB Big Data?

Sort of. MongoDB **scales horizontally** (you can shard it across many servers), so it can hold billions of documents. But it's not a "Big Data" tool in the Hadoop / Spark sense — it's an **operational database**, designed for fast reads and writes from an app, not for running massive analytical jobs over the whole dataset.

In practice, big systems use **both**:
- **MongoDB** — live app data (user profiles, posts, sessions).
- **Hadoop / Spark / BigQuery** — analytics over all that data, run nightly.

### Q4. Does MongoDB replace HDFS / Hadoop?

No. They solve different problems:
- HDFS = a distributed **file system** for huge raw files.
- MongoDB = a distributed **database** for structured JSON-ish records.

You'd put log files in HDFS, but user profiles in MongoDB.

### Q5. When do I pick MongoDB?

Pick MongoDB when:
- Your data is **shaped like JSON** (nested, varying fields).
- You need **fast reads/writes from a web or mobile app**.
- Your schema **evolves often** (you add fields all the time).
- You don't need complex multi-table JOINs.

Pick SQL when:
- Data is highly **relational** (orders, products, customers, invoices).
- You need **transactions** spanning multiple tables.
- Reports / analytics queries dominate.

### Q6. Why JavaScript syntax in mongosh?

MongoDB's shell is literally a JavaScript engine. `db.students.find(...)` is a JavaScript method call on an object. You can use loops, variables, even `function` definitions inside the shell. From Python, the equivalent library is **PyMongo** (`pip install pymongo`) — same concepts, Python syntax.

---

## 13. The takeaway

Three sentences to remember:
1. **A document is a JSON object. A collection is a folder of documents. That's MongoDB.**
2. **No fixed schema** — documents in the same collection can have different fields. Great for flexible app data, less great for strict reports.
3. **`find` for queries, `aggregate` for GROUP BY.** Once you know those two, you can read 90% of MongoDB code.
