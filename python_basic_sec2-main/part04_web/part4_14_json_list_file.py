"""
jsonデータをダウンロードして保存する。
jsonのリストを受け取るとしても、特にやることは変わらない。
"""
from pathlib import Path
import requests

url = 'https://flask.pc5bai.com/metal/api/info/'

response = requests.get(url)

# ステータスコードを確認する
print(response.status_code)

# ファイルを保存する
path = Path(__file__).parent / 'data' / 'metal_all.json'
with path.open('w', encoding='utf-8', ) as f:
    f.write(response.text)
