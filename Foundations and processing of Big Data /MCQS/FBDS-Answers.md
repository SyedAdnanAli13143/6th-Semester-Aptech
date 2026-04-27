# FBDS — All Questions with Correct Answers & Easy Explanations

(Compiled from FBDS-1, FBDS-2, FBDS-3, FBDS-4, FBDS-5. Duplicates removed.)

---

## 1. _______ is a framework that allows distributed processing of large datasets across clusters of computers using simple programming models.
**Correct Answer: A) Hadoop**

**Why:** Hadoop is the actual software framework that splits big data and processes it on many computers at once.
**Real-life example:** Imagine you have to count every grain of rice in a huge truck. Alone it would take days. If you call 100 friends and each counts one bag, you finish in minutes. Hadoop is the "manager" that gives one bag to each friend and then collects the totals.

---

## 2. When a file is split into blocks, the default size of each file block is ____.
**Correct Answer: C) 128 MB**

**Why:** Hadoop (HDFS) chops big files into 128 MB pieces by default so it can store them on different machines.
**Real-life example:** Think of a long pizza that won't fit in one box. You cut it into equal slices of 128 MB so each slice fits in a small box (DataNode) and can be carried separately.

---

## 3. Creating copies of a block in multiple DataNodes is called ________.
**Correct Answer: B) Block Replication**

**Why:** HDFS keeps 3 copies of each block on different machines so data is never lost if one machine fails.
**Real-life example:** Like saving your important photos on your phone, laptop, AND Google Drive. If your phone breaks, the photos are still safe on the other two places.

---

## 4. A ______ is a map-side join where every single record is paired up from another dataset.
**Correct Answer: C) Cartesian product**

**Why:** A Cartesian product join pairs every record of one dataset with every record of another — no key matching, just full pairing.
**Real-life example:** Imagine 5 shirts and 4 pants. To check every possible outfit, you pair every shirt with every pant = 20 outfits. That "every-with-every" pairing is a Cartesian product.

---

## 5. Which of the following statements is NOT a characteristic of MapReduce?
**Correct Answer: C) Handles small-scale data**

**Why:** MapReduce is designed specifically for huge data (terabytes/petabytes), not small data. Using it for small data is overkill.
**Real-life example:** MapReduce is like a giant industrial truck — perfect for moving a whole house's furniture, but useless if you just want to carry one bag of groceries.

---

## 6. When a table is created in Hive, data is stored as text with ____ comma-separated fields per line.
**Correct Answer: C) Three**

**Why:** Hive's default text storage uses 3 comma-separated fields per row.
**Real-life example:** Like a class attendance sheet with three columns: Roll No, Name, Status. Each line: `1, Adnan, Present`.

---

## 7. Which of the following is NOT a primitive data type in Hive?
**Correct Answer: A) ARRAY**

**Why:** BOOLEAN, FLOAT, DOUBLE are simple/primitive types. ARRAY is a complex (collection) type because it holds many values.
**Real-life example:** A primitive type is like a single coin. ARRAY is like a wallet that holds many coins — it's a collection, not a single value.

---

## 8. ____ is a command-line interface application for transferring data between relational databases and Hadoop.
**Correct Answer: B) SQOOP**

**Why:** "SQOOP" = SQL-to-Hadoop. It moves data from MySQL/Oracle into Hadoop and vice versa.
**Real-life example:** SQOOP is like a courier service (FedEx) that picks up parcels from your old office (MySQL) and delivers them to your new warehouse (Hadoop).

---

## 9. What action does the 'Impala-shell -q "select * from simple"' command perform?
**Correct Answer: A) Runs direct queries from shell using the -q option**

**Why:** The `-q` flag tells Impala to run the query you typed right after it, without entering interactive mode.
**Real-life example:** Like sending a quick text "what's the time?" instead of calling someone and chatting. `-q` = "just answer this one thing and exit."

---

## 10. The character "____" is used to execute Beeline commands.
**Correct Answer: D) !**

