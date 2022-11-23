"""
jsonデータをダウンロードして保存する。
"""
from pathlib import Path

import requests

url = 'https://flask.pc5bai.com/metal/api/info/gold/'
response = requests.get(url)
if response.status_code != 200:
    print(response.status_code)
    exit(1)

# ファイルを保存する
path = Path(__file__).parent / 'data' / 'gold.json'
with path.open('w', encoding='utf-8', ) as f:
    f.write(response.text)
