from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg


spark = (
    SparkSession.builder
    .appName("Analise Customers")
    .getOrCreate()
)


caminho = "/opt/spark/storage/E-Commerce/customers.csv"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(caminho)
)


print("=== QUANTIDADE DE CLIENTES ===")
print(df.count())


print("=== CLIENTES POR CIDADE ===")

(
    df.groupBy("City")
    .agg(count("*").alias("Quantidade"))
    .orderBy(col("Quantidade").desc())
    .show(10, truncate=False)
)


print("=== IDADE MÉDIA ===")

(
    df.select(
        avg("Age").alias("IdadeMedia")
    )
    .show()
)


print("=== CLIENTES POR SEGMENTO ===")

(
    df.groupBy("CustomerSegment")
    .agg(count("*").alias("Quantidade"))
    .orderBy(col("Quantidade").desc())
    .show()
)


spark.stop()