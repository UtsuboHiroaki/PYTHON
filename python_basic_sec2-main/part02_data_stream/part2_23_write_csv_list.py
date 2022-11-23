"""
csv.writer を使うと、csvファイルに書き込むことができる
"""
import csv
from pathlib import Path

base_path = Path(__file__).parent
by_list_path = base_path / 'data' / 'csv_write_by_list.csv'

with by_list_path.open(mode='w', encoding='utf-8', newline='', ) as file:
    # csvファイルにデータをリストとして書き込む
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', '田中', '25'])
    writer.writerow(['2', '佐藤', '35'])
