"""
csvファイルをダウンロードして解析する
取得元が、ローカルのファイルではなく、レスポンスボディとなっただけ

"""
import csv

import requests

url = 'https://flask.pc5bai.com/stock/info/csv/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

text_lines = response.text.splitlines()

reader = csv.reader(text_lines, )
for row in reader:
    print(row)

dict_reader = csv.DictReader(text_lines, )
for row in dict_reader:
    print(row)
