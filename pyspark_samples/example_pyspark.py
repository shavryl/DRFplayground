from pyspark.sql import SparkSession


spark = SparkSession\
    .builder\
    .appName("Python Spark SQL example")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()


df = spark.read.format('com.databricks.spark.csv')\
    .options(header='true', inferschema='true')\
    .load("/Home/Downloads/setup.py", header=True)

df.show(5)
df.printSchema()
