# Module 01 — Foundations of Big Data + Hadoop Architecture

## Part 1 — Theory (easy version)

### 1.1 What is Big Data?

**Big Data** is just **data that is too big, too fast, or too messy for one normal computer to handle.**

Real-life examples you already know:

1. **Your phone's photo gallery.** 100 photos — no problem. 10,000 photos over 5 years plus 4K videos — your phone starts lagging. Now imagine Google Photos storing *everyone's* pictures. That is Big Data.
2. **YouTube.** Every minute, about 500 hours of video get uploaded. No single computer can store or process that.
3. **WhatsApp messages.** Billions of messages every day flying across the world. One database server would melt.

So when data grows past what a single computer can manage, we need a different approach — Big Data tools.

### 1.2 The 5 V's — the official definition

We describe Big Data using **5 V's** (five words that start with V):

| V | What it means | Easy example |
|---|---|---|
| **Volume** | How *much* data | Facebook stores billions of photos |
| **Velocity** | How *fast* data comes in | Stock prices change every second |
| **Variety** | How *many kinds* of data | Text messages, photos, videos, voice notes — all mixed |
| **Veracity** | How *trustworthy* the data is | Some reviews on Amazon are fake or spam |
| **Value** | What *useful insight* you get | Netflix recommending shows you actually like |

**In our projects' world:**
- EarthScape Climate → Volume (years of satellite data), Velocity (sensors sending data every second), Variety (images + numbers + text).
- EduPredict → Volume (millions of student records), Variety (attendance + grades + login logs), Value (predicting which students need help).

### 1.3 Why normal databases (like MySQL) cannot do this

*(MySQL = a popular traditional database — stores data in rows and columns, like Excel, runs on one computer.)*

Imagine a **small restaurant with one chef.**
- 5 customers: fine.
- 50 customers: slow.
- 500 customers at once: total disaster.

A normal database like MySQL is that one chef. It lives on one computer. When data gets too big, there is nothing the chef can do — he is only one person.

Three big problems:
1. **The computer's disk fills up.** You cannot just keep adding more disks forever.
2. **Buying a bigger computer is expensive and has a limit.** Even the biggest server in the world has a ceiling.
3. **Queries become painfully slow.** Joining two tables with billions of rows on one machine can take hours.

### 1.4 The Big Data idea — "divide the work"

The solution is simple: **instead of one chef, hire 100 chefs working together.**

Two tricks make this work:

1. **Split the food (data) into small pieces** and put different pieces in different kitchens (computers).
2. **Send the recipe (code) to each kitchen** so all chefs cook their piece at the same time.

Real-life analogies:

1. **A library.** One librarian with 10 million books → impossible to find anything. 100 librarians, each in charge of a section → you ask, they all search their section in parallel, answer comes back fast.
2. **Checking exam papers.** One teacher checking 1000 papers takes days. 20 teachers checking 50 papers each finish in a morning.
3. **Cleaning a big hall.** One person takes 10 hours. 10 people take 1 hour.

Hadoop was the first open-source tool that did this for data.

### 1.5 Hadoop — three main parts

Hadoop has **three pieces** that work together:

```
+---------------------------------------+
|              HADOOP                   |
|                                       |
|   HDFS       YARN       MapReduce     |
|  (storage)  (manager)  (processing)   |
+---------------------------------------+
```

Think of it like a **pizza delivery company:**
- **HDFS** = the warehouse where all ingredients are stored.
- **YARN** = the manager who assigns orders to delivery riders.
- **MapReduce** = the riders who actually cook and deliver.

#### A) HDFS — Hadoop Distributed File System

**What it does:** stores huge files by splitting them and spreading the pieces across many computers.

Rules:
- Break every file into **blocks of 128 MB**.
- Make **3 copies** of each block and put them on different computers (so if one machine dies, your data survives).
- Two types of computers in HDFS:
  - **NameNode** = the boss. Remembers which block is on which computer. (Only one main NameNode.)
  - **DataNodes** = the workers. Actually hold the blocks. (Many — could be 10, 100, or 1000.)

