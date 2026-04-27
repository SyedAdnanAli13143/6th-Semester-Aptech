# Lab 2 — MapReduce in Python (Beginner Friendly)

In Lab 1 you ran a **ready-made** wordcount program. Here you'll write your **own** mini-program in Python and run it on the same Hadoop cluster.

---

## 1. The idea (read this first)

Imagine your teacher gives you a stack of exam papers from 5 students. Each student took 3 exams. You want the **average score for each student**.

How would you do it by hand?

**Step 1 — Map (sort papers into piles).**
Walk through the stack. For each paper, write a sticky note: `student_id → score`. Put it on that student's pile.

**Step 2 — Reduce (do math on each pile).**
For each pile, add the scores and divide by 3. That's the student's average.

**That's MapReduce.** Map = label each item. Reduce = crunch each pile.

The cool part: if the stack had 1 million papers, you could give 10 friends 100,000 papers each (Map runs in parallel). Then collect the piles and let 10 friends compute averages (Reduce runs in parallel). One huge job → many small jobs at the same time. That's how Hadoop scales.

```
Input rows  ──▶  Mapper labels each row  ──▶  Hadoop groups same labels  ──▶  Reducer crunches each group  ──▶  Output
```

---

## 2. Our data

`sample_data/students.csv` (already provided):
```
student_id,name,course,score,passed
S001,Ali,Math,82,1
S001,Ali,Science,76,1
S001,Ali,English,68,1
S002,Sara,Math,45,0
...
```

Each student appears 3 times (one row per exam). We want each student's **average score**.

---

## 3. The two Python files

### `mapper.py` — labels each row

```python
import sys
for line in sys.stdin:
    parts = line.strip().split(",")
    if parts[0] == "student_id":   # skip header
        continue
    student_id = parts[0]
    score = parts[3]
    print(f"{student_id}\t{score}")
```

What it does: read one line, print `student_id` then a TAB then `score`. That's it.

The mapper does **not** compute averages. It just labels.

### `reducer.py` — averages each group

```python
import sys
current, total, count = None, 0.0, 0
for line in sys.stdin:
    student_id, score = line.strip().split("\t")
    if student_id != current:
        if current is not None:
            print(f"{current}\t{total/count:.2f}")
        current, total, count = student_id, 0.0, 0
    total += float(score)
    count += 1
if current is not None:
    print(f"{current}\t{total/count:.2f}")
```

What it does: walk through the lines (which arrive **sorted by student_id**). Keep a running total. When the student_id changes, that means we finished a student — print their average and start fresh.

That last `if current is not None:` after the loop is to print the **last** student. Easy to forget.

---

## 4. Try it on your laptop first (no Hadoop yet)

Move into the lab folder:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_02/streaming-lab"
```

Run the whole pipeline as a Unix pipe:
```bash
cat sample_data/students.csv | python mapper.py | sort | python reducer.py
```

You should see:
```
S001    75.33
S002    57.67
S003    57.00
S004    87.33
S005    42.67
```

What just happened?
- `cat` — feeds the file in.
- `mapper.py` — labels every row.
- `sort` — groups same student_ids together. **This is what Hadoop does for free.**
- `reducer.py` — averages each group.

This is exactly what Hadoop will do, just on your laptop. **If it works here, it'll work on Hadoop.** Always test like this first — it saves a lot of time.

---

## 5. Now run it on Hadoop

We use the same cluster from Lab 1. Make sure it's running:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_01/hadoop-lab"
docker compose up -d
```

Go back to the Lab 2 folder:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_02/streaming-lab"
```

If you're on Git Bash, run this once so paths work:
```bash
export MSYS_NO_PATHCONV=1
```

### 5a. Put the CSV into HDFS

The `hdfs` command lives **inside** the container, so we copy the file in two hops: laptop → container → HDFS.
```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -mkdir -p /demo
docker cp sample_data/students.csv hadoop-lab-namenode-1:/tmp/students.csv
docker exec hadoop-lab-namenode-1 hdfs dfs -put -f /tmp/students.csv /demo/
```

### 5b. Send the Python scripts into the container

```bash
docker cp mapper.py  hadoop-lab-namenode-1:/tmp/mapper.py
docker cp reducer.py hadoop-lab-namenode-1:/tmp/reducer.py
```

### 5c. Run the job

```bash
docker exec hadoop-lab-namenode-1 hadoop jar \
  /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -files /tmp/mapper.py,/tmp/reducer.py \
  -mapper  "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -input  /demo/students.csv \
  -output /demo/avg_out
