# Real-Time Music Streaming Data Processor

### 🚀 Tech Stack

#### 🖥️ Languages
<div style="display: flex; gap: 10px; align-items: center;">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/SQL-4169E1?style=flat&logo=postgresql&logoColor=white" height="20">
</div>

#### 🛠️ Frameworks & Libraries
<div style="display: flex; gap: 10px; align-items: center;">
  <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat&logo=apachekafka&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/BigQuery-669DF6?style=flat&logo=googlebigquery&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" height="20">
</div>

#### ☁️ Cloud & Tools
<div style="display: flex; gap: 10px; align-items: center;">
  <img src="https://img.shields.io/badge/Google_Cloud_Platform-4285F4?style=flat&logo=googlecloud&logoColor=white" height="20">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white" height="20">
</div>


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
is stored in a **BigQuery**, which serves as the data warehouse for the streaming data.

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

## Development Requirements

### Local Development

For local development, the following components are required:

- Docker
- Docker Compose
- Python 3.10
- Miniconda or Anaconda

#### Setup

Install the required Python packages using the following command:

```shell
pip install -r requirements.txt
```

#### Linting before Commit

All code changes should be linted using `black` before committing. To lint the code, run the following commands:

```shell
black .
flake8 .
```

The output of above commands should be empty, indicating that the code is linted and ready for commit.

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
