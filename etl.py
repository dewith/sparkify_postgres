import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Process JSON files and insert data in songs and artists tables 
    of the database.

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    filepath : str
        The filepath with the JSON files containing song information.
    """
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id',
                    'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location',
                      'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Process JSON files and insert data in time, users and songplays tables 
    of the database.

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    filepath : str
        The filepath with the JSON files containing song plays information.
    """
    df = pd.read_json(filepath, lines=True)¡
    df = df.loc[df.page == 'NextSong', :]

    # insert time data records
    df['ts'] = pd.to_datetime(df.ts, unit='ms')
    t = df['ts']
    time_data = {
        'start_time': t,
        'hour': t.dt.hour,
        'day': t.dt.day,
        'week': t.dt.week,
        'month': t.dt.month,
        'year': t.dt.year,
        'weekday': t.dt.weekday
    }
    time_df = pd.DataFrame(data=time_data)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # insert user records
    user_df = df.loc[:, ['userId', 'firstName', 'lastName', 'gender', 'level']]
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = {
            'songplay_id': row.registration,
            'start_time': row.ts,
            'user_id': row.userId,
            'level': row.level,
            'song_id': songid,
            'artist_id': artistid,
            'session_id': row.sessionId,
            'location': row.location,
            'user_agent': row.userAgent
        }
        cur.execute(songplay_table_insert, list(songplay_data.values()))


def process_data(cur, conn, filepath, func):
    """[summary]

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    conn : psycopg2.extensions.connection
        Handles the connection to a PostgreSQL database instance. 
    filepath : str
        Path with the JSON files containing the data to be processed.
    func : callable
        Function to process the files in filepath and isert records in the 
        connection using the cursor.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    CREDENTIALS = "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    conn = psycopg2.connect(CREDENTIALS)
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()

if __name__ == "__main__":
    main()
