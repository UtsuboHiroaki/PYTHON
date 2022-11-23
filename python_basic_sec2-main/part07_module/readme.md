# プログラムの実行、モジュール/オブジェクトのインポート

## Python プログラムの実行

Python プログラムの実行方法には、大きく分けて、以下の2とおりがある。

1. 対話モードで実行する:
2. コマンドラインからモジュールを指定して実行する:

### 1. 対話モードで実行する:

powewrshell:

```shell
python
>>> print("こんにちは")
こんにちは
>>> 3 + 5
8
>>> exit()
```

***

### 2. コマンドラインからモジュールを指定して実行する:

main01.py

```python
print("こんばんは")
print(5 * 7)
```

powewrshell/dos等:

```shell
> python -m main01
こんばんは
35
```

-m オプションなしで実行することもできる。  
その場合は、 .py まで記述する。

powewrshell/dos等:

```shell
> python main01.py
こんばんは
35
```

***

コマンドラインから引数を渡すこともできる。  
(Pythonスクリプト側での引数の処理については次章にて扱う)

write_list.py

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min', type=int, default=3, help='初期値を指定します')
    parser.add_argument('-i', '--items', type=int, default=5, help='出力する要素数を指定します')

    args = parser.parse_args()

    min_value = args.min
    max_value = args.min + args.items

    result_list = list(range(min_value, max_value, ))
    print(result_list)
```

powewrshell/dos等:

```shell
> python write_list.py -m 5 -i 7
[3, 4, 5, 6, 7]
```

***

スクリプトファイルが別ディレクトリにある場合は、以下の要領。  
カレントディレクトリから、パスを `.` で区切って指定する。

sub_dir/sub_module.py

```python
print("おはようございます")
print(7 ** 2)
```

powewrshell:

```shell
> python -m subdir.sub_module
おはようございます
49
```

もっとも、そもそも、こういう呼び出し方をしなくてはならないとしたら設計がよろしくない。  
コマンドラインから呼びだすべモジュールは、プロジェクトのトップディレクトリに配置するべき。

***

## モジュールとパッケージ

### モジュール

モジュールとは、使いまわしたい関数やクラス、変数等が記述されたファイル。  
import 文は、モジュール内で定義されたオブジェクトを利用可能にするための文。

- モジュールの拡張子は .py であること。
- モジュールの文字コードは UTF-8 であること。

[参考: Python チュートリアル » 6. モジュール](https://docs.python.org/ja/3/tutorial/modules.html)

### パッケージ

パッケージは、複数モジュールをまとめたひとつのディレクトリ。  
パッケージには、 `__init__.py` というモジュールを必ず含める。  
(`__init__.py` がないと、pythonは、パッケージ内のモジュールを正しく読み込めないことがある)

`__init__py` の中身は空でも問題ない。

インポート対象としてパッケージを指定した場合は、そのパッケージ内の `__init__.py` の内容がインポートされる。  
[参考: Python チュートリアル » 6. モジュール > 6.4. パッケージ](https://docs.python.org/ja/3/tutorial/modules.html#packages)

***

## import 文

import 文の書き方には、絶対インポートと相対インポートの2種類がある。

| 種類      | インポート対象の所在の記述方法                                              | 例                                   |
|---------|--------------------------------------------------------------|-------------------------------------|
| 絶対インポート | main モジュールの所在を起点に記述する<br>少なくとも、 main モジュール(後述)では必ずこの方法で記述する。 | from package.module import function |
| 相対インポート | そのモジュールの所在を起点に記述する<br>あまり大掛かりな探索はしないほうがよい。                   | from .module import function        |

[参考: Python チュートリアル » 6. モジュール > 6.4.2. パッケージ内参照](https://docs.python.org/ja/3/tutorial/modules.html#intra-package-references)

### import 文の書式

#### 絶対インポート

以下を覚えておけば、あとは、パリエーションでなんとかなる。

```python
import module_name  # モジュールをインポートする
import package_name  # パッケージをインポートする (__init__.py の内容がインポートされる)
from module_name import object_name  # モジュール内のオブジェクトをインポートする
from module_name import *  # モジュール内のすべてのオブジェクトをインポートする(非推奨)
from package_name import module_name  # パッケージ内のモジュールをインポートする
from package_name.module_name import object_name  # パッケージ内のモジュール内のオブジェクトをインポートする
```

#### 相対インポート

以下を覚えておけば、あとは、絶対インポートのときのやり方の類推でなんとかなる。

```python
from .module_name import object_name  # 同一ディレクトリのモジュール内にあるオブジェクトをインポートする
from ..module_name import object_name  # ひとつ上のディレクトリのモジュール内にあるオブジェクトをインポートする
```

ただし、上位のパッケージを多く辿っていくのは推奨できない。  
パッケージは、同一機能のプログラムのさらに細分化されたものをまとめるためのものだからである。  
[参考: Python チュートリアル » 6. モジュール > 6.4. パッケージ](https://docs.python.org/ja/3/tutorial/modules.html#packages)  

#### インポート文での as の使用

以下のように、インポートしたオブジェクトに別名をつけることもできる。  
別名をつけることで、同じモジュール内のオブジェクト名が衝突することを防ぐことができる。  
別名は、インポート文でオブジェクトを呼び出したモジュール内でのみ有効。

```python
import module_name as alias1  # インポートしたモジュールに alias1 という別名をつける 
from module_name import object_name as alias2  # インポートしたオブジェクトに alias1 という別名をつける
from package_name import module_name as alias3  # インポートしたモジュールに alias3 という別名をつける
from package_name.module_name import object_name as alias4  # インポートしたオブジェクトに alias4 という別名をつける
```

### import したオブジェクトの利用

インポートしたオブジェクトは、以下のように利用する。

sub.py

```python
def func1():
    print("関数 func1() が呼び出されました")