Real-life examples:

1. **Chapters of a book spread among friends.** You give chapter 1 to Ali, chapter 2 to Sara, chapter 3 to Omar. You also give a backup copy of each chapter to one more friend, in case someone loses theirs. You keep a notebook that says "chapter 1 is with Ali and Fatima." You are the **NameNode**. Your friends are **DataNodes**. The notebook is the **metadata**.
2. **Google Drive on 1000 servers.** Your file is not really on one server. Google splits and copies it across many.
3. **A pizza sliced and stored in different fridges.** If one fridge breaks, other fridges still have slices.

#### B) YARN — Yet Another Resource Negotiator

**What it does:** decides which computer runs which piece of work.

- **ResourceManager** = the main manager (one).
- **NodeManager** = a helper on every worker machine, reports "I have X RAM and Y CPU free."
- **ApplicationMaster** = a temporary supervisor created for each job.

Real-life examples:

1. **A call-center manager** assigning incoming calls to agents based on who is free.
2. **A school principal** deciding which teacher takes which class period.
3. **Uber's app** picking the nearest available driver for your ride.

#### C) MapReduce — the processing model

**What it does:** runs your code on every piece of data in parallel, then combines the answers.

Two steps:
- **Map**: do something small to each record (like tagging).
- **Reduce**: combine all those small results into a final answer.

The classic example: **counting words in a book.**

Imagine you have a 10,000-page book and want to count how many times each word appears.

Step 1 — **Map** (give each page to a different person):
```
Page 1: "the cat sat"   →  the=1, cat=1, sat=1
Page 2: "the dog ran"   →  the=1, dog=1, ran=1
Page 3: "the cat ran"   →  the=1, cat=1, ran=1
```

Step 2 — **Shuffle** (group by word):
```
the → [1,1,1]
cat → [1,1]
sat → [1]
dog → [1]
ran → [1,1]
```

Step 3 — **Reduce** (sum the counts):
```
the = 3,  cat = 2,  sat = 1,  dog = 1,  ran = 2
```

More real-life examples of Map → Reduce thinking:

1. **Counting votes in an election.** Each polling station counts its own ballots (Map). The central office adds all station totals to get the final result (Reduce).
2. **Summing sales for a company with 100 branches.** Each branch calculates its monthly total (Map). Head office adds all 100 branch totals together (Reduce).
3. **Counting how many students passed each subject across 50 schools.** Each school counts its own students per subject (Map). The ministry adds them up across all schools (Reduce).

Today we usually use **Spark** instead of MapReduce (10–100× faster because it uses RAM, not disk). But MapReduce is the idea everything else is built on, so you must understand it first.

### 1.6 The Hadoop ecosystem (other tools you will hear about)

Hadoop has many friends. One sentence each:

*(Before the table: **SQL** is a simple language to ask questions from tables of data, like "give me all students with marks above 80". **NoSQL** means databases that do not use tables — they store flexible, JSON-like documents.)*

| Tool | What it does (simple) |
|---|---|
| **Hive** | Lets you write **SQL** on Hadoop instead of writing code. |
| **Impala** | Like Hive but gives results faster (good for dashboards). |
| **HBase** | A **NoSQL** database that sits on top of HDFS. |
| **Sqoop** | Copies data **between MySQL-type databases and HDFS**. |
| **Flume** | Pulls **log files** into HDFS. |
| **Kafka** | A pipe for **real-time events** (like a WhatsApp group — messages flow through). |
| **Spark** | A faster, friendlier replacement for MapReduce. |
| **Spark Streaming** | Same as Spark but for **live data** that keeps arriving. |
| **Oozie / Airflow** | A scheduler — runs your jobs at fixed times (like "every night at 2 AM"). |
| **Zookeeper** | The "traffic cop" that keeps all these tools in sync. |
| **Pig** | Old scripting language for data (rarely used now). |
| **Mahout** | Old machine-learning library (replaced by Spark MLlib). |
| **Ambari / Cloudera Manager** | A dashboard to manage the whole cluster. |

