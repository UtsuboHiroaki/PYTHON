"""
タグ と属性で同時に絞りこめる。
"""
from pathlib import Path

from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# 以下では、 div タグであって、クラスが company-info のもののみを抽出している
company_info_list = soup.select('div.company-info')
for company_info in company_info_list:
    print(company_info.getText())

# 以下では、 a タグであって target 属性の値が _blank なもののみ抽出している
ext_links = soup.select('a[target="_blank"]')
for link in ext_links:
    print(link.getText(), link['href'])
