# E-commerce Data Engineering Lab

Projeto de estudo e portfólio desenvolvido para praticar conceitos fundamentais de Engenharia de Dados utilizando um ambiente local baseado em Docker.

A proposta é reproduzir uma arquitetura simplificada de processamento de dados utilizando **Apache Spark**, **MinIO como Data Lake compatível com S3**, **Jupyter Lab**, **PostgreSQL** e **Docker Compose**.

O projeto foi construído localmente para permitir a execução e exploração dos dados sem depender de serviços cloud pagos.

## Arquitetura

```text
                         ┌─────────────────┐
                         │   CSVs / RAW    │
                         │                 │
                         │ customers.csv   │
                         │ orders.csv      │
                         │ payments.csv    │
                         │ products.csv    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      MinIO      │
                         │   Data Lake     │
                         │      S3 API     │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │      Apache Spark        │
                    │                          │
                    │  Spark Master + Workers  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                         ┌─────────────────┐
                         │     Jupyter     │
                         │      Lab        │
                         │                 │
                         │   PySpark       │
                         └─────────────────┘
```

O projeto utiliza os dados em sua camada **RAW**, permitindo que os notebooks sejam utilizados para exploração, análise e prática com PySpark.

## Tecnologias

* Python
* PySpark
* Apache Spark 3.5
* Docker
* Docker Compose
* MinIO
* Jupyter Lab
* PostgreSQL
* Delta Lake
* Hadoop AWS / S3A
* Git / GitHub

## Componentes

### Apache Spark

O ambiente possui:

* 1 Spark Master
* 3 Spark Workers
* Spark History Server

Os workers foram configurados com recursos reduzidos para permitir a execução do ambiente em um computador pessoal.

### MinIO

O MinIO funciona como um armazenamento de objetos compatível com a API S3.

Estrutura utilizada:

```text
ecommerce/
└── raw/
    ├── customers.csv
    ├── orders.csv
    ├── payments.csv
    └── products.csv
```

### Jupyter Lab

O Jupyter Lab é executado dentro de um container Docker e fornece o ambiente para desenvolvimento dos notebooks PySpark.

### PostgreSQL

O PostgreSQL está disponível no ambiente como banco relacional para estudos e futuras integrações com Spark.

## Estrutura do projeto

```text
EstudosSpark/
│
├── build/
│   ├── docker-compose.yml
│   ├── Dockerfile.spark
│   ├── Dockerfile.history
│   ├── requirements.txt
│   └── config/
│       ├── history/
│       └── spark/
│           └── jars/
│
├── jobs/
│   ├── 01_teste_cluster.py
│   ├── 02_leitura_ecommerce.py
│   ├── 03_analise_customers.py
│   └── 04_bronze_customers.py
│
├── resources/
│   └── notebooks/
│       ├── *.ipynb
│       └── Anotações/
│           └── *.md
│
├── storage/
│   └── E-Commerce/
│       ├── customers.csv
│       ├── orders.csv
│       ├── payments.csv
│       └── products.csv
│
├── metrics/
│
├── .gitignore
└── README.md
```

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/ArthurrAlmeida/EstudosSpark.git
cd EstudosSpark/build
```

### 2. Configurar as variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Os caminhos devem apontar para as pastas do projeto no computador local.

### 3. Subir o ambiente

```bash
docker compose up -d
```

Verifique os containers:

```bash
docker compose ps
```

Todos os principais serviços devem estar com status `Up`.

### 4. Acessar os serviços

#### Jupyter Lab

```text
http://localhost:8888
```

#### MinIO

```text
http://localhost:9001
```

#### Spark Master

```text
http://localhost:8080
```

#### Spark History Server

```text
http://localhost:18080
```

### 5. Parar o ambiente

```bash
docker compose down
```

> Evite utilizar `docker compose down -v`, pois o parâmetro `-v` remove os volumes persistentes utilizados pelo projeto.

## Dados

O projeto utiliza quatro conjuntos de dados:

### Customers

Informações dos clientes.

```text
CustomerID
Age
City
SignupDate
CustomerSegment
```

### Orders

Informações dos pedidos.

```text
OrderID
CustomerID
OrderDate
ProductID
Quantity
Discount
PaymentMethod
Status
```

### Payments

Informações dos pagamentos.

```text
PaymentID
OrderID
PaymentDate
PaymentStatus
```

### Products

Informações dos produtos.

```text
ProductID
ProductName
Category
UnitPrice
```

## Conceitos praticados

Durante o desenvolvimento do projeto foram praticados conceitos fundamentais de Engenharia de Dados, incluindo:

* Docker e containers
* Docker Compose
* Redes entre containers
* Variáveis de ambiente
* Dockerfiles
* Apache Spark
* Spark Master e Workers
* Driver e Executors
* DataFrames
* Transformations
* Actions
* Lazy Evaluation
* Partições
* Shuffle
* `groupBy`
* Agregações
* Leitura de arquivos CSV
* Schema e `inferSchema`
* Armazenamento S3
* S3A
* MinIO
* Data Lake
* Jupyter Lab
* PySpark
* Spark History Server

## Exemplos de operações Spark

Um dos primeiros testes realizados no projeto foi a criação de um DataFrame diretamente no Spark:

```python
dados = [
    ("Arthur", 24),
    ("João", 30),
    ("Maria", 28),
    ("Pedro", 35),
    ("Ana", 22),
    ("Lucas", 40)
]

df = spark.createDataFrame(
    dados,
    ["nome", "idade"]
)

df.show()
```

Também foram realizados testes de agregação:

```python
df.groupBy().avg("idade").show()
```

E leitura dos dados de e-commerce:

```python
df_customers = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/opt/spark/storage/E-Commerce/customers.csv")
)
```

## Objetivo do projeto

O objetivo principal deste projeto foi construir e compreender um ambiente local de Engenharia de Dados, permitindo praticar Spark e conceitos relacionados sem depender de infraestrutura cloud.

O projeto também serve como base para estudos futuros envolvendo:

* pipelines de dados;
* processamento incremental;
* orquestração;
* modelagem de dados;
* armazenamento em formatos colunares;
* integração com serviços cloud;
* arquiteturas Lakehouse.

## Autor

**Arthur Veiga**

Projeto desenvolvido como parte dos estudos práticos em Engenharia de Dados.

---

**Stack principal:** Python | PySpark | Apache Spark | Docker | MinIO | Jupyter | PostgreSQL
