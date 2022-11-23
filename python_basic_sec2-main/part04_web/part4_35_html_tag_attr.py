"""
タグ と属性で同時に絞りこめる。
"""
import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

# 以下では、 div タグであって、クラスが company-info のもののみを抽出している
company_info_list = soup.select('div.company-info')
for company_info in company_info_list:
    print(company_info.getText())

# 以下では、 a タグであって target 属性の値が _blank なもののみ抽出している
ext_links = soup.select('a[target="_blank"]')
for link in ext_links:
    print(link.getText(), link['href'])