### 1.7 How these tools fit together in a real project

```
 Data sources        Move in          Store            Process          Show
 -------------    -------------    -----------    --------------    -----------
 Satellites  →→   Kafka         →→  HDFS       →→  Spark         →→  Tableau
 Sensors    →→    Flume         →→  (raw)      →→  Spark SQL     →→  Dashboards
 MySQL DB   →→    Sqoop         →→  HDFS + Hive→→  Spark MLlib   →→  MongoDB
 LMS logs   →→    Kafka         →→  HDFS       →→  Streaming     →→  Alerts
```

### 1.8 Common confusions (do not believe these)

- **"Hadoop = Big Data."** No. Hadoop is *just one* tool for Big Data. There are many others (for example, cloud services from Amazon, Google, and Microsoft that do similar things).
- **"Spark replaces Hadoop completely."** No. Spark replaces *MapReduce* only. Spark still uses **HDFS** for storage.
- **"MongoDB is Big Data."** Alone, no. MongoDB is just a flexible database. It becomes part of a Big Data stack when combined with HDFS, Kafka, and so on.
- **"More data is always better."** Only if the data is clean and relevant. 1 GB of clean data beats 1 TB of junk.

### 1.9 Glossary — every keyword in one place

| Keyword | Simple meaning |
|---|---|
| **Big Data** | Data too big, too fast, or too messy for one normal computer. |
| **Cluster** | Many computers working together as one system. |
| **Node** | One single computer inside a cluster. |
| **Distributed** | Work or data spread across many computers. |
| **Parallel** | Many things being done at the same time. |
| **HDFS** | Hadoop's file system — stores files by splitting them across nodes. |
| **Block** | A small piece of a file (default 128 MB) stored inside HDFS. |
| **Replication** | Keeping extra copies of each block for safety (default 3 copies). |
| **NameNode** | The "boss" computer in HDFS that tracks which block is where. |
| **DataNode** | A "worker" computer in HDFS that actually holds blocks. |
| **Metadata** | Information *about* data — for example, "block X is on computer Y". |
| **YARN** | Hadoop's manager — decides which node runs which job. |
| **ResourceManager** | The main manager in YARN. |
| **NodeManager** | A YARN helper that runs on each worker and reports free CPU/RAM. |
| **ApplicationMaster** | A short-lived supervisor created for each job. |
| **MapReduce** | A way to process data in two steps: Map (per item) + Reduce (combine). |
| **Map** | Step that processes each record in parallel. |
| **Shuffle** | Step that groups records with the same key together. |
| **Reduce** | Step that combines grouped records into final answers. |
| **Spark** | A faster replacement for MapReduce (uses RAM instead of disk). |
| **MySQL** | A traditional database that stores data in tables, runs on one computer. |
| **SQL** | A simple language to ask questions from tables ("SELECT * FROM students"). |
| **NoSQL** | A database that does *not* use tables — stores flexible documents. |
| **RAM** | Computer's fast working memory (much faster than disk). |
| **Disk** | The slow but large storage of a computer (hard disk / SSD). |
| **Docker** | A tool that runs software inside ready-made packages called containers. |
| **Container** | A small, ready-to-run package containing an OS and an app together. |
| **Image** | The template used to create containers (like a recipe). |
| **WSL** | Windows Subsystem for Linux — a Linux terminal inside Windows. |

---

### 1.10 Docker — why we use it, and its alternatives

Before the practical starts, a quick word about **Docker** — the main tool we are about to use.

#### The problem Docker solves

If you tried to install Hadoop on Windows the normal way, you would have to:
1. Install the right version of Java.
2. Download Hadoop, unzip it, edit 5–10 config files.
3. Set up SSH keys between the NameNode and DataNodes.
4. Make sure network ports and hostnames are correct.
5. Pray it does not clash with other software already on your laptop.

