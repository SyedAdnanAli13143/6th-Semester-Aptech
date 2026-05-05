from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, round

spark = (
    SparkSession.builder
    .appName("SparkToMongo")
    .config("spark.mongodb.read.connection.uri",  "mongodb://mongo-lab:27017/school.students")
    .config("spark.mongodb.write.connection.uri", "mongodb://mongo-lab:27017/school.student_averages")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

df = spark.read.format("mongodb").load()

result = (
    df.groupBy("student_id")
      .agg(round(avg("score"), 2).alias("avg_score"))
      .orderBy("student_id")
)

print("=== Computed averages (will be written to Mongo) ===")
result.show()

(
    result.write
          .format("mongodb")
          .mode("overwrite")
          .save()
)

print(">>> Wrote results to MongoDB collection 'school.student_averages'")
spark.stop()
