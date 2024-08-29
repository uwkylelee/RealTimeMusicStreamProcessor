FROM bitnami/spark:3.5.0

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY src/ .

# 환경 변수 설정
ENV SPARK_HOME=/opt/bitnami/spark
ENV PYSPARK_PYTHON=python3

# 애플리케이션 실행
CMD [ "spark-submit", \
"--master", "spark://spark-master:7077", \
"--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0", \
"main.py" ]
