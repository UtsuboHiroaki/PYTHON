"""
classで絞りこむ

class はひとつのタグ内に複数含まれていることもある。
"""
import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

company_link_list = soup.select('.company-link')
for link in company_link_list:
    print(link.getText(), link['href'])

# 以下では、複数クラスを両方含むもののみを抽出している
metal_company_link = soup.select_one('.company-link.metal')
print(metal_company_link.getText(), metal_company_link['href'])

