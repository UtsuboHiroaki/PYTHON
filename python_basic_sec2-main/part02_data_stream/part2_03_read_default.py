"""
エンコード指定をはずすと、プラットフォーム(os)によって定められたデフォルトのエンコードで読み込もうとする。
(エンコードは指定するもの」と覚えましょう)
"""
from pathlib import Path

path = Path(__file__).parent

utf8_file_path = path / 'data' / 'text_utf8.txt'
shiftjis_file_path = path / 'data' / 'text_shiftjis.txt'

# 文字コードを指定しないで、 utf8 でエンコードされたファイルを読み込もうとする
# Windows環境では失敗する。
with utf8_file_path.open(mode='r', ) as file:
    print(file.read())

# 文字コードを指定しないで、 shift_jis でエンコードされたファイルを読み込もうとする
# Mac, Linux 環境では失敗する
with shiftjis_file_path.open(mode='r', ) as file:
    print(file.read())