**Why:** In Beeline, special commands start with `!` (e.g., `!connect`, `!quit`).
**Real-life example:** Like pressing the "*" key on a phone menu to access special options. `!` is Beeline's special-command key.

---

## 11. Which of the following features does Hive NOT include?
**Correct Answer: C) Used mainly for interactive queries and data analysis**

**Why:** Hive is built for **batch processing** of huge data. Quick interactive queries are Impala's job, not Hive's.
**Real-life example:** Hive is like a slow oven that bakes a big cake overnight. If you want quick microwaved popcorn, use Impala instead.

---

## 12. Which of the following is NOT part of the query execution process in Impala?
**Correct Answer: B) Process data using MapReduce or Apache Spark**

**Why:** Impala does NOT use MapReduce or Spark — that's its big advantage. It runs queries directly with its own engine, which is why it's fast.
**Real-life example:** Hive uses MapReduce (like cooking on a slow wood stove). Impala has its own gas burner — same kitchen, faster cooking.

---

## 13. By 2020, the amount of new information created for each human being will be _____.
**Correct Answer: B) 1.7 MB**

**Why:** Industry research said every person on Earth generates about 1.7 MB of new data **every second** by 2020.
**Real-life example:** Every selfie, WhatsApp message, Google search, Instagram scroll — all that adds up to 1.7 MB per person per second.

---

## 14. Using multiple machines to execute a job is called _____.
**Correct Answer: D) Distributed systems**

**Why:** When work is spread across many computers connected together, it's called a distributed system.
**Real-life example:** A team of 10 cleaners cleaning different rooms of a hotel at the same time = distributed cleaning. One cleaner alone = sequential.

---

## 15. How long does it take for one machine to process 1 Terabyte of data?
**Correct Answer: C) 45 minutes**

**Why:** A single hard disk reads ~100 MB/sec, so 1 TB takes around 45 minutes just to read — that's why we need many machines together.
**Real-life example:** One person filling a swimming pool with a garden hose takes 45 min. 10 hoses together fill it in under 5 min — same idea behind Hadoop's distributed power.

---

## 16. What action does the command line `$hdfs dfs -ls` perform?
**Correct Answer: D) Gets a directory listing of user's home directory in HDFS**

**Why:** `-ls` is the "list" command in HDFS, just like `ls` in Linux. Without a path, it shows your home folder contents.
**Real-life example:** Like opening "My Documents" on Windows to see what files are inside.

---

## 17. MapReduce was introduced by _______.
**Correct Answer: B) Google**

**Why:** Google researchers Jeffrey Dean and Sanjay Ghemawat published the original MapReduce paper in 2004.
**Real-life example:** Just like Apple invented the iPhone and others copied the idea, Google invented MapReduce and Hadoop is the open-source copy.

---

## 18. Which of the following is NOT a real-time use of MapReduce?
**Correct Answer: B) Gaussian Analysis**

**Why:** MapReduce is used in algorithms, data transfer, and enterprise analytics. Gaussian Analysis is a statistical/mathematical method, not a typical MapReduce real-world use case.
**Real-life example:** MapReduce is like a delivery truck — perfect for moving boxes (data), not for advanced statistics that need precision math tools.

---

## 19. The MapReduce responsibilities of a developer does NOT include _______.
**Correct Answer: B) Distributing the job**

**Why:** The Hadoop framework itself distributes the job to nodes automatically. The developer only writes the logic and points to the input/output.
**Real-life example:** You order food from Swiggy. You only choose what to eat (logic) — Swiggy decides which delivery boy goes where (distribution). You don't manage that.

---

## 20. ________ is a Hadoop feature that helps cache files needed by applications.
**Correct Answer: A) Distributed Cache**

**Why:** Distributed Cache copies small required files (like lookup tables, jars) to every node so jobs run faster without fetching repeatedly.
**Real-life example:** Like giving every student in a class their own copy of the textbook instead of making them line up at one library copy.

---

## 21. Which of the following access mechanisms does HDFS NOT provide?
**Correct Answer: D) C**

