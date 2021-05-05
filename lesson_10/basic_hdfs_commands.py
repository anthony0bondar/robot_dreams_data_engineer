import json
import os

import psycopg2
from hdfs import InsecureClient # library docs https://hdfscli.readthedocs.io/en/latest/index.html

pg_creds = {
    'host': '192.168.88.205'
    , 'port': '5433'
    , 'database': 'postgres'
    , 'user': 'pguser'
    , 'password': 'secret'
}

gp_creds = {
    'host': '192.168.88.205'
    , 'port': '5433'
    , 'database': 'postgres'
    , 'user': 'gpuser'
    , 'password': 'secret'
}

def main():

    client = InsecureClient(f'http://127.0.0.1:50070/', user='user')

    # create directory in HDFS
    client.makedirs('/test')

    #list content
    ll = client.list('/')
    print(f"list of files: {ll}")

    # create file in HDFS
    data = [{"name": "Anne", "salary": 10000}, {"name": "Victor", "salary": 9500}]
    with client.write('/test/sample_file.json', encoding='utf-8') as json_file_in_hdfs:
        json.dump(data, json_file_in_hdfs)
    # OR
    client.write(os.path.join('/', 'test', 'sample_file2.json'), data=json.dumps(data), encoding='utf-8')

    # download file from HDFS
    client.download('/test/sample_file.json', './file_from_hadoop.json')

    # upload file to HDFS
    client.upload('/test/local_file_in_hadoop1.json', './file_from_hadoop.json')
    client.upload('/test/local_file_in_hadoop2.json', './file_from_hadoop.json')
    client.upload('/test/local_file_in_hadoop3.json', './file_from_hadoop.json')

    # rename file
    client.rename('/test/local_file_in_hadoop2.json', '/test/local_file_in_hadoop22222.json')

    # delete file from HDFS
    client.delete('/test/local_file_in_hadoop3.json', recursive=False)

    # copy table's data from PostgreSQL to HDFS
    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        with client.write('/test/dump.csv',) as csv_file:
            cursor.copy_expert('COPY users(id, name) TO STDOUT WITH HEADER CSV', csv_file)

    # copy data from HDFS to Greenplum
    with psycopg2.connect(**gp_creds) as gp_connection:
        cursor = gp_connection.cursor()
        with client.read('/test/dump.csv') as csv_file:
            cursor.copy_expert('COPY users(id, name) FROM STDIN WITH HEADER CSV', csv_file)


if __name__ == '__main__':
    main()