One wrong setting and Hadoop will not start, with error messages that are hard to understand. Beginners waste days here.

#### What Docker does (in simple words)

Docker **packages an application plus everything it needs (OS files, libraries, configs) into a single downloadable file called an *image*.** When you run an image, Docker creates a **container** — a small, isolated mini-computer with the app already working correctly.

So instead of installing Hadoop by hand, we say "run the Hadoop image" and Docker gives us a working Hadoop in about 30 seconds.

#### Real-life analogy

Think of Docker images as **frozen pizzas.**
- A frozen pizza is a ready-made meal — dough, sauce, cheese, toppings all in one package.
- You put it in any oven and it works every time.
- Without it, you would need flour, tomatoes, cheese, spices — and you might still mess it up.

Docker images are the frozen pizzas. Your computer is the oven. `docker run` puts the pizza in the oven.

Two more analogies:
- **Shipping containers.** A container can hold anything — shoes, books, TVs — and any ship can carry it. Docker containers do the same for software.
- **APK files on Android.** One file, install anywhere, works the same on every phone.

#### Container vs Virtual Machine (important)

People often confuse Docker with virtual machines (VMs). They are not the same:

| | Virtual Machine | Container (Docker) |
|---|---|---|
| Contains | A full operating system + apps | Just the app + its libraries |
| Size | Several GB | Tens of MB to a few hundred MB |
| Startup time | 30–60 seconds | 1–2 seconds |
| Isolation | Very strong (hardware level) | Strong (operating-system level) |
| Examples | VirtualBox, VMware, Hyper-V | Docker, Podman |

Use a VM when you need a totally different operating system. Use a container when you just want an app to run the same everywhere.

#### Why Docker is the right choice for Big Data learning

- **One YAML file gives you a whole Hadoop cluster.** No long install guides.
- **You can delete everything and start fresh** without touching your Windows installation.
- **Everyone gets identical software** — no "it works on my machine" problems.
- **Containers are small and start fast**, so a laptop with 8 GB RAM can run the stack.

#### Alternatives to Docker

Docker is the most popular but not the only option:

| Tool | Notes |
|---|---|
| **Podman** | Almost identical to Docker, no background service. Used where Docker's license is a concern. |
| **containerd** | The engine underneath Docker. Low-level — usually not used directly. |
| **LXC / LXD** | Older Linux container tool. Feels more like "tiny VMs". |
| **VirtualBox / VMware / Hyper-V** | Full virtual machines. Heavier and slower, stronger isolation. |
| **Cloudera QuickStart / Hortonworks Sandbox** | Pre-built virtual machines with Hadoop already installed. Big downloads (~10 GB). Good if you prefer a GUI. |
| **Install Hadoop natively on Linux** | Possible but painful. Not recommended for beginners. |
| **Cloud services (AWS EMR, Azure HDInsight, Google Dataproc)** | Hadoop/Spark as a service — no local install. Costs money. Used for real production work. |

For learning on a laptop, **Docker is the smallest, fastest, easiest path** — that is why we use it.

---

## Part 2 — Practical (Windows, from zero, nothing installed)

This whole section assumes you are on **Windows 10 or Windows 11** with **nothing installed**. By the end you will have a small Hadoop cluster running on your own laptop and you will have run a real MapReduce job.

Total time: ~45–60 minutes (most of it is downloads running in the background).

> **Lab folder:** everything for this section is inside [`hadoop-lab/`](hadoop-lab/):
> - `docker-compose.yml` — the ready-to-run cluster definition (tested).
> - `commands.md` — every command in copy-paste order with expected output.
> - `UI_GUIDE.md` — what the two web dashboards do and how to use them.
> - `sample_data/words.txt`, `sample_data/students.csv` — data to load and process.
>
> The whole `hadoop-lab/` folder is self-contained — copy it anywhere.

### Before you start — check these

