"""
idで絞りこむ

id は、その性質上、同一ページに1しか存在しない(はず)。
"""
from pathlib import Path
from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# id はひとつしかない(はず)。なので、idで要素を取得するならば、select_one を使うことになる。
metal_link = soup.select_one('#galapagos-metal')
print(metal_link.getText(), metal_link['href'])
