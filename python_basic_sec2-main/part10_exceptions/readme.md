# 例外 exceptions

## 前提-エラーの分類

| 分類 | 説明                          | メモ                      |
|--------|-----------------------------|-------------------------|
| 構文エラー  | プログラムの構文が間違っている場合。          | そもそも実行できない。             |
| 実行時エラー | プログラムの実行中に発生したエラー。 | 中断される or 想定内ならばハンドルされる。 |
| 論理エラー  | プログラムは実行完了するが、得られた結果がおかしい場合 | いちおう実行完了する。             |

ここで、例外処理は、「想定内の実行時エラーをハンドル(*)するための仕組み」である。

(*)「ハンドルする」とは、「捕まえて処理する」というようなニュアンスの言葉

### メモ:

一般論としては、論理エラーよりも、実行時エラーの方が、より早く発見できる分好ましい。  
また、実行時エラーよりも、構文エラーの方が、より早く発見できる分好ましい。

最悪なのは、気づくのが困難な「論理エラー」。  
これは、テストコードを書いて発見するか、テストコードで検証できなかった部分については、実運用を通じて実績を信頼の担保とするよりない。  
しかし、「実績を信頼の担保とする」というようでは、「機密性」（Confidentiality）、「完全性」（Integrity）、「可用性」（Availability）の情報セキュリティの3要素を担保するには、心許ない。

***

## 例外を自在に活用できるようになるためのポイント

- 実行時エラーを発生させるのは、 `raise` 文。引数は、例外クラスか、例外クラスのインスタンス  
  例外クラスは、 `Exception` クラスを継承している
- 例外をハンドルする構文は、`try` - `except` 構文。  
  `except` 節で、例外クラスを指定する
- Pythonには、あらかじめ、多くの例外クラスが用意されている  
  独自の例外を定義することもできる

***

## 例外を発生させる

### 例外を発生させ、例外発生時の出力を読んでみる

例外を発生させ、例外発生時の出力を読んでみる。

以下では、組み込みの `ValueError` 例外を発生させる。  
引数には、 `ValueError` クラスを指定している。

part10_01_raise_class.py

```python
value = 200

if value > 100:
    raise ValueError

print("raise文の後の処理は実行されません。")
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_01_raise_class.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_01_raise_class.py", line 4, in <module>
    raise ValueError
ValueError

Process finished with exit code 1
```

***

以下では、組み込みの `ValueError` 例外を発生させる。  
引数には、 `ValueError` クラスのインスタンスを指定している。

part10_02_raise_instance.py

```python
value = 200

if value > 100:
    raise ValueError('value の値は 100 以下にしてください。')

print("raise文の後の処理は実行されません。")
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_02_raise_instance.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_02_raise_instance.py", line 4, in <module>
    raise ValueError('value の値は 100 以下にしてください。')
ValueError: value の値は 100 以下にしてください。

Process finished with exit code 1
```

***

Pythonインタープリターが例外を raise する場合もある。

以下では、0での除算を試みる。  
すると、Pythonインタープリターは、組み込みの `ZeroDivisionError` 例外を発生させる。

part10_03_divide_by_zero.py

```python
result = 5 / 0

print("raise文の後の処理は実行されません。")
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_03_divide_by_zero.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_03_divide_by_zero.py", line 1, in <module>
    result = 5 / 0
ZeroDivisionError: division by zero

Process finished with exit code 1
```

***

以下では、カラブルでないオブジェクトを呼びそうとすることで、組み込みの `TypeError` 例外を発生させる。

part10_04_not_callable.py

```python
moji = "hoge"
result = moji()

print("raise文の後の処理は実行されません。")
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_04_not_callable.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_04_not_callable.py", line 2, in <module>
    result = moji()
TypeError: 'str' object is not callable

Process finished with exit code 1
```

***

以下では、ビルトインの datetime モジュール内で、組み込みの `TypeError` 例外を発生させる。

part10_05_excption_in_builtins.py

