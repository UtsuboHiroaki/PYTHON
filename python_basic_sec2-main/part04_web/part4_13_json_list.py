"""
jsonデータをダウンロードして解析する。
jsonのリストを受け取るとしても、特にやることは変わらない。
"""
import json
import requests

url = 'https://flask.pc5bai.com/metal/api/info/'
response = requests.get(url)
if response.status_code != 200:
    print(response.status_code)
    exit(1)

result_dict_list = json.loads(response.text)
for result_dict in result_dict_list:
    print(result_dict['metal_type'], result_dict['buy'], result_dict['sell'], )
