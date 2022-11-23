"""
csvファイルをダウンロードして解析する
取得元が、ローカルのファイルではなく、レスポンスボディとなっただけ

"""
from pathlib import Path

import requests

url = 'https://flask.pc5bai.com/stock/info/csv/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

# ファイルを保存する
path = Path(__file__).parent / 'data' / 'stock.csv'
with path.open('w', encoding='utf-8', newline='') as f:
    f.write(response.text)