```

Plain-English translation:
> "Hey Hadoop — take these two Python files. Use the first one as the mapper, the second one as the reducer. Read input from `/demo/students.csv`. Write the result to `/demo/avg_out`."

Open http://localhost:8088 and you'll see the job go ACCEPTED → RUNNING → FINISHED, just like the wordcount in Lab 1.

### 5d. Read the result

```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -cat /demo/avg_out/part-00000
```

```
S001    75.33
S002    57.67
S003    57.00
S004    87.33
S005    42.67
```

**Same answer as your laptop test.** That's the whole point — your tiny laptop pipe and the big Hadoop cluster ran the exact same Python and got the exact same answer.

---

## 6. Two things students often hit

- **"Output folder already exists" error** when you re-run the job.
  Hadoop refuses to overwrite a previous result. Delete it and try again:
  ```bash
  docker exec hadoop-lab-namenode-1 hdfs dfs -rm -r /demo/avg_out
  ```

- **"No such file or directory" on the Python script** even though the file is right there.
  Means the file was saved with Windows line endings (CRLF). In VSCode bottom-right corner, click `CRLF` → choose `LF` → save. Try again.

---

## 7. Clean up

```bash
# delete lab data, keep cluster running
docker exec hadoop-lab-namenode-1 hdfs dfs -rm -r /demo

# or stop the cluster completely
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_01/hadoop-lab"
docker compose down
```

---

## 8. The takeaway

Three sentences to remember:
1. **Mapper labels each row. Reducer crunches each group. Hadoop sorts in between.**
2. **Mappers run in parallel because each row is independent.** That's how Hadoop handles 1 TB the same way as 1 MB.
3. **You can test the whole thing as a Unix pipe on your laptop** — `cat | mapper | sort | reducer` is identical to what Hadoop does, just smaller.

---

## 9. Common student questions

### Q1. How is Hadoop / Big Data actually used in real life?

Big companies have **way more data than one computer can hold**, so they use Hadoop to spread it across many machines and process it together.

Real examples:
- **Facebook / Instagram** — every like, comment, photo, friend connection. Billions of events per day.
- **Netflix** — every show you watch, pause, skip. Used to recommend "what to watch next".
- **Banks** — every credit-card transaction. Used to detect fraud (e.g., "your card was just used in 2 countries within 5 minutes — block it").
- **Amazon** — every search and click. Used for "people who bought X also bought Y".
- **Telecom companies** — every call, every SMS, every data session.
- **YouTube** — 500 hours of video uploaded **every minute**.

The pattern is always the same:
> "We have so much data that no single computer can store or process it. So we split it across 100 / 1000 / 10000 machines, and each one works on a small piece. Then combine the answers."

That "split + combine" idea is exactly what your `mapper.py` and `reducer.py` are doing — just on a tiny scale.

---

### Q2. Can we do this normally (without Hadoop)?

**Yes — if your data is small.** This is important to understand.

| Data size | Tool to use |
|---|---|
| Few MBs (an Excel file) | Excel, Pandas |
| Up to a few GBs | Python + Pandas, or MySQL |
| 10–100 GB | MySQL / Postgres on a strong server |
| Hundreds of GB to TBs | Hadoop, Spark |
| Petabytes | Hadoop / Spark on big clusters |

**Don't use Hadoop for small data.** It's overkill — like using a truck to deliver one pizza.

In our lab, the CSV is tiny (15 rows). We could solve it with 2 lines of Pandas:
```python
import pandas as pd
df = pd.read_csv("students.csv")
print(df.groupby("student_id")["score"].mean())
```

That gives the same answer — **in a millisecond**, on your laptop, no Hadoop needed.

So why are we using Hadoop here? Because we're **learning the pattern**. The pattern is the same whether the file is 15 rows or 15 billion rows. Once you know map + reduce, you can scale it.

> **Rule of thumb:** Hadoop is for when "Pandas crashed" or "MySQL is too slow". Until then, use the simple tool.

---

### Q3. Will we have to run these commands again and again?

**For learning (this lab) — yes**, because you're seeing what each step does. Run it, watch it, understand it.

**In real life — no, almost never.** Real companies don't have a person typing `hadoop jar ...` every morning. Instead:

- **Scheduled jobs.** A tool like **Apache Airflow**, **Oozie**, or even basic **cron** runs the job automatically. Example: "every night at 2 AM, process yesterday's sales and update the dashboard."
- **Triggered jobs.** When new data arrives in HDFS, a pipeline kicks off automatically.
- **Pipelines.** One job's output is another job's input — chained together. The whole chain runs on its own.

So in practice:
1. An engineer **writes** the mapper/reducer (or Spark job) **once**.
2. Saves it in a script.
3. Schedules it to run automatically forever.
4. Nobody types `hadoop jar` anymore — it just runs.

That's why the script is the important part, not the typing. **The script is the product.** The commands are just how you launch it during development.


