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
