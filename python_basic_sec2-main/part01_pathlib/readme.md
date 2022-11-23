# pathlib.Path:

pathlib.Path オブジェクトを生成して、ファイルやディレクトリを操作できる。  
その手の処理用の機能として os モジュールの関数があったが、Python 3.4 から pathlib モジュールが標準ライブラリに追加された。

## ディレクトリ/ファイル関連のライブラリ比較:

| ライブラリ        | メモ                                                                |
|--------------|-------------------------------------------------------------------|
| os           | 古い。pathlib.Pathを使うのが正解。                                           |
| pathlib.Path | Python3.4から登場。 osモジュールの代替。クラス。                                    |
| shutil       | ファイル/ディレクトリ操作の便利機能が集まっている。<br>すなわち、copy, move, delete 関連の便利機能の集合体。 |

特に、shutil では、shutil.rmtree (ディレクトリを中身ごと削除)だけは真っ先に覚えたい。

[os --- 雑多なオペレーティングシステムインターフェース](https://docs.python.org/ja/3/library/os.html)  
[pathlib --- オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)  
[shutil --- 高水準のファイル操作](https://docs.python.org/ja/3/library/shutil.html)

## ファイル、フォルダ操作の主要なプロパティとメソッドまとめ

1. 基本方針:
    - pathlib.Path でなんとかできないか検討する
    - osモジュールにあるものはたいていある
2. 慣れてきたら:
    - shutil により便利なものがないか探す(分量はそんなに多くない)  
      [shutil --- 高水準のファイル操作](https://docs.python.org/ja/3/library/shutil.html)

| 項目      | 方針                              | 方針                                               |
|---------|---------------------------------|--------------------------------------------------|
| パス生成/移動 | 現在のパスを元にPathオブジェクトを作る           | pathlib.Path.cwd()                               |
| パス生成/移動 | 引数からPathオブジェクトを作る               | pathlib.Path()                                   |
| パス生成/移動 | 親ディレクトリへ移動                      | pathlib.Path.parent, pathlib.Path.parents        |
| パス生成/移動 | 子ディレクトリへ移動                      | pathlib.Path() / 'sub_dir'                       |
| パス生成/移動 | 子ディレクトリへ移動                      | pathlib.Path().joinpath('sub_dir1', 'subdir_2',) |
| パス情報確認/取得 | 存在するか？                          | pathlib.Path.exists()                            |
| パス情報確認/取得 | ファイルか？                          | pathlib.Path.is_file()                           |
| パス情報確認/取得 | ディレクトリか？                        | pathlib.Path.is_dir()                            |
| パス情報確認/取得 | 名前を取得                           | pathlib.Path.name                                |
| パス情報確認/取得 | 拡張子の手前までを取得                     | pathlib.Path.stem                                |
| パス情報確認/取得 | 拡張子を取得                          | pathlib.Path.suffix                              |
| ディレクトリ  | サブディレクトリ(ファイルもディレクトリも)を iterate | pathlib.Path.iterdir()                           |
| ディレクトリ  | 条件にマッチする子要素を取得                  | pathlib.Path.glob()                              |
| ディレクトリ  | 生成                            | pathlib.Path.mkdir()                             |
| ディレクトリ  | 移動                              | pathlib.Path.replace()                            |
| ディレクトリ  | 削除                              | shutil.rmtree()                                  |
| ファイル    | 生成                              | pathlib.Path.touch()                             |
| ファイル    | 移動                              | pathlib.Path.replace()                            |
| ファイル    | 削除                              | pathlib.Path.unlink()                            |

pathlib ページ内の、 os モジュールにあるツールとの対応付けも参照のこと。  
[os モジュールにあるツールとの対応付け](https://docs.python.org/ja/3/library/pathlib.html#correspondence-to-tools-in-the-os-module)

## pathlib.Path オブジェクトの生成

pathlib.Path オブジェクトは、ファイルやディレクトリのパスを表す。

Path オブジェクトの引数の渡し方はいろいろあるが、まずは以下を覚えたい。

```python
from pathlib import Path

# パス文字列を生成する
path = Path('D://projects/python_basic_sec2', )

# 実行中のモジュールのパスを使う
path = Path(__file__)  # __file__ で、実行中のモジュールのパスを示す文字列を得られる
```

現在のパスを得る

```python
from pathlib import Path

# パス文字列を生成する
path = Path.cwd()

# 実行中のモジュールのパスを使う
path = Path(__file__)  # __file__ で、実行中のモジュールのパスを示す文字列を得られる
```

## パスの移動

Pathオブジェクトに演算子 / を使うと、パスを連結して下位のパスを作ることができる。

```python
from pathlib import Path

path = Path('D://projects/python_basic_sec2', )
new_path = path / 'part1_pathlib' / 'readme.md'
```

joinpath() でも同様の結果を得られる。

```python
from pathlib import Path

path = Path('D://projects/python_basic_sec2', )
new_path = path.joinpath('part1_pathlib', 'readme.md')
```

親ディレクトリへの移動は、parents 属性等を使う。

```python
from pathlib import Path

path = Path('D://projects/python_basic_sec2', )
path = path / 'part1_pathlib' / 'readme.md'
new_path1 = path.parent  # 親ディレクトリへ移動
new_path2 = path.parents[1]  # 親ディレクトリへ移動
```

## pathilb.Path の主要なメソッド1

```python
from pathlib import Path

path = Path('D:', 'projects', 'python_basic_sec2', )

# パスがあるかどうか確かめる
path.exists()  # True/False

# パスがファイルかどうか確かめる
path.is_file()  # True/False

# パスがディレクトリかどうか確かめる
path.is_dir()  # True/False

# パス名を取得する
path.name  # 'python_basic_sec2'

# パスの拡張子を取得する
path.suffix  # ''

# 拡張子を除いたファイル名を取得する
path.stem  # 'python_basic_sec2'
```

## pathilb.Path の主要なメソッド2

```python
from pathlib import Path

path = Path('D:', 'projects', 'python_basic_sec2', )

# 直下の一覧を取得
for item in path.iterdir():
    print(item)

# 条件を指定して再帰的に一覧を取得
# ** は、再帰的に検索することを意味する
# とりあえずこれだけ覚えておけばあとはなんとかなる
for item in path.glob('**'):
    print(item)
```

## ディレクトリの作成と削除

```python
from pathlib import Path

path = Path('D:', 'projects', 'python_basic_sec2', )

# ディレクトリを作成する
new_dir1 = path / 'new_dir1'
new_dir1.mkdir()

# ディレクトリを作成する（すでに存在している場合も以下の書き方であればエラーにならない）
new_dir1.mkdir(exist_ok=True)

# ディレクトリを削除する
new_dir1.rmdir()
```

```python
import shutil
from pathlib import Path

path = Path('D:', 'projects', 'python_basic_sec2', )

# ディレクトリを作成する(中間ディレクトリも一気に作成する)
new_dir2 = path / 'new_dir2' / 'new_dir3'
new_dir2.mkdir(parents=True)

# 中身のあるディレクトリを削除するには、 shutil.rmtree() を使う
shutil.rmtree(new_dir2)
```