| What | Need | How to check |
|---|---|---|
| Windows version | Windows 10 (build 19044+) or Windows 11 | Start menu → type **winver** → Enter |
| RAM | At least **8 GB** (16 GB recommended) | Start menu → **System information** |
| Free disk space | At least **20 GB** on C: | File Explorer → This PC |
| Virtualization | Must be **enabled in BIOS** | Task Manager → Performance → CPU → look at "Virtualization: Enabled" |

If "Virtualization" shows **Disabled**, reboot into BIOS (press F2/F10/Del during boot), find the setting "Intel VT-x" or "AMD-V", enable it, save, and restart. Docker will not run without this.

### Two terminals — know the difference

You will use **two different terminals** in this practical:
- **Windows PowerShell** — the normal Windows terminal. Used only once, to install WSL.
- **Ubuntu (WSL)** — a Linux terminal inside Windows. Used for everything else.

Whenever a command is shown below, the heading tells you which terminal to type it in.

---

### Step 0 — Install the tools (one time only)

We will use **Docker** to run Hadoop. Docker packages software into ready-to-run boxes called **containers**. This way you do not have to install Hadoop, Java, and all their settings by hand — Docker does it for you.

#### 0A) Install WSL (do this first)

**Terminal: Windows PowerShell (Admin)**

1. Right-click the Start menu → **Terminal (Admin)** (or on older Windows 10, "Windows PowerShell (Admin)"). Click **Yes** on the UAC prompt.
2. Type this and press Enter:
   ```powershell
   wsl --install
   ```
   **What this does, word by word:**
   - `wsl` → the Windows command for "Windows Subsystem for Linux".
   - `--install` → a flag telling Windows to install WSL2 *and* also install Ubuntu as the default Linux distribution.
3. Wait until it finishes. It downloads Ubuntu (~500 MB).
4. **Restart the computer when it tells you to.**
5. After reboot, open **Ubuntu** from the Start menu. On first launch, it asks you to pick a username and password — any short name works (this has nothing to do with your Windows login).

Verify WSL is installed — in **PowerShell**:
```powershell
wsl --list --verbose
```
**What this does:**
- `--list` → show all Linux distributions installed under WSL.
- `--verbose` → also show each distribution's WSL version and whether it is running.

Expected output: one line saying `Ubuntu  Stopped  2`. The **2** means WSL version 2 (the fast, correct one).

#### 0B) Install Docker Desktop

**Windows browser + installer (no terminal needed)**

1. Open this link: **https://www.docker.com/products/docker-desktop/**
2. Click **Download for Windows — AMD64** (or ARM64 if you have a Snapdragon/ARM laptop).
3. Double-click the downloaded file `Docker Desktop Installer.exe`.
4. On the first screen, make sure **"Use WSL 2 instead of Hyper-V"** is checked. Keep everything else default. Click **OK**.
5. When it finishes, click **Close and restart**.
6. After reboot, open **Docker Desktop** from the Start menu. Accept the terms.
7. Wait until the whale icon in the bottom-right Windows tray says **"Docker Desktop is running"**.
8. In Docker Desktop, click the gear icon → **Resources → WSL Integration** → turn on the switch for **Ubuntu** → click **Apply & restart**. This lets WSL talk to Docker.

#### 0C) Check that Docker works inside Ubuntu

**Terminal: Ubuntu (WSL)**

Open **Ubuntu** from the Start menu, then type:
```bash
docker --version
docker run hello-world
```

**What each command does:**
| Command | What it means |
|---|---|
| `docker --version` | Prints the version of Docker installed. Proves Docker is visible from inside Ubuntu. |
| `docker run hello-world` | Downloads a tiny official test image called `hello-world` from Docker Hub (the public library of images) and runs it. It prints a welcome message, then exits. |

Expected: you should see **"Hello from Docker!"** at the end.

If you get `permission denied` or `command not found`:
- Make sure **Docker Desktop is running** (check the system tray).
- Make sure **WSL Integration for Ubuntu** is turned on (Step 0B, point 8).
- Close the Ubuntu terminal and open it again.

