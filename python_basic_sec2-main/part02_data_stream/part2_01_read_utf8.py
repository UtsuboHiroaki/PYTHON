from pathlib import Path

path = Path(__file__).parent
utf8_text_path = path / 'data' / 'text_utf8.txt'

# 一気に全行読み込む
with utf8_text_path.open(mode='r', encoding='utf-8') as file:
    print(file.read())

# 一行ずつ読み込む
with utf8_text_path.open(mode='r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

# utf8 のファイルを shiftjis (cp932) で読み込もうとすると、失敗する
# with utf8_text_path.open(mode='r', encoding='shift_jis') as file:
#     print(file.read())
#
# with utf8_text_path.open(mode='r', encoding='cp932') as file:
#     print(file.read())
