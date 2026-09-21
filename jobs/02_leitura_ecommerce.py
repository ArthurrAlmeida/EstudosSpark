from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("Leitura E-commerce")
    .getOrCreate()
)


caminho = "/opt/spark/storage/E-Commerce/customers.csv"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(caminho)
)


print("=== SCHEMA ===")
df.printSchema()

print("=== QUANTIDADE DE REGISTROS ===")
print(df.count())

print("=== PRIMEIROS REGISTROS ===")
df.show(10, truncate=False)


spark.stop()