---

### Step 1 — Start a tiny Hadoop cluster

**Terminal: Ubuntu (WSL)**

```bash
mkdir ~/hadoop-lab && cd ~/hadoop-lab
```
**Breakdown:**
- `mkdir` → "make directory" (create folder).
- `~/hadoop-lab` → a new folder called `hadoop-lab` inside your home folder (`~` means home).
- `&&` → "and if the previous command succeeded, run the next one".
- `cd ~/hadoop-lab` → "change directory" — enter that new folder.

```bash
nano docker-compose.yml
```
**Breakdown:**
- `nano` → a simple text editor that runs in the terminal (works like Notepad).
- `docker-compose.yml` → the filename we are creating. `.yml` = YAML, a simple format used for settings files.

A text editor opens. Paste the following exactly (the same file is in [`hadoop-lab/docker-compose.yml`](hadoop-lab/docker-compose.yml) ready to use):

```yaml
x-hadoop-env: &hadoop-env
  CORE-SITE.XML_fs.defaultFS: hdfs://namenode:9000
  CORE-SITE.XML_hadoop.http.staticuser.user: root
  HDFS-SITE.XML_dfs.replication: "1"
  HDFS-SITE.XML_dfs.namenode.rpc-address: namenode:9000
  HDFS-SITE.XML_dfs.namenode.datanode.registration.ip-hostname-check: "false"
  MAPRED-SITE.XML_mapreduce.framework.name: yarn
  MAPRED-SITE.XML_yarn.app.mapreduce.am.env: HADOOP_MAPRED_HOME=/opt/hadoop
  MAPRED-SITE.XML_mapreduce.map.env: HADOOP_MAPRED_HOME=/opt/hadoop
  MAPRED-SITE.XML_mapreduce.reduce.env: HADOOP_MAPRED_HOME=/opt/hadoop
  YARN-SITE.XML_yarn.resourcemanager.hostname: resourcemanager
  YARN-SITE.XML_yarn.nodemanager.pmem-check-enabled: "false"
  YARN-SITE.XML_yarn.nodemanager.vmem-check-enabled: "false"
  YARN-SITE.XML_yarn.nodemanager.aux-services: mapreduce_shuffle

services:
  namenode:
    image: apache/hadoop:3.3.6
    hostname: namenode
    user: root
    command: ["hdfs", "namenode"]
    ports:
      - 9870:9870
      - 9000:9000
    environment:
      <<: *hadoop-env
      ENSURE_NAMENODE_DIR: /tmp/hadoop-root/dfs/name

  datanode:
    image: apache/hadoop:3.3.6
    user: root
    command: ["hdfs", "datanode"]
    environment:
      <<: *hadoop-env
    depends_on: [namenode]

  resourcemanager:
    image: apache/hadoop:3.3.6
    hostname: resourcemanager
    user: root
    command: ["yarn", "resourcemanager"]
    ports:
      - 8088:8088
    environment:
      <<: *hadoop-env
    depends_on: [namenode]

  nodemanager:
    image: apache/hadoop:3.3.6
    user: root
    command: ["yarn", "nodemanager"]
    environment:
      <<: *hadoop-env
    depends_on: [resourcemanager]
```

> **Why the long config block?** The `apache/hadoop:3.3.6` image ships with an empty Hadoop config. Without `fs.defaultFS`, `yarn.resourcemanager.hostname`, etc. the NameNode crashes with `Invalid URI for NameNode address`. The `x-hadoop-env` anchor keeps the settings in one place and reuses them for all four services.

