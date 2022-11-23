"""
エンコード指定をはずすと、プラットフォーム(os)によって定められたデフォルトのエンコードで書き込もうとする。
(エンコードは指定するもの」と覚えましょう)
"""
from datetime import datetime
from pathlib import Path

path = Path(__file__).parent
new_text_file_path = path / 'data' / 'new_file_default.txt'

# 文字コード指定なしでデータsを書き込む
with new_text_file_path.open(mode='w', ) as file:
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 最初の一行\n')

# 書き込んだデータを読んでみよう
# 以下は、Windows環境ではエラーにならない。(デフォルトが shift_jis なので)
with new_text_file_path.open(mode='r', encoding='cp932') as file:
    print(file.read())

# 書き込んだデータを読んでみよう(以下は文字コードがあわないのでエラー)
# 以下は Mac環境ではエラーにならない。(デフォルトが utf-8 なので)
with new_text_file_path.open(mode='r', encoding='utf-8') as file:
    print(file.read())
