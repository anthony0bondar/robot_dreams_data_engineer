import json
import os

from hdfs import InsecureClient # library docs https://hdfscli.readthedocs.io/en/latest/index.html


def main():

    client = InsecureClient(f'http://127.0.0.1:50070/', user='user')

    # create directory in HDFS
    client.makedirs('/test')

    #list content
    ll = client.list('/')
    print(ll)

    # create file in HDFS
    data = [{"name": "Anne", "salary": 10000}, {"name": "Victor", "salary": 9500}]
    with client.write('/test/sample_file.json', encoding='utf-8') as json_file_in_hdfs:
        json.dump(data, json_file_in_hdfs)
    # OR
    client.write(os.path.join('/', 'test', 'sample_file2.json'), data=json.dumps(data), encoding='utf-8')

    # download file from HDFS
    client.download('/test/sample_file.json', './file_from_hadoop.json')

    # upload file to HDFS
    client.upload('/test/local_file_in_hadoop.json', './file_from_hadoop.json')


if __name__ == '__main__':
    main()
