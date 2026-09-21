from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("Bronze Customers")
    .getOrCreate()
)


origem = "/opt/spark/storage/E-Commerce/customers.csv"

destino = "s3a://ecommerce/bronze/customers"


df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(origem)
)


print("=== DADOS LIDOS ===")
df.show(5)


print("=== GRAVANDO BRONZE ===")

(
    df.write
    .mode("overwrite")
    .parquet(destino)
)


print("=== GRAVAÇÃO CONCLUÍDA ===")


spark.stop()