from typing import Dict

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (IntegerType, StringType, StructField, StructType,
                               TimestampType)

from database_helper.db_manager import PostgresDataManager
from database_helper.models.track_like_event_log import TrackLikeEventLog
from database_helper.models.track_stream_event_log import TrackStreamEventLog


class StreamingPipeline:
    """
    A class to process Kafka streaming data using Spark Structured Streaming.
    """

    def __init__(self, kafka_config: Dict[str, str],
                 db_manager: PostgresDataManager):
        """
        Initialize the streaming pipeline.

        :param kafka_config: A dictionary containing
        Kafka connection parameters.
        :param db_manager: An instance of PostgresDataManager
        for database operations.
        """
        self.spark = SparkSession.builder \
            .appName("UnifiedStreamingPipeline") \
            .getOrCreate()
        self.spark.conf.set("spark.sql.streaming.minBatchesToRetain", 10)
        self.spark.conf.set("spark.streaming.kafka.maxOffsetsPerTrigger", 1000)
        self.kafka_config = kafka_config
        self.db_manager = db_manager

        # Define schemas for different log types
        self.streaming_schema = StructType([
            StructField("user_id", IntegerType(), True),
            StructField("track_id", IntegerType(), True),
            StructField("event_timestamp", TimestampType(), True),
            StructField("event_type", StringType(), True),
        ])

        self.like_schema = StructType([
            StructField("user_id", IntegerType(), True),
            StructField("track_id", IntegerType(), True),
            StructField("event_timestamp", TimestampType(), True),
            StructField("event_type", StringType(), True),
        ])

    def process_stream(self, topic: str) -> None:
        """
        Process streaming data from the specified Kafka topic.

        :param topic: Kafka topic name.
        """
        kafka_df = self.spark \
            .readStream.format("kafka") \
            .option("kafka.bootstrap.servers",
                    self.kafka_config['bootstrap_servers']) \
            .option("subscribe", topic) \
            .option("kafka.group.id", "pipeline_group") \
            .load()

        # Parse Kafka data into structured data with dynamic schema
        parsed_df = kafka_df.selectExpr(
            "CAST(value AS STRING) as json_data").select(
            from_json(col("json_data"), self.streaming_schema).alias(
                "streaming_data"),
            from_json(col("json_data"), self.like_schema).alias("like_data"),
        )

        # Separate streaming and like data
        streaming_df = (
            parsed_df.select("streaming_data.*")
            .filter(col("streaming_data.event_type") == "streaming")
            .drop("event_type")
        )
        like_df = (
            parsed_df.select("like_data.*")
            .filter(col("like_data.event_type") == "like")
            .drop("event_type")
        )

        # Process each type of log
        streaming_df.writeStream.foreachBatch(
            self._process_streaming).outputMode("append").start()

        like_df.writeStream.foreachBatch(
            self._process_like).outputMode("append").start()

        # Await termination of streams
        self.spark.streams.awaitAnyTermination()

    def _process_streaming(self, batch_df, batch_id):
        """
        Process streaming logs and save to `track_stream_log`.

        :param batch_df: DataFrame containing streaming logs.
        :param batch_id: Batch ID for the streaming data.
        """
        try:
            records = batch_df.collect()
            data = [record.asDict() for record in records]
            self.db_manager.insert(TrackStreamEventLog, data)
            print(
                f"Processed {len(data)} streaming records into `track_stream_log`.")
        except Exception as e:
            print(f"Error processing batch {batch_id}: {e}")

    def _process_like(self, batch_df, batch_id):
        """
        Process like logs and save to `track_like_log`.

        :param batch_df: DataFrame containing like logs.
        :param batch_id: Batch ID for the like data.
        """
        try:
            records = batch_df.collect()
            data = [record.asDict() for record in records]
            self.db_manager.insert(TrackLikeEventLog, data)
            print(f"Processed {len(data)} like records into `track_like_log`.")
        except Exception as e:
            print(f"Error processing batch {batch_id}: {e}")
