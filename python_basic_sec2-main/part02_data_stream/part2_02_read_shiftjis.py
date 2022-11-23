"""
エンコードを正しく指定しないとファイルを読み込めない。
あるいは、文字化けする。

特に、Windows環境では、エンコードがShift_JISの場合がままあるので注意。
Shift_JISでエンコードされたテキストファイルを読む際には、 cp932 というエンコードを指定する。
shift_jis を指定しても動くこともあるが、 cp932 のほうがややリスクが少ないよう。
(詳しい仕様の違いは、 https://docs.python.org/ja/3/library/codecs.html#standard-encodings を参照)
"""
from pathlib import Path

path = Path(__file__).parent
shiftjis_file_path = path / 'data' / 'text_shiftjis.txt'

# shiftjis のファイルを shiftjis で読み込む
# with shiftjis_file_path.open(mode='r', encoding='shift_jis') as file:
#     print(file.read())
#
# # shiftjis のファイルを cp932 で読み込む(cp932 のほうが若干おすすめ)
# with shiftjis_file_path.open(mode='r', encoding='cp932') as file:
#     print(file.read())

# shiftjis のファイルを utf-8で読み込もうとすると、失敗する
with shiftjis_file_path.open(mode='r', encoding='utf-8') as file:
    print(file.read())
