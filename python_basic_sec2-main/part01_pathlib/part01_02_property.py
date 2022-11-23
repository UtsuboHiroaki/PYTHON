from pathlib import Path

# カレントディレクトリを示す Path オブジェクトを生成します
path = Path(__file__)
print(path)
print(path.exists())
print(path.is_file())
print(path.is_dir())

# 親ディレクトリを示す Path オブジェクトを生成します
parent_path = path.parent
print(parent_path)
print(parent_path.exists())
print(parent_path.is_file())
print(parent_path.is_dir())

# ファイル名関係
print(path.name)
print(path.stem)
print(path.suffix)

# サブディレクトリを順番に取り出す
children = parent_path.iterdir()
for child in children:
    print(child)

# glob - すべて順番に取り出す
items = parent_path.glob('**')
for item in items:
    print(item)

# glob - .py ファイルのみを順番に取り出す
items = parent_path.glob('*.py')
for item in items:
    print(item)

print('終了しました')