def func2():
    print("関数 func2() が呼び出されました")
```

main11_absolute_module.py

```python
import sub

sub.func1()
sub.func2()
```

main13_absolute_object.py

```python
from sub import func1, func2

func1()
func2()
```

なお、main41_absolute_object.py のように、 import 対象をモジュール内のオブジェクトに限定することもできる。  
しかし、その場合もモジュール内のコードは実行されてしまう。

```python
print("sub_with_process.py の読み込みを開始します")


def func1():
    print("関数 func1() が呼び出されました")


def func2():
    print("関数 func2() が呼び出されました")


func1()
```

main41_absolute_object.py

```python
from sub_with_process import func2

func2()
```

```shell
> python main41_absolute_object.py
関数 func1() が呼び出されました
関数 func2() が呼び出されました
```

ついては、モジュール内のコードを実行したくない場合は、以下の `__name__` 変数の値による条件分岐を行う。

### グローバル変数 `__name__`

モジュールの中では、そのモジュールのモジュール名をグローバル変数 `__name__` で取得できる。  
ただし、 `__name__` は、コマンドラインから直接呼び出されたときは `__main__` となる。  
(逆に言うと、 import 文で呼び出されたときは、モジュール名となる)

この性質を利用して、モジュールの中で、「コマンドラインから直接呼び出されたときだけ実行される処理」を記述することができる。  
以下の要領。

sub_without_process.py

```python
def func1():
    print("関数 func1() が呼び出されました")


def func2():
    print("関数 func2() が呼び出されました")


if __name__ == "__main__":
    func1()
```

main42_absolute_object_without.py

```python
from sub_without_process import func2