**Why:** HDFS provides Java API, Python (via libraries), and a Web GUI. There's no native C interface.
**Real-life example:** Like a hotel that offers room service in English, Hindi, and via a self-service app — but not in French. C is the missing language for HDFS.

---

## 22. By default, all data in the data warehouse directory structure is stored in _____.
**Correct Answer: C) /user/hive/warehouse**

**Why:** Hive uses this exact path on HDFS as the default warehouse location for tables.
**Real-life example:** Just like Windows installs programs into "C:\Program Files" by default, Hive stores all tables in `/user/hive/warehouse` by default.

---

## 23. While validating data, missing data is represented as ______.
**Correct Answer: C) NULL**

**Why:** In databases (SQL, Hive, Impala), missing or unknown values are stored as NULL — not zero, because zero is a real number.
**Real-life example:** If a student didn't appear for a test, their mark is "NULL" (no info). Writing "0" would wrongly say they got zero marks.

---

## 24. Hive was developed by _____.
**Correct Answer: D) Facebook**

**Why:** Facebook engineers built Hive to handle their massive growing data using SQL-like queries on Hadoop.
**Real-life example:** Just like Twitter built Bootstrap and shared it with the world, Facebook built Hive and gave it to the open-source community.

---

## 25. All SQL commands are terminated with a ______.
**Correct Answer: B) ;**

**Why:** Every SQL statement ends with a semicolon `;` to tell the engine "I'm done with this command, run it now."
**Real-life example:** Like a full stop at the end of a sentence. Without `;`, the system thinks you're still typing more.

---

## 26. Which of the following statements about Impala is NOT TRUE?
**Correct Answer: C) It is commonly used to analyze social media coverage**

**Why:** Impala is built for **structured** data (tables with rows/columns). Social media data (tweets, comments, images) is unstructured — that's not Impala's strength.
**Real-life example:** Impala is like a calculator made for numeric receipts. Trying to use it on a messy diary full of stories and pictures won't work well.

---

## 27. The first step to start Impala in lab is ____.
**Correct Answer: B) Log in to cloud lab Web console**

**Why:** Before you can use Impala, you must first access the lab environment by logging in to the cloud web console.
**Real-life example:** Before you start your car, you need the key. Before using Impala, you need to log in — that's the "key" step.

---

# Quick Answer Key (for fast revision)

| Q | Answer |
|---|--------|
| 1. Distributed-processing framework | A) Hadoop |
| 2. Default block size | C) 128 MB |
| 3. Copies of blocks | B) Block Replication |
| 4. Map-side join, every record paired | C) Cartesian product |
| 5. NOT MapReduce characteristic | C) Handles small-scale data |
| 6. Hive comma-separated fields | C) Three |
| 7. NOT primitive in Hive | A) ARRAY |
| 8. CLI for RDBMS↔Hadoop | B) SQOOP |
| 9. Impala-shell -q | A) Runs direct queries (-q) |
| 10. Beeline command character | D) ! |
| 11. NOT a Hive feature | C) Mainly interactive queries |
| 12. NOT in Impala execution | B) Uses MapReduce/Spark |
| 13. New info per human (2020) | B) 1.7 MB |
| 14. Multiple machines for a job | D) Distributed systems |
| 15. 1 TB processing time | C) 45 minutes |
| 16. `hdfs dfs -ls` | D) Lists user's home in HDFS |
| 17. MapReduce introduced by | B) Google |
| 18. NOT real-time use of MR | B) Gaussian Analysis |
| 19. NOT a dev responsibility | B) Distributing the job |
| 20. Hadoop file caching feature | A) Distributed Cache |
| 21. HDFS does NOT support | D) C |
| 22. Default warehouse path | C) /user/hive/warehouse |
| 23. Missing data represented as | C) NULL |
| 24. Hive developed by | D) Facebook |
| 25. SQL terminator | B) ; |
| 26. NOT TRUE about Impala | C) Used for social media analysis |
| 27. First step to start Impala | B) Log in to cloud lab Web console |
