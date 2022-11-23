from datetime import datetime
from pathlib import Path

path = Path(__file__).parent
utf8_file_path = path / 'data' / 'new_file_utf8.txt'

# 上書きモードでファイルを開く
with utf8_file_path.open(mode='w', encoding='utf-8') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 最初の一行\n')

# 追記モードでファイルを開く
with utf8_file_path.open(mode='a', encoding='utf-8') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 2行目\n')

# 書き込んだデータを読んでみよう
with utf8_file_path.open(mode='r', encoding='utf-8') as file:
    print(file.read())
