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