func2()
```

```shell
> python main42_absolute_object_without.py
関数 func2() が呼び出されました
```

[3.10.6 Documentation » Python 標準ライブラリ » Python ランタイムサービス » __
main__ --- Top-level code environment](https://docs.python.org/ja/3/library/__main__.html#module-__main__)

***

## 推奨の記法、諸注意、追記事項:

### 1. import対象は極力限定する

以下の理由から、都度都度、必要なオブジェクトだけを指定してインポートする方が望ましい。

- 可読性のため
- 変数等の汚染のリスクを避けるため(変数名の競合のリスクが減る)
- 高速化のため(モジュール全体をインポートするより高速)

### 2. インポート文の記載場所と優先順位

インポート文は、極力、モジュールの先頭に記載する。  
ただし、モジュール先頭のdocstringより後。

例外:  
ただし、インポート文をモジュール先頭に置くことで不具合が生じる場合は、関数やメソッド内に記述することもある。

インポート文の記載順序は、以下の優先順位に従うことが望ましい。

1. 標準ライブラリ
2. サードパーティ製ライブラリ
3. 自作ライブラリ

それぞれについて、 abc 順に記載する。

Pycharmのショートカットキー`[Alt] + [Ctrl] + [O]`(Code > Optimize Imports)で、インポート文を自動で整理することができる。

### 3. インポート文でインポートできないもの

以下については、 from module import * でインポートすることはできない。

- モジュール内の `_` ではじまる名前のオブジェクト
- モジュール内に `__all__` が定義されている場合、 `__all__`  で明示されなかったオブジェクト  
  (自分で実装することはまずないが、ある程度の規模のパッケージでは見かけることがある)

[6.4.1. パッケージから * を import する](https://docs.python.org/ja/3/tutorial/modules.html#importing-from-a-package)

もっとも、 import * という記法自体がよろしくない。  
使い捨てのプログラムを書くときに簡便な手法として使う程度にとどめるべき。

### 4. モジュールとパッケージの名称

module と package で同名のものがあると不具合が起きるので、注意。  
モジュールを見に行ってしまい、パッケージ内は見に行かないため。  
Pythonあるあるです (^^;

***

### 5. import_module 関数によるインポート

importlib.import_module 関数は、インポート対象をプログラム実行開始後に動的に決定したい場合に使う。(*1)  
importlib.import_module を使う場合の挙動を分解すると、以下のとおり。

1. 利用したいプログラムを設定ファイル内に記述しておく
2. プログラムは、実行開始すると、設定ファイルを読み込む
3. 設定ファイルの内容に従って、インポート対象を決定する
4. import_module 関数を使って、インポート対象をインポートする

import_module 関数を自分で使うことはまずないが、ある程度の規模のパッケージでは見かけることがある。

たとえば django の settings.py では、デフォルトで以下のような設定がされている。

django は、起動時に、この設定ファイルを読み込み、インポート対象を決定して読み込む。  
つまり、 import_module 関数を使って、変数 INSTALLED_APPS, 変数 MIDDLEWARE で指定されたモジュール/オブジェクトを順番に読み込んでいる。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## Pythonでのオブジェクトのネーミングルール

この機会に、Python での一般的なネーミングルールを以下に示す。

| 名前            | 説明               |
|---------------|------------------|
| モジュール名、パッケージ名 | snake_case で記述する |
| 変数名           | snake_case で記述する |
| 定数名           | 全て大文字で記述する(*2)   |
| 関数名、メソッド名     | snake_case で記述する |
| クラス名          | PascalCase で記述する |

- [snake_case](https://forum.pc5bai.com/tips/glossary/snake_case/)
- [PascalCase](https://forum.pc5bai.com/tips/glossary/pascal_case/)

名称の先頭に `_` を1つまたは2つつけたオブジェクトを見かけることがある。  
そのニュアンスは、以下のとおり。

| パターン  | ニュアンス                                                                           | 例                         | 
|-------|---------------------------------------------------------------------------------|---------------------------|
| 1つの場合 | 「外部から直接呼び出されない、呼び出してはいけない」というニュアンスになる。                                          | _get_inner_file()         | 
| 2つの場合 | Pythonのかなりコアな部分の機能に関わるものというニュアンス。<br>既存のものを上書きすることはあるが、自作のオブジェクトではこういう名前は避けること。 | `__truediv__`, `__name__` |

***

(*1)
後述のクラスインスタンスでの setattr, getattr, hasattr, delattr 等も、文字列ベースでオブジェクトを指定する方法の例。  
「オブジェクトを文字列ベースで指定する方法がある」ということは、慣れないととっつきにくいかもしれない。

(*2)  
Pythonは、「値の変更が不可能なオブジェクト」とか「外部からアクセスできないオブジェクト」という概念が希薄。  
定数という趣旨ですべて大文字で記述したオブジェクトであっても、モジュール内で書き換え可能。  
Python では、記法によってプログラマの意図を表現するにとどめている。
