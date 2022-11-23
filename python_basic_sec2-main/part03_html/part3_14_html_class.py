"""
classで絞りこむ

class はひとつのタグ内に複数含まれていることもある。
"""
from pathlib import Path
from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

company_link_list = soup.select('.company-link')
for link in company_link_list:
    print(link.getText(), link['href'])

# 以下では、複数クラスを両方含むもののみを抽出している
metal_company_link = soup.select_one('.company-link.metal')
print(metal_company_link.getText(), metal_company_link['href'])

