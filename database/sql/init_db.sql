CREATE TABLE IF NOT EXISTS bulk_track_raw_data
(
    track_id         TEXT,
    artists          TEXT,
    album_name       TEXT,
    track_name       TEXT,
    popularity       BIGINT,
    duration_ms      BIGINT,
    explicit         BOOLEAN,
    danceability     double precision,
    energy           double precision,
    key              BIGINT,
    loudness         double precision,
    mode             BIGINT,
    speechiness      double precision,
    acousticness     double precision,
    instrumentalness double precision,
    liveness         double precision,
    valence          double precision,
    tempo            double precision,
    time_signature   BIGINT,
    track_genre      TEXT
);

COPY bulk_track_raw_data FROM '/data/bulk_track_raw_data.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE IF NOT EXISTS users
(
    user_id    INT PRIMARY KEY,
    user_name  TEXT,
    user_email TEXT
);

-- CREATE TABLE IF NOT EXISTS artists (
--     artist_id INT PRIMARY KEY,
--     artist_name TEXT
-- );

CREATE TABLE IF NOT EXISTS artists AS
SELECT ROW_NUMBER() OVER (ORDER BY artist_name) AS artist_id,
       artist_name
FROM (SELECT DISTINCT unnest(regexp_split_to_array(artists, ';')) AS artist_name
      FROM bulk_track_raw_data) AS unique_artists;

-- CREATE TABLE IF NOT EXISTS albums (
--     album_id INT PRIMARY KEY,
--     album_name TEXT
-- );

CREATE TABLE IF NOT EXISTS albums AS
SELECT ROW_NUMBER() OVER (ORDER BY album_name) AS album_id,
       album_name
FROM (SELECT DISTINCT album_name
      FROM bulk_track_raw_data
      WHERE album_name IS NOT NULL) AS unique_albums;


-- CREATE TABLE IF NOT EXISTS tracks
-- (
--     track_id        INT PRIMARY KEY,
--     track_name      TEXT,
--     artist_id_array INT[],
--     album_id        INT,
--     genre           TEXT,
--     popularity      BIGINT,
--     duration_ms     INT
-- );

CREATE TABLE IF NOT EXISTS tracks AS
SELECT ROW_NUMBER() OVER (ORDER BY track_name) AS track_id,
       btrd.track_name,
       ARRAY(
               SELECT artist_id
               FROM artists
               WHERE artist_name = ANY (regexp_split_to_array(btrd.artists, ';'))
           )                                   AS artist_id_array,
       a.album_id,
       btrd.track_genre                        AS genre,
       btrd.popularity,
       btrd.duration_ms
FROM bulk_track_raw_data AS btrd
         JOIN albums AS a
              ON btrd.album_name = a.album_name;

CREATE TABLE IF NOT EXISTS track_stream_log
(
    user_id           INT,
    track_id          INT,
    created_timestamp TIMESTAMP,
    PRIMARY KEY (user_id, track_id)
);

CREATE TABLE IF NOT EXISTS track_like_log
(
    user_id           INT,
    track_id          INT,
    created_timestamp TIMESTAMP,
    PRIMARY KEY (user_id, track_id)
);