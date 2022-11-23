"""
csv.reader を使うと、csvファイル内の各行の中身をリストとして取得できる
"""
import csv
from pathlib import Path

base_path = Path(__file__).parent
csv_file_path = base_path / 'data' / 'csv_sample.csv'

with csv_file_path.open(mode='r', encoding='utf-8',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