```python
from datetime import date, timedelta

dt = date(2022, 11, 15)
td = timedelta(seconds=12)

new_dt = td * dt
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_13_excption_in_builtins.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_13_excption_in_builtins.py", line 7, in <module>
    new_dt = td * dt
TypeError: unsupported operand type(s) for *: 'datetime.timedelta' and 'datetime.date'

Process finished with exit code 1
```

### より複雑なトレースバック

カラブルやモジュールをまたがる処理で例外が発生した場合、トレースバックには、一連の呼び出しの流れが出力される。  
このトレースバックは、プログラムをデバッグする際の重要な情報。

以下では、複数の関数をまたがった処理内で例外が発生している。

part10_11_call_and_exception.py

```python
def func_a():
    return 1 / 0


def func_b():
    return func_a()


def func_c():
    return func_b()


if __name__ == '__main__':
    func_c()
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_11_call_and_exception.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_11_call_and_exception.py", line 14, in <module>
    func_c()
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_11_call_and_exception.py", line 10, in func_c
    return func_b()
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_11_call_and_exception.py", line 6, in func_b
    return func_a()
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_11_call_and_exception.py", line 2, in func_a
    return 1 / 0
ZeroDivisionError: division by zero

Process finished with exit code 1
```

***

以下では、別モジュール内での処理中に例外が発生している。

sub/another_module.py

```python
def func_x():
    return 1 / 0


def func_y():
    return func_x()


def func_z():
    return func_y()
```

part10_12_module_and_exception.py

```python
from sub.another_module import func_z

if __name__ == '__main__':
    func_z()
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_12_module_and_exception.py 
Traceback (most recent call last):
  File "D:\projects\python_basic_sec2\part10_exceptions\part10_12_module_and_exception.py", line 4, in <module>
    func_z()
  File "D:\projects\python_basic_sec2\part10_exceptions\sub\another_module.py", line 10, in func_z
    return func_y()
  File "D:\projects\python_basic_sec2\part10_exceptions\sub\another_module.py", line 6, in func_y
    return func_x()
  File "D:\projects\python_basic_sec2\part10_exceptions\sub\another_module.py", line 2, in func_x
    return 1 / 0
ZeroDivisionError: division by zero

Process finished with exit code 1
```

***

### 【重要】 Traceback は、必ず読むこと！

実行時エラーでプログラムが強制終了したら、必ず Traceback を読むこと。

前述のとおり、カラブルやモジュールをまたがる処理で例外が発生した場合、トレースバックには、一連の呼び出しの流れが出力される。  
このトレースバックは、プログラムをデバッグする際の重要な情報。

Traceback を読む習慣をつけることは、プログラミング上達には極めて大切。  
例外が発生したときに、どのような経緯で発生したのか、どのようなエラーが発生したのかを追いかけることができる。

また、自分の原因が自分で判別できなくて人に支援を求める場合も、 Traceback を提供することが大切。  
(Traceback がないと、支援を求められた側も、原因を判別することができない)

***

## 例外クラス exception classes

例外の正体は、 Exception クラスを継承したクラスインスタンス。  
以下に、組み込み例外の階層構造図を示す。

