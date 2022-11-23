# コマンドラインからの実行

コマンドラインからモジュールを指定してPythonプログラムを実行できる。

part08_01.py

```python
print("こんばんは")
print(5 * 7)
```

powewrshell/dos等:

```shell
> python part08_01.py
こんばんは
35
```

ここで、コマンドラインからPythonスクリプトに引数を渡すことができる。

コマンドラインからPythonスクリプトが受け取った引数の処理には、大きく分けて以下の2つの手段がある。

| 手段       | 説明                                                                                                                                         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| sys.argv | sys.argv は、コマンドラインから渡された引数を格納したリスト。<br>[sys --- システムパラメータと関数 > sys.argv](https://docs.python.org/ja/3/library/sys.html#sys.argv)                   |
| argparse | argparse は、コマンドラインから渡された引数を解析するためのモジュール。<br>[argparse --- コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.org/ja/3/library/argparse.html) |

argparse のほうが、より簡単に引数を処理できる。

***

## sys.argv による引数の処理

sys モジュールの argv には、コマンドラインから渡された引数がリストとして格納されている。  
なお、リストの先頭には、実行されたスクリプト名が格納されている。(*1)

part08_11_argv.py

```python
import sys

print(sys.argv)
```

```shell
> python part08_11_argv.py 1 2 3
['part08_11_argv.py', '1', '2', '3']
```

引数がオプション名を含む場合は、以下のようになる。

main03.py

```python
import sys

print(sys.argv)
```

```shell
> python part08_11_argv.py -a 1 -b 2 -c 3
['part08_11_argv.py', '-a', '1', '-b', '2', '-c', '3']
```

上記のとおり、純粋なリストなので、解析がかなり面倒になる。

(*1)  
リストの先頭には、実行されたスクリプト名が格納されている。  
ファイル名のみが格納されるかファイルのフルパスが格納されるかは、OSによって異なる。

***

## argparse による引数の処理

argparse は、コマンドラインから渡された引数を解析するためのモジュール。

以下は、位置引数を渡す例:

part08_21_argparse.py

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('min', type=int, help='初期値を指定します')
parser.add_argument('items', type=int, help='最大値を指定します')
args = parser.parse_args()

print(args.min)
print(args.items)
my_list = list(range(args.min, args.min + args.items))
print(my_list)
```

```shell
> python part08_21_argparse.py --help
usage: part08_21_argparse.py [-h] min items

positional arguments:
  min         初期値を指定します
  items       最大値を指定します

options:
  -h, --help  show this help message and exit
```

```shell
> python part08_21_argparse.py 4 5
4
5
[4, 5, 6, 7, 8]
```

以下は、キーワード引数を渡す例。

part08_22_argparse.py

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--min', type=int, default=3, help='初期値を指定します')
parser.add_argument('-i', '--items', type=int, default=5, help='出力する要素数を指定します')
parser.add_argument('-c', '--count', action='store_true', help='要素数を返します')
args = parser.parse_args()

print(args.min)
print(args.items)
print(args.count)

my_list = list(range(args.min, args.min + args.items))
print(my_list)
if args.count:
    print(len(my_list))
```

```shell
> python part08_22_argparse.py --help
usage: part08_22_argparse.py [-h] [-m MIN] [-i ITEMS] [-l]

options:
  -h, --help            show this help message and exit
  -m MIN, --min MIN     初期値を指定します
  -i ITEMS, --items ITEMS
                        出力する要素数を指定します
  -l, --length          要素数を返します
```

```shell
> python part08_22_argparse.py -m 4 -i 5
4
5
False
[4, 5, 6, 7, 8]
```

```shell
> python part08_22_argparse.py -m 7 -i 9 --count
7
9
True
[7, 8, 9, 10, 11, 12, 13, 14, 15]
9
```

add_argument メソッドの主要な引数:

| 引数名    | 説明                                                                  |
|--------|---------------------------------------------------------------------|
| ハイフンなし | 先頭に - がない場合は位置引数となる。                                                |
| -n     | キーワード引数(1文字)を指定する場合は、先頭に - をつける。                                    |
| --min  | キーワード引数(2文字以上)を指定する場合は、先頭に -- をつける。                                 |

キーワード引数:

| 引数名     | 説明                                                                                    |
|---------|---------------------------------------------------------------------------------------|
| type    | 引数の型を指定する。単一の文字列を受け入れる任意の callable にすることができる。(*2)<br>ただし、bool型は指定しないこと。(*3)           |
| default | 引数のデフォルト値を指定する。                                                                       |
| action  | 引数のアクションを指定する。<br>bool 型を指定したい場合は、action='store_true' または action='store_false' を指定する。 |
| help    | 引数のヘルプを指定する。                                                                          |

(*2)  
[argparse --- コマンドラインオプション、引数、サブコマンドのパーサー > type](https://docs.python.org/ja/3/library/argparse.html#type)

(*3)  
コマンドラインから受け取った引数は、まず、文字列として受け取る。  
そして、type で指定した型に変換する。
ここで、bool 型を指定すると、引数が指定された場合は常に True になってしまう。
なぜなら、長さ1以上の文字列は常に True になるからである。(文字列の 'False' は、 bool() 関数に渡すと True になる)

***

Pycharm の Run -> Debug でキーワード引数を指定してモジュールを実行するには、 Edit Configurations で、 parameters を指定する。
