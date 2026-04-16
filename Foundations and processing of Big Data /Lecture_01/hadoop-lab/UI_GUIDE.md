# Hadoop Web UIs — What They Do and How to Use Them

Hadoop comes with two built-in web dashboards. They are the easiest way to *see* what is happening inside the cluster. You only need a browser — no commands.

---

## 1. HDFS Dashboard — http://localhost:9870

This is the **NameNode's web page**. It lets you look inside the distributed file system.

### What you are looking at

When you open it, you land on the **Overview** tab. The header tells you:
- NameNode state (usually "Active").
- How much storage the cluster has, how much is used.
- How many DataNodes are connected.
- Whether Safe Mode is on or off (Safe Mode = read-only boot mode).

### The 5 tabs at the top — one line each

| Tab | What it shows |
|---|---|
| **Overview** | A summary: cluster health, storage, version, Safe Mode status. |
| **Datanodes** | Every DataNode in the cluster — its address, used space, free space, last contact time. |
| **Datanode Volume Failures** | Any disk failures across DataNodes. (Empty in a healthy cluster.) |
| **Snapshot** | Saved point-in-time copies of folders (advanced feature). |
| **Startup Progress** | Shows how the NameNode loaded its metadata when it started. |
| **Utilities ▾** | The useful one — contains **Browse the file system** and **Logs**. |

### Key sections to inspect

1. **Click "Datanodes"**
   - There will be 1 row (we only have 1 DataNode in this setup).
   - "In Operation" column should say `In Service`.
   - In a real cluster this table would have 10, 100, or 1000 rows.

2. **Click "Utilities → Browse the file system"**
   - Type `/` in the path box and press Enter → HDFS root appears.
   - Click **demo** → `words.txt` is listed.
   - Click **words.txt** → pop-up shows:
     - **Block Pool ID** — an internal ID for all blocks in this cluster.
     - **Block ID** — the unique ID of this file's block.
     - **Size** — file size in bytes.
     - **Availability** — which DataNodes have a copy of the block.
   - Every file stored in HDFS appears here. Every block is tracked. Every replica is tracked.

3. **Click "Utilities → Logs"**
   - Raw log files of the NameNode.
   - Rarely needed in practice, but good to know where it is.

### One-line summary

> The HDFS UI is a **file explorer + dashboard** for the distributed file system. Use it to verify uploads, inspect blocks, and check cluster storage.

---

## 2. YARN Dashboard — http://localhost:8088

This is the **ResourceManager's web page**. It shows every *job* (called an "application" in YARN) that has ever run.

### What you are looking at

When you open it, you land on the **Cluster Metrics** page. At the top you see counters:
- **Apps Submitted / Running / Completed** — how many jobs so far.
- **Containers Running** — how many worker processes are alive right now.
- **Memory Used / Total** — how much RAM the cluster has and is using.
- **Active Nodes** — number of healthy worker machines (1 in our case).

Below: the big table of applications.

### Key sections to inspect

1. **Watch a job appear live**
   - In one terminal, run the word-count MapReduce job (see `commands.md` section G).
   - In the browser, refresh http://localhost:8088 every 2 seconds.
   - The job goes through:
     - **ACCEPTED** (queued).
     - **RUNNING** (workers are doing the map and reduce).
     - **FINISHED** with **SUCCEEDED** in the Final Status column.

2. **Click the Application ID** (the blue link in the first column, e.g. `application_1776328181208_0001`)
   - Opens the application detail page.
   - Shows start time, end time, elapsed time, user, queue.

3. **Click the "History" link** on the same detail page
   - Per-task breakdown — how many map tasks ran, how many reduce tasks ran, how long each one took.
   - Useful for finding slow tasks in a real job.

4. **Click "Nodes" on the left sidebar**
   - Lists every NodeManager (worker machine).
   - Each row shows: node name, free memory, containers running, health.
   - YARN uses this information to decide *where* to send the next task.

5. **Click "Scheduler" on the left sidebar**
   - Queue structure. Jobs are submitted to queues, and the scheduler decides who runs next.

### One-line summary

> The YARN UI is a **job tracker + resource monitor**. Use it to watch jobs run, find finished jobs, and see which machines are busy.

---

## 3. How the two UIs fit together

```
You upload a file
       │
       ▼
  HDFS UI (9870)  ── the file and its blocks appear here
       │
       ▼
You run a MapReduce job on that file
       │
       ▼
  YARN UI (8088)  ── the job runs here
       │
       ▼
Output is written back to HDFS
       │
       ▼
  HDFS UI (9870)  ── the output folder and results appear here
```

Keep **both tabs open in the browser** and switch between them:
- Before the job: HDFS UI confirms the input file exists.
- During the job: YARN UI shows it running.
- After the job: HDFS UI shows the output folder.

---

## 4. End-to-end walkthrough (follow in order)

1. Open two browser tabs side by side: http://localhost:9870 and http://localhost:8088.
2. Run `docker compose up -d` (if cluster is stopped).
3. HDFS UI → Datanodes → 1 worker is visible. (In production there would be many.)
4. HDFS UI → Utilities → Browse filesystem → `/` is empty. HDFS starts empty.
5. Run the upload commands (commands.md sections D and E).
6. Refresh HDFS UI → `/` → `/demo` → `words.txt`. The file and its blocks are now visible.
7. Switch to YARN UI → no jobs yet.
8. Run the wordcount command (commands.md section G).
9. Refresh YARN UI every 2 seconds → job status changes ACCEPTED → RUNNING → FINISHED.
10. When FINISHED → click the Application ID → full breakdown of map/reduce tasks.
11. Switch back to HDFS UI → `/demo/wc_out` → the output folder exists.
12. Run the cat command (commands.md section H) → word counts appear.

Every concept from the theory section now matches something visible in the UIs and terminal.
