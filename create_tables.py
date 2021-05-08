import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# editar esto 
def create_database():
    """Create and connect to the sparkifydb.

    Returns
    -------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    conn : psycopg2.extensions.connection
        Handles the connection to a PostgreSQL database instance. 
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """Drop each table using the queries in `drop_table_queries` list.

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    conn : psycopg2.extensions.connection
        Handles the connection to a PostgreSQL database instance. 
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create each table using the queries in `create_table_queries` list. 

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        Allows Python code to execute PostgreSQL command in a database session.
    conn : psycopg2.extensions.connection
        Handles the connection to a PostgreSQL database instance. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Drop (if exists) and creates the sparkify database."""
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()