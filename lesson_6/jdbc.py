import psycopg2

pg_creds = {
    'host': '192.168.88.102',
    'port': '5432',
    'database': 'demo',
    'user': 'pguser',
    'password': 'secret'
}


def read_jdbc():
    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        with open('sample.csv', 'w') as csv_file:
            cursor.copy_expert('COPY (select * from test2 where id < 3) TO STDOUT WITH HEADER CSV', csv_file)


def write_jdbc():
    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        with open('sample.csv', 'r') as csv_file:
            cursor.copy_expert('COPY test2 FROM STDIN WITH HEADER CSV', csv_file)


if __name__ == '__main__':
    read_jdbc()
    #write_jdbc()
