"""
jsonデータをダウンロードして解析する。
取得元が、ローカルのファイルではなく、レスポンスボディとなっただけ。
"""
import json
import requests

url = 'https://flask.pc5bai.com/metal/api/info/gold/'
response = requests.get(url)
if response.status_code != 200:  # ステータスコードが200であることを確認する
    print(response.status_code)
    exit(1)

result_dict = json.loads(response.text)  # jsonデータを辞書型に変換する

print(result_dict['metal_type'], result_dict['buy'], result_dict['sell'], )
