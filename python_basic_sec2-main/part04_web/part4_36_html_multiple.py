"""
複数の条件を組み合わせて絞りこめる。
"""
import requests
from bs4 import BeautifulSoup

url = 'https://flask.pc5bai.com/'
response = requests.get(url)

if response.status_code != 200:
    print(response.status_code)
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

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
