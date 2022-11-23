"""
タグで絞りこむ
"""
from pathlib import Path
from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# select, select_one それぞれの戻り値に注意！
# select の戻り値はリスト,  select_one の戻り値はリストではない
footers = soup.select('footer')
for item in footers:
    print(item.getText())
footer = soup.select_one('footer')  #
print(footer.getText())

