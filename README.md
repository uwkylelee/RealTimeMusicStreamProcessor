# Real-time Music Streaming Data Processor & Music Recommendation System

## Table of Contents

- [Introduction](#introduction)
- [Development Requirements](#development-requirements)
- [Data Generation](#data-generation)
- [Data Processing](#data-processing)
- [GitHub Actions CI/CD](#github-actions-cicd)
- [Helpful Commands](#helpful-commands)
- [References](#references)

## Introduction

This repository serves as a comprehensive practice environment for large-scale data processing and building a
recommendation system using simulated music streaming data. The data is synthetically generated using the `Faker`
library in Python, which mimics realistic user interactions and streaming behaviors.

The system leverages **Apache Kafka** for real-time data ingestion and streaming, ensuring efficient handling of
high-throughput data pipelines. For processing this data, **PySpark** provides a robust distributed
computing framework. The data is processed in real-time using Spark's structured streaming capabilities, which
facilitates the generation of music recommendations based on user preferences and streaming history. The processed data
is stored in a **PostgreSQL** database, which serves as the data warehouse for the streaming data.

The project is deployed to **Google Cloud Platform (GCP)** through **Google Kubernetes Engine (GKE)**. The deployment
process involves containerizing the components using **Docker** and deploying them to GKE using **Kubernetes**. The
deployment is automated using **GitHub Actions** CI/CD pipelines, which ensure that the latest changes are deployed
automatically to the GKE cluster.

## Development Requirements

- Docker
- Docker Compose
- Python 3.10

## Data Generation

The data generation component simulates live music stream data and sends it to Kafka topics. This is achieved through a
Kafka producer that generates synthetic music stream data, mimicking real-world scenarios.

## Data Processing

Data processing is handled by Apache Spark, which consumes data from Kafka topics, processes it, and prepares it for the
recommendation system. Spark's structured streaming capabilities enable efficient handling of real-time data streams.

## Helpful Commands

<details>
<summary>PSQL DB Commands</summary>

### Start DB Instance

```shell
docker-compose -f database/docker-compose.yml up -d --build
```

### Stop

```shell
docker-compose -f database/docker-compose.yml down
```

### Remove DB

```shell
docker rm musicDB
```

### Database Connection in Docker Container

```shell
psql -U pyspark -d music_db
```

</details>

<details>
<summary>Kafka  Commands</summary>

### Start Kafka Instance

```shell
docker-compose -f kafka/docker-compose.yml up -d --build
```

### Stop Kafka Instance

```shell
docker-compose -f kafka/docker-compose.yml down
```

</details>

<details>
<summary>Spark  Commands</summary>

### Start Spark Instance

```shell
docker-compose -f spark/docker-compose.yml up -d --build
```

### Stop Spark Instance

```shell
docker-compose -f spark/docker-compose.yml down
```

</details>

## References

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [Docker Documentation](https://docs.docker.com/)