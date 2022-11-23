"""
csvファイルをダウンロードして解析する
取得元が、ローカルのファイルではなく、レスポンスボディとなっただけ

"""
import csv
from io import StringIO

import requests

url = 'https://flask.pc5bai.com/stock/info/csv/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

with StringIO(response.text) as string_io:
    reader = csv.reader(string_io)
    for row in reader:
        print(row)

with StringIO(response.text) as string_io:
    dict_reader = csv.DictReader(string_io)
    for row in dict_reader:
        print(row)
