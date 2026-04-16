# Hadoop Lab — Ready-to-Copy Commands

Full command sequence for Lecture 01. Each command block can be copy-pasted as-is.

---

## A) Start the cluster

In **Ubuntu (WSL)** or **Git Bash on Windows**:
```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_01/hadoop-lab"
docker compose up -d
```

First run downloads ~1.5 GB. Later runs start in ~10 seconds.

Verify:
```bash
docker ps --filter 'name=hadoop-lab'
```
Expected: 4 containers running (`namenode`, `datanode`, `resourcemanager`, `nodemanager`).

Wait ~15 seconds for the NameNode to leave safe mode:
```bash
docker exec hadoop-lab-namenode-1 hdfs dfsadmin -safemode get
```
Expected: `Safe mode is OFF`.

---

## B) Open the web dashboards

Open in any browser on Windows:
- **HDFS UI** → http://localhost:9870
- **YARN UI** → http://localhost:8088

(See `UI_GUIDE.md` in this folder for what each one does and what to click.)

---

## C) One-time fix on Windows (Git Bash only)

Git Bash converts `/demo` into `C:/Program Files/Git/demo`, which breaks HDFS commands.
In each terminal session, run this **once**:

```bash
export MSYS_NO_PATHCONV=1
```

If you use Ubuntu (WSL) instead of Git Bash, you do not need this.

---

## D) HDFS folder + upload

```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -mkdir /demo
docker exec hadoop-lab-namenode-1 hdfs dfs -ls /
```
Expected output of `ls /`:
```
Found 1 items
drwxr-xr-x   - root supergroup          0 ...   /demo
```

Copy the sample file into the container, then push into HDFS:
```bash
docker cp sample_data/words.txt hadoop-lab-namenode-1:/tmp/words.txt
docker exec hadoop-lab-namenode-1 hdfs dfs -put -f /tmp/words.txt /demo/
docker exec hadoop-lab-namenode-1 hdfs dfs -ls /demo/
```

---

## E) Look at the blocks

```bash
docker exec hadoop-lab-namenode-1 hdfs fsck /demo/words.txt -files -blocks -locations
```

Key lines:
- `1 block(s)` → HDFS split the file into blocks.
- `blk_1073741825_1001` → block ID.
- `len=XXX` → block size in bytes.
- `Live_repl=1` → 1 replica (we set replication=1 in this setup; in production it would be 3).
- `DatanodeInfoWithStorage[172.18.0.4:9866, ...]` → which DataNode holds the replica.

---

## F) Read the file back

```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -cat /demo/words.txt
```

---

## G) Run MapReduce word count

```bash
docker exec hadoop-lab-namenode-1 hadoop jar \
  /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
  wordcount /demo/words.txt /demo/wc_out
```

Important: the output folder (`/demo/wc_out`) must **NOT** already exist. If you rerun, delete it first:
```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -rm -r /demo/wc_out
```

While the job runs, refresh http://localhost:8088 → the job moves ACCEPTED → RUNNING → FINISHED.

---

## H) View the results

```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -ls /demo/wc_out
docker exec hadoop-lab-namenode-1 hdfs dfs -cat /demo/wc_out/part-r-00000
```

Output shows each word with its count (`the 8`, `data 4`, etc.).

---

## I) Try a second MapReduce example

The same jar has many example jobs. Run `grep` (counts lines matching a regex):

```bash
docker exec hadoop-lab-namenode-1 hadoop jar \
  /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
  grep /demo/words.txt /demo/grep_out "the"
docker exec hadoop-lab-namenode-1 hdfs dfs -cat /demo/grep_out/part-r-00000
```

---

## J) Clean up HDFS (keeps cluster running)

```bash
docker exec hadoop-lab-namenode-1 hdfs dfs -rm -r /demo
```

---

## K) Stop the cluster

```bash
cd "/c/Users/Adnan/Desktop/ML/project/curriculum/lecture_01/hadoop-lab"
docker compose down
```

This stops and deletes all 4 containers. HDFS data is lost (stored inside containers). The downloaded Hadoop image stays on disk, so the next `docker compose up -d` is fast.

To also wipe the image (full reset):
```bash
docker compose down
docker image rm apache/hadoop:3.3.6
```
