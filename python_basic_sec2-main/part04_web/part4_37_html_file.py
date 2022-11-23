"""
BeautifulSoup での HTML ページ解析の基本方針:
以下によって、絞りこむ
    タグ
    ID
    クラス
    (属性)

絞りこんで得られるものが、単体の要素なのか、リストなのかに注意！(戻り値を確認すること)
    select_one: 戻り値は単体
    select    : 戻り値はリスト
"""
from pathlib import Path

import requests

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

# ファイルを保存する
path = Path(__file__).parent / 'data' / 'info.html'
with path.open('w', encoding='utf-8') as f:
    f.write(response.text)
