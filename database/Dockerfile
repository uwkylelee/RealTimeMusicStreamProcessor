FROM postgres:13

# Copy raw data
COPY data/ data/

# Copy initialization script
COPY sql/init_db.sql /docker-entrypoint-initdb.d/