[組み込み例外 - 例外のクラス階層](https://docs.python.org/ja/3/library/exceptions.html#exception-hierarchy)

***

## 例外処理 exception handling

`try` ... `except` ... `else` ... `finally` 構文によって、事前に想定された例外をハンドリングできる。

```python
try:
    # 例外が発生する可能性のある処理
    a + b
except SomeException:
    # SomeException 例外が発生した場合の処理
    print('SomeException 例外が発生しました。')
except SomeAnotherException:
    # SomeAnotherException 例外が発生した場合の処理
    print('SomeAnotherException 例外が発生しました。')
except:
    # SomeException でも SomeAnotherException でもない例外が発生した場合の処理
    print('想定外の例外が発生しました。')
else:
    # 例外が発生しなかった場合の処理
    print('例外は発生しませんでした。')
finally:
    # 例外の有無に関わらず、必ず実行する処理
    print('処理を終了します。')
```

例外が `except` 節内でハンドリングされた場合は、finally 節が実行されたのち、以降の処理がひきつづき実行される。

以下に例を示す。

part10_21_handle_exception.py

```python
a = 100
b = 0

try:
    result = a / b
except ZeroDivisionError as e:  # 例外オブジェクトを e に代入
    print(isinstance(e, ZeroDivisionError))  # True
    print(e)  # e.__str__() の結果
    print('ZeroDivisionError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm 2022.2.1/plugins/python/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto --client 127.0.0.1 --port 57185 --file D:/projects/python_basic_sec2/part10_exceptions/part10_21_handle_exception.py 
True
division by zero
ZeroDivisionError 例外をハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
```

***

例外は、発生した例外クラスの親クラスでもハンドルできる。

part10_22_handle_exception_base_class.py

```python
a = 100
b = 0

try:
    result = a / b
except ArithmeticError as e:  # ArithmeticError は、ZeroDivisionError の親クラス
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, ArithmeticError))  # True
    print(e)  # e.__str__() の結果
    print('ArithmeticError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_22_handle_exception_base_class.py 
True
True
division by zero
ArithmeticError 例外をハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
```

***

記述のとおり、例外は、`Exception` クラスを継承したクラス。  
なので、`Exception` クラスであらゆる例外をハンドルできる。

part10_23_handle_exception_class.py

```python
a = 100
b = 0

try:
    result = a / b
except Exception as e:  # Exception は、すべての例外の親クラス
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, ArithmeticError))  # True
    print(isinstance(e, Exception))  # True
    print(e)  # e.__str__() の結果
    print('Exceptionをハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_23_handle_exception_class.py 
True
True
True
division by zero
Exceptionをハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
```

もっとも、すべての例外を安易にハンドルするのは、あまり良い考えではない。

想定内の例外はハンドルされても良い。  
しかし、想定外の例外については、内々に処理されてしまうより、異常終了したほうが好ましい。  
なぜなら、「想定外の事態が発生したのに異常終了しない」とは、「実行時エラーで済むはずだったものが、論理エラーになってしまった」ということだから。

***

複数の例外のいずれかをハンドルしたいならば、以下のように書く。

part10_24_handle_multiple_exceptions.py

```python
a = 100
b = 0
c = 'moji'
d = [1, 2, 3]

try:
    result = a / b
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
    print('ZeroDivisionError 例外をハンドルしました')
except TypeError as e:
    print(isinstance(e, TypeError))
    print(e)
    print('TypeError 例外をハンドルしました')
except Exception as e:
    print(isinstance(e, Exception))
    print(e)
    print('Exceptionをハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_24_handle_exceptions.py 
True
division by zero
ZeroDivisionError 例外をハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
````

***

「いくつかの型の例外については同じ処理で良い」ということであれば、以下のような書き方でも良い。

part10_25_handle_multiple_exceptions.py

```python
a = 100
b = 0

try:
    result = a / b
except (ZeroDivisionError, TypeError) as e:
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, TypeError))  # True
    print(e)  # e.__str__() の結果
    print('ZeroDivisionError または TypeError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_25_handle_multiple_exceptions.py 
True
False
division by zero
ZeroDivisionError または TypeError 例外をハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
```

***

例外が発生したのが呼び出したカラブルや別モジュール内であってもハンドルできる。

part10_26_handle_another_module_exception.py

```python
from sub.another_module import func_z

try:
    func_z()
except ZeroDivisionError as e:
    print(e)
    print('ZeroDivisionError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
```

```shell
D:\projects\python_basic_sec2\venv\Scripts\python.exe D:/projects/python_basic_sec2/part10_exceptions/part10_26_handle_another_module_exception.py 
division by zero
ZeroDivisionError 例外をハンドルしました
処理を終了します
try ... except ... else ... finally の一連のプロックから抜けました

Process finished with exit code 0
```

***

## 独自の例外を定義する

Exception クラスのサブクラスを自分で作ることもできる。    
新たに例外クラスを定義するには、既存の例外クラスで機能の近そうなものを継承するのが良い。  
(継承する親クラスによって、例外インスタンス生成時に受け取る引数が異なることがあるので注意！)

以下では、日付を検証して、一定の条件に合致するものの場合には独自の例外を発生させる。

part10_31_original_exception.py

```python
import datetime


class DateError(ValueError):
    def __init__(self, message, date):
        self.message = message
        self.date = date
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.date.strftime("%Y/%m/%d")}'


def set_execute_day(task, day):
    """
    仕事を実行する日を設定する。

    ただし、以下のいずれかに合致する日を指定された場合は例外を発生して拒絶する
        - 過去の日付
        - 休日
        - 5, 10日

    :param task: 実行する仕事
    :param day: 実行予定日
    :return: 「必ず実行する」というお約束のお返事
    """
    if day < datetime.date.today():
        raise DateError('過去の日付は指定できません', day)

    if day.weekday() in [5, 6]:
        raise DateError('平日ではありません', day)

    if day.day % 5 == 0:
        raise DateError('5, 10日は忙しいので無理です', day)

    return f'{task} を {day.strftime("%Y/%m/%d")} に必ず実行するとお約束します！'


try:
    result = set_execute_day('月次決算をとりまとめる仕事', datetime.date(2022, 11, 12))
except DateError as e:
    print(e)
else:
    print(result)
```

なお、今回の例では、いずれの例外も ValueError を継承している。  
なので、 ValueError で補足することもできる。

ただし、もちろん、より精度の高い例外処理のためには、継承クラスを指定するほうが望ましい。

***

ところで、`PastDayError`、`NotWeekDayError`、`FiveTenDayError` は性質が似ている。  
そこで、 `ValueError` を継承したこれらの親クラスを作ってリライトしてみた。

part10_32_date_exception.py

```python
import datetime


class DateError(ValueError):
    def __init__(self, message, date):
        self.message = message
        self.date = date
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.date.strftime("%Y/%m/%d")}'