**What each line means:**
| Line | Meaning |
|---|---|
| `version: "3"` | Format version of this compose file. |
| `services:` | Everything below is a container we want to create. |
| `namenode:` | Name of the first container. |
| `image: apache/hadoop:3.3.6` | Use this pre-built Hadoop image (version 3.3.6) from Docker Hub. |
| `hostname: namenode` | Internal network name so other containers can find it. |
| `command: ["hdfs", "namenode"]` | What to run inside: start the HDFS NameNode process. |
| `ports: - 9870:9870` | Connect port 9870 inside the container to port 9870 on your Windows — that is how `localhost:9870` in your browser reaches it. |
| `- 9000:9000` | Same for HDFS's internal client port. |
| `environment: ENSURE_NAMENODE_DIR: ...` | An extra setting telling the image where to keep HDFS metadata. |
| `datanode:` | Second container — an HDFS DataNode. |
| `depends_on: [namenode]` | Wait for NameNode to start first. |
| `resourcemanager:` | The YARN boss. |
| `nodemanager:` | The YARN worker helper. |

Save and exit the editor:
- **Ctrl+O** → "write out" (save).
- **Enter** → confirm filename.
- **Ctrl+X** → exit nano.

Now start Hadoop:
```bash
docker compose up -d
```
**Breakdown:**
- `docker compose` → the tool that reads `docker-compose.yml` and creates all the containers together.
- `up` → create and start all services.
- `-d` → "detached" mode. Containers run in the background; the terminal stays free. Without `-d`, your screen would fill with log messages.

The first run downloads about **1.5 GB** (only once).

When it finishes, check:
```bash
docker ps
```
**Breakdown:**
- `docker ps` → "process status" — lists only the containers that are **currently running**.

You should see 4 containers: `namenode`, `datanode`, `resourcemanager`, `nodemanager`. **Your Hadoop cluster is alive.**

---

### Step 2 — Open the HDFS dashboard in your browser

**Any Windows browser (Chrome, Edge, Firefox).**

```
http://localhost:9870
```

Explore:
- Top menu → **Datanodes** → shows your worker computers (just 1 in this setup).
- Top menu → **Utilities → Browse the file system** → file explorer for HDFS.

This dashboard is the **NameNode's web face**. Whatever you do from the terminal, you can see it here too.

---

### Step 3 — Open the YARN dashboard

**Any Windows browser.**

```
http://localhost:8088
```

Right now it is empty (no jobs are running yet). Any job you submit will show up here.

---

### Step 4 — Get inside the NameNode and make a folder in HDFS

**Terminal: Ubuntu (WSL)**

```bash
docker exec -it hadoop-lab-namenode-1 bash
```
**Breakdown:**
- `docker exec` → run a command *inside a container that is already running*.
- `-i` → "interactive" — keep the input stream open so you can type.
- `-t` → give you a proper terminal (colors, tab-completion, etc.).
- `hadoop-lab-namenode-1` → the full container name. `hadoop-lab` is our folder, `namenode` is the service, `1` is the instance number.
- `bash` → the command we want to run inside the container — start a bash shell so we can type more commands.

*(If the container name is different on your machine, run `docker ps` and copy the exact name that ends with `namenode-1`.)*

Your prompt changes — now you are inside the container. Create a folder in HDFS:
```bash
hdfs dfs -mkdir /demo
hdfs dfs -ls /
```
**Breakdown:**
- `hdfs` → the Hadoop command-line program.
- `dfs` → the "distributed file system" sub-command. Everything after this talks to HDFS, **not** the local disk.
- `-mkdir /demo` → make a new HDFS folder at the root, named `demo`.
- `-ls /` → list everything at the root of HDFS.

Refresh the HDFS web UI → Browse the file system → you will see `/demo`. That is your first HDFS folder.

---

### Step 5 — Upload a file and look at its blocks

