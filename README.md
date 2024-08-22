# Music Streaming Data Processing & Recommendation System

Repository for practicing large-scale data processing and recommendation system with fake music streaming data.

## Table of Contents

- [Introduction](#introduction)
- [Data Generation](#data-generation)
- [Data Processing](#data-processing)
- [Recommendation System](#recommendation-system)
- [References](#references)

## Introduction

This repository is for practicing large-scale data processing and recommendation system with fake music streaming data.
The data is generated using the `Faker` library in Python. The data processing is done using `Apache Kafka`
and `PySpark` and the recommendation system is built using `PySpark` and `Spark MLlib`.

### Development Environment

- Python 3.10
- Apache Kafka 3.0.0
- Java 17

## Run DB

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

## Run Kafka


### Start Kafka Instance
```shell
docker-compose -f kafka/docker-compose.yml up -d --build
```

### Stop Kafka Instance
```shell
docker-compose -f kafka/docker-compose.yml down
```


## Run Spark

### Start Spark Instance
```shell
docker-compose -f spark/docker-compose.yml up -d --build
```

### Stop Spark Instance
```shell
docker-compose -f spark/docker-compose.yml down
```

## Recommendation System

## References
