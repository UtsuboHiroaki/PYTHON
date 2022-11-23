"""
複数の条件を組み合わせて絞りこめる。
"""
from pathlib import Path

from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# 以下では、 div.company-info 内の anchor のみを抽出している
company_link_list = soup.select('div.company-info a')
for company_link in company_link_list:
    print(company_link.getText(), company_link['href'])

# 複数条件で絞りこむときは、直接の親子関係になくてもよい
company_link_list = soup.select('section a')
for company_link in company_link_list:
    print(company_link.getText(), company_link['href'])

# いったん section を変数に入れて、そこからさらに .select してみよう
section = soup.select_one('section')
links = section.select('a')
for link in links:
    print(link.getText(), link['href'])
