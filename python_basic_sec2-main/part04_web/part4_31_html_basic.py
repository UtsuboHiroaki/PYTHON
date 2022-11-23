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

import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

# まずは、html文書を BeautifulSoup に取りこませる
soup = BeautifulSoup(response.text, "html.parser")

# 取り込めたことを確認してみる
print(soup)

anchors = soup.select('a')  # a タグをすべてリスト
for anchor in anchors:
    print(anchor.getText(), anchor['href'])

anchors = soup.select('section a')  # section タグ内の a タグをすべてリスト
for anchor in anchors:
    print(anchor.getText(), anchor['href'])

# 以下のように、次第に絞りこんでいくこともできる
footer = soup.select_one('footer')
footer_links = footer.select('a')
for link in footer_links:
    print(link.getText(), link['href'])
