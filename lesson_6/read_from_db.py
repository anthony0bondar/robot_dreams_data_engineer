import os

import psycopg2

pg_creds = {
    'host': '192.168.88.241'
    , 'port': '5432'
    , 'database': 'sample_db'
    , 'user': 'pguser'
    , 'password': 'secret'
}


def read_from_db():

    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        cursor.execute('SELECT * FROM sample_schema.sample_table')
        result = cursor.fetchall()
        print(result)

    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        with open(file=os.path.join('.', 'data', 'sample_table.csv'), mode='w') as csv_file:
            cursor.copy_expert('COPY sample_schema.sample_table(name, surname) TO STDOUT WITH HEADER CSV', csv_file)


def write_to_db():

    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        data = [('Vasiliy', 'Petrov'), ('Mariya', 'Voronina')]
        cursor.executemany("INSERT INTO sample_schema.sample_table (name, surname) VALUES (%s, %s)", data)

    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        with open(file=os.path.join('.', 'data', 'sample_table.csv'), mode='r') as csv_file:
            cursor.copy_expert('COPY sample_schema.sample_table(name, surname) FROM STDIN WITH HEADER CSV', csv_file)


if __name__ == '__main__':
    read_from_db()
    write_to_db()
