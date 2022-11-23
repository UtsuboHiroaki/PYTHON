from pathlib import Path

# 引数として文字列を渡してディレクトリを示す Path オブジェクトを生成します
path = Path("D:/projects/python_basic_sec2/part01_pathlib")
print(path)

# カレントディレクトリを示す Path オブジェクトを生成します
path = Path.cwd()  # current working directory
print(path)

path = Path(__file__).parent  # __file__ はこのファイルのパスを示す変数です
print(path)

# 親ディレクトリを示す Path オブジェクトを生成します
parent_path = path.parent
print(parent_path)

# 親ディレクトリを順にリストします。すべて、 Path オブジェクトです。l
parents = path.parents
for parent in parents:
    print(type(parent), parent)

# 子ディレクトリを示す Path オブジェクトを生成します(その1)
child_path = path / "part01_01_path.py"
print(child_path)
print(child_path.exists())  # 存在確認

child_path = path / "sub_dir" / "sub_file1.txt"
print(child_path)
print(child_path.exists())  # 存在確認

# 子ディレクトリを示す Path オブジェクトを生成します(その2)
child_path = path.joinpath("part01_01_path.py")
print(child_path)
print(child_path.exists())  # 存在確認

child_path = path.joinpath("sub_dir", "sub_file1.txt")
print(child_path)
print(child_path.exists())  # 存在確認

print('終了しました')
