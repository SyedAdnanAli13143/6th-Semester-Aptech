from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, round, sum as _sum

spark = (
    SparkSession.builder
    .appName("SparkFromMongo")
    .config("spark.mongodb.read.connection.uri",  "mongodb://mongo-lab:27017/school.students")
    .config("spark.mongodb.write.connection.uri", "mongodb://mongo-lab:27017/school.students")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

df = spark.read.format("mongodb").load()

print("=== Raw documents from MongoDB ===")
df.select("student_id", "name", "course", "score", "passed").show()

print("=== Average score per student (Spark on Mongo data) ===")
(
    df.groupBy("student_id")
      .agg(round(avg("score"), 2).alias("avg_score"))
      .orderBy("student_id")
      .show()
)

print("=== Pass count per course ===")
(
    df.groupBy("course")
      .agg(_sum("passed").alias("students_passed"))
      .orderBy("course")
      .show()
)

spark.stop()
