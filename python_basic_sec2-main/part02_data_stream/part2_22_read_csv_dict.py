"""
csv.DictReader を使うと、csvファイル内の各行の中身を辞書として取得できる
"""
import csv
from pathlib import Path

base_path = Path(__file__).parent
csv_file_path = base_path / 'data' / 'csv_sample.csv'

with csv_file_path.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# with csv_file_path.open(mode='r', encoding='utf-8', newline='') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['登録番号'], row['名前'], row['住所'], )
