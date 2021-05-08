# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id   VARCHAR,
        name        VARCHAR NOT NULL,
        location    TEXT,
        latitude    DECIMAL,
        longitude   DECIMAL,
        PRIMARY KEY (artist_id)
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id     VARCHAR,
        title       VARCHAR NOT NULL,
        artist_id   VARCHAR NOT NULL REFERENCES artists(artist_id),
        year        INT NOT NULL,
        duration    NUMERIC NOT NULL,
        PRIMARY KEY (song_id)
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time  TIMESTAMP,
        hour        INT NOT NULL,
        day         INT NOT NULL,
        week        INT NOT NULL,
        month       INT NOT NULL,
        year        INT NOT NULL,
        weekday     INT NOT NULL,
        PRIMARY KEY (start_time)
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id     BIGINT ,
        first_name  VARCHAR NOT NULL,
        last_name   VARCHAR,
        gender      VARCHAR,
        level       VARCHAR NOT NULL,
        PRIMARY KEY (user_id)
    )
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL UNIQUE,
        start_time  TIMESTAMP NOT NULL REFERENCES time(start_time),
        user_id     BIGINT NOT NULL REFERENCES users(user_id),
        level       VARCHAR NOT NULL,
        song_id     VARCHAR REFERENCES songs(song_id),
        artist_id   VARCHAR REFERENCES artists(artist_id),
        session_id  VARCHAR NOT NULL,
        location    TEXT,
        user_agent  TEXT,
        PRIMARY KEY (songplay_id)
    )
""")


# INSERT RECORDS
songplay_table_insert = ("""
    INSERT INTO songplays  (songplay_id, start_time, user_id,
                            level, song_id, artist_id,
                            session_id, location, user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        gender = EXCLUDED.gender,
        level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO UPDATE SET
        location = EXCLUDED.location,
        latitude = EXCLUDED.latitude,
        longitude = EXCLUDED.longitude;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")


# FIND SONGS
song_select = ("""
    SELECT s.song_id, s.artist_id
    FROM songs AS s
    JOIN artists AS a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")


# QUERY LISTS
create_table_queries = [artist_table_create, song_table_create, time_table_create,
                        user_table_create, songplay_table_create]
drop_table_queries = [artist_table_drop, song_table_drop, time_table_drop,
                      user_table_drop, songplay_table_drop]