Still inside the container:
```bash
echo "the quick brown fox jumps over the lazy dog the cat sat the cat ran" > /tmp/words.txt
```
**Breakdown:**
- `echo "..."` → print text.
- `>` → redirect the output to a file instead of the screen.
- `/tmp/words.txt` → the file to create (on the container's local disk).

```bash
hdfs dfs -put /tmp/words.txt /demo/
hdfs dfs -ls /demo/
```
**Breakdown:**
- `-put` → upload a file from the container's local disk **into HDFS**.
- `/tmp/words.txt` → the source (local).
- `/demo/` → the destination (inside HDFS).
- `-ls /demo/` → list the contents of the HDFS `/demo` folder to confirm the upload worked.

Ask HDFS how it actually stored the file:
```bash
hdfs fsck /demo/words.txt -files -blocks -locations
```
**Breakdown:**
- `hdfs fsck` → "filesystem check" — a health-check tool for HDFS, like `chkdsk` on Windows but for HDFS.
- `/demo/words.txt` → the file to check.
- `-files` → show file-level information.
- `-blocks` → also show block-level details.
- `-locations` → also show which DataNode holds each block.

You will see something like:
```
/demo/words.txt ... 1 block(s): OK
0. BP-....  blk_....  len=69  Live_repl=1   [DatanodeInfo ...]
```

This is proof: the file was split into a **block**, the block has an ID, and there is one **replica** on a specific **DataNode**. Every concept from the theory section just became a real thing.

---

### Step 6 — Read the file back

```bash
hdfs dfs -cat /demo/words.txt
```
**Breakdown:**
- `-cat` → print the contents of an HDFS file to the terminal. Same idea as `cat` on Linux, but reads from HDFS instead of local disk.

---

### Step 7 — Run your first MapReduce job (word count)

Hadoop ships with example jobs ready to use. Run the built-in word count:

```bash
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
  wordcount /demo/words.txt /demo/wc_out
```
**Breakdown:**
- `hadoop jar` → run a Java program (a `.jar` file) as a Hadoop job.
- `/opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar` → full path to the example-jobs JAR that ships with Hadoop. (The `apache/hadoop:3.3.6` image does **not** set `$HADOOP_HOME`, so we use the hardcoded path.)
- `\` at end of line → "continue this command on the next line".
- `wordcount` → the name of the specific example inside the JAR (the JAR has several; we pick this one).
- `/demo/words.txt` → the input file in HDFS.
- `/demo/wc_out` → the output folder in HDFS. Important: it must **not** already exist. Hadoop refuses to overwrite.

While it runs, open **http://localhost:8088** — the job will appear in the list going through statuses **ACCEPTED → RUNNING → FINISHED**. That is YARN doing its job.

When it finishes, look at the output:
```bash
hdfs dfs -ls /demo/wc_out
hdfs dfs -cat /demo/wc_out/part-r-00000
```
**Breakdown:**
- `-ls /demo/wc_out` → list the files inside the output folder. You will see `_SUCCESS` (a marker file Hadoop writes when a job finishes cleanly) plus one or more files named `part-r-00000`.
- `-cat /demo/wc_out/part-r-00000` → print the actual results. `part-r-00000` means "output piece number 0 from reducer number 0".

You should see the word counts:
```
brown   1
cat     2
dog     1
fox     1
jumps   1
lazy    1
over    1
quick   1
ran     1
sat     1
the     4
```

That is **Map → Shuffle → Reduce** producing a real result.

---

### Step 8 — Clean up and close

Inside the container:
```bash
hdfs dfs -rm -r /demo
```
**Breakdown:**
- `-rm` → remove (delete).
- `-r` → recursive — also delete everything inside.
- `/demo` → the HDFS folder to delete.

```bash
exit
```
**Breakdown:**
- `exit` → leave the container's bash shell and return to your Ubuntu terminal.

Stop Hadoop for the day (in Ubuntu):
```bash
cd ~/hadoop-lab
docker compose down
```
**Breakdown:**
- `cd ~/hadoop-lab` → go back to the folder that has the compose file.
- `docker compose down` → stop and delete all 4 containers. Anything stored inside the containers is gone (that is why we keep data in HDFS, not in the container's local disk).

To start the cluster again later (in Ubuntu):
```bash
cd ~/hadoop-lab
docker compose up -d
```
**Breakdown:**
- Same `up -d` as before. Docker reuses the already-downloaded images, so this time the cluster starts in seconds.

