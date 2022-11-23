"""
csv.DictWriter を使うと、csvファイルに辞書の内容を書き込める
"""
import csv
from pathlib import Path

base_path = Path(__file__).parent

by_write_path = base_path / 'data' / 'csv_write_by_dict.csv'

with by_write_path.open(mode='w', encoding='utf-8', newline='', ) as file:
    # csvファイルにデータを辞書として書き込む
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerow({'id': '3', 'age': '27', 'name': '花子', '住所': '東京都', })
    writer.writerow({'name': '太郎', '住所': '神奈川県', 'age': '37', 'id': '4', })
