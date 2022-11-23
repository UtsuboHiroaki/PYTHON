from datetime import datetime
from pathlib import Path

path = Path(__file__).parent
shiftjis_file_path = path / 'data' / 'new_file_shiftjis.txt'

# 上書きモードでファイルを開く
with shiftjis_file_path.open(mode='w', encoding='cp932') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 最初の一行\n')

# 追記モードでファイルを開く
with shiftjis_file_path.open(mode='a', encoding='cp932') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 2行目\n')

# 書き込んだデータを読んでみよう
with shiftjis_file_path.open(mode='r', encoding='cp932') as file:
    print(file.read())

