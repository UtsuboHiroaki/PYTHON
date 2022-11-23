"""
タグで絞りこむ
"""
import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

# select, select_one それぞれの戻り値に注意！
# select の戻り値はリスト,  select_one の戻り値はリストではない
footers = soup.select('footer')
for item in footers:
    print(item.getText())
footer = soup.select_one('footer')  #
print(footer.getText())

