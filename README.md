# Real-time Music Streaming Data Processor & Music Recommendation System

## Table of Contents

- [Introduction](#introduction)
    - [Data Generation](#data-generation)
        - [Source of Track Data](#source-of-track-data)
    - [Data Processing](#data-processing)
- [Development Requirements](#development-requirements)
    - [Local Development](#local-development)
    - [GCP Deployment](#gcp-deployment)
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

### Data Generation

The data generation component simulates live music stream data and sends it to Kafka topics. This is achieved through a
Kafka producer that generates synthetic music stream data, mimicking real-world scenarios.

The source of track data is a Kaggle dataset containing information about various tracks, including their metadata and
audio features. Link to the dataset is provided below.

#### Source of Track Data

[Kaggle Spotify Tracks Dataset](
https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
)

### Data Processing

Data processing is handled by Apache Spark, which consumes data from Kafka topics, processes it, and prepares it for the
recommendation system. Spark's structured streaming capabilities enable efficient handling of real-time data streams.

## Development Requirements

### Local Development

For local development, the following components are required:

- Docker
- Docker Compose
- Python 3.10
- Miniconda or Anaconda

### GCP Deployment

For deployment to Google Cloud Platform, the following components are required:

- Google Cloud SDK
- GitHub Actions

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
- [Google Cloud Platform Documentation](https://cloud.google.com/docs)
- [Anaconda Documentation](https://docs.anaconda.com/)