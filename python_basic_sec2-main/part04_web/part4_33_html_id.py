"""
idで絞りこむ

id は、その性質上、同一ページに1しか存在しない(はず)。
"""
import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

# id はひとつしかない(はず)。なので、idで要素を取得するならば、select_one を使うことになる。
metal_link = soup.select_one('#galapagos-metal')
print(metal_link.getText(), metal_link['href'])