class PastDateError(DateError):
    def __init__(self, day):
        super().__init__('過去の日付は指定できません', day)


class NotWeekDayDateError(DateError):
    def __init__(self, day):
        super().__init__('平日ではありません', day)


class FiveTenDayDateError(DateError):
    def __init__(self, day):
        super().__init__('5, 10日は忙しいので無理です', day)


def set_execute_day(task, day):
    """
    仕事を実行する日を設定する。

    ただし、以下のいずれかに合致する日を指定された場合は例外を発生して拒絶する
        - 過去の日付
        - 休日
        - 5, 10日

    :param task: 実行する仕事
    :param day: 実行予定日
    :return: 「必ず実行する」というお約束のお返事
    """
    if day < datetime.date.today():
        raise PastDateError(day)

    if day.weekday() in [5, 6]:
        raise NotWeekDayDateError(day)

    if day.day % 5 == 0:
        raise FiveTenDayDateError(day)

    return f'{task} を {day.strftime("%Y/%m/%d")} に必ず実行するとお約束します！'


try:
    result = set_execute_day('月次決算をまとめる仕事', datetime.date(2022, 11, 12))
except PastDateError as e:
    print(e)
except NotWeekDayDateError as e:
    print(e)
except FiveTenDayDateError as e:
    print(e)
else:
    print(result)
```

***

`PastDayError`、`NotWeekDayError`、`FiveTenDayError` のいずれも、`DayError` を継承している。  
なので、以下の書き方でも当然例外をハンドルできる。  
(せっかく別クラスにしたのにあえて親クラスでハンドルする意味はないが、クラスや例外についての理解を深めるためにあえて記載)

```python
try:
    result = set_execute_day('月次決算をまとめる仕事', datetime.date(2022, 11, 12))
except DateError as e:
    print(e)
else:
    print(result)
```

## そのほか

### except 節の中で別の例外を発生させる

raise 文を補定した except 節の中で別の例外を raise させることもできる。  
[8. エラーと例外 - 8.5. 例外の連鎖](https://docs.python.org/ja/3/tutorial/errors.html#exception-chaining)

## まとめ

- 実行時エラーを発生させるのは、 `raise` 文。引数は、例外クラスか、例外クラスのインスタンス  
  例外クラスは、 `Exception` クラスを継承している
- 例外をハンドルする構文は、`try` - `except` 構文。  
  `except` 節で、例外クラスを指定する
- Pythonには、あらかじめ、多くの例外クラスが用意されている  
  独自の例外を定義することもできる

