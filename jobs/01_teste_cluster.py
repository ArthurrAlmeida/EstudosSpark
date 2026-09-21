from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Teste Cluster E-commerce")
    .getOrCreate()
)

print("=== TESTE DO CLUSTER SPARK ===")
print(f"Spark Version: {spark.version}")
print(f"Master: {spark.sparkContext.master}")

dados = [
    ("Arthur", 24),
    ("João", 30),
    ("Maria", 28),
    ("Pedro", 35),
    ("Ana", 22),
    ("Lucas", 40)
]

df = spark.createDataFrame(dados, ["nome", "idade"])

print("=== DADOS ===")
df.show()

print("=== PARTIÇÕES ===")
print(f"Número de partições: {df.rdd.getNumPartitions()}")

print("=== RESULTADO ===")
df.groupBy().avg("idade").show()

spark.stop()