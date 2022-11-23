import shutil
from pathlib import Path

# ディレクトリ/ファイルの生成/削除
path = Path(__file__).parent
child_path = path / 'child'

Path.mkdir(child_path)

file1_path = child_path / 'hoge1.txt'
Path.touch(file1_path)

file2_path = child_path / 'hoge2.txt'
Path.touch(file2_path)

Path.unlink(file1_path)  # ファイルを削除
shutil.rmtree(child_path)  # 中身があってもまるごと削除

# ディレクトリ/ファイルの移動
path_from = path / 'base_dir'
path_to = path / 'target_dir'

Path.mkdir(path_from)
current_path = path_from.replace(path_to)  # base_dir ディレクトリを target_dir ディレクトリに移動
print(current_path)

shutil.rmtree(current_path)  # 中身があってもまるごと削除

print('終了しました')
