# 例外

例外を使うことの利点:

1. 例外のタイプによって処理を切り分けられる
2. 呼び出した関数やメソッド内での例外発生にも対応できる
3. 独自に例外を定義できる

すべての例外は、 BaseException クラスのサブクラス。

[組み込み例外](https://docs.python.org/ja/3/library/exceptions.html)

## 例外の発生

```python
raise Exception('例外のメッセージ')
```

```python
def calc_except_three(n):
    """
    3以外の値を受け取って2倍した値を返す
    3を受け取ったときは ValueError
    """
    if n == 3:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    return n * 2


print(calc_except_three(3))
```

以下のような処理でも、裏で raise が呼ばれているということイメージできるだろうか。

```python
value = 5 / 0  # ZeroDivisionError: division by zero
```

## 例外の捕捉

```python
try:
    # 例外が発生する可能性のある処理
    pass
except Exception as e:
    # 例外が発生したときの処理
    pass
else:
    # 例外が発生しなかったときの処理
    pass
finally:
    # 例外の有無に関わらず、必ず実行する処理
    pass
```

実際には、以下のように、より具体的な例外を捕捉することが多い。

```python
try:
    # 例外が発生する可能性のある処理
    pass
except ValueError as e:
    # ValueError が発生したときの処理
    pass
except ZeroDivisionError as e:
    # ZeroDivisionError が発生したときの処理
    pass
except Exception as e:
    # その他の例外が発生したときの処理
    pass
else:
    # 例外が発生しなかったときの処理
    pass
finally:
    # 例外の有無に関わらず、必ず実行する処理
    pass
```

上記に従って、もう少し実装してみよう

```python
def calc_except_thirty(n, divide_by):
    """
    :n: 30以外の数値を受け取る
    :divide_by: 0以外の数値を受け取る
    """
    if n == 30:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    return n / divide_by


try:
    result = calc_except_thirty(10, 3)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print('finally は必ず実行されます')
```

## 独自の例外を定義する

上達すると、独自の例外を定義して処理したくなる。  
独自の例外を定義するには、 Exception クラス等、既存の例外クラスで機能の近そうなものを継承する。

以下では、非常に簡単な例として、文字列を受け取ったときには独自の例外を発生させるようにしてみる。

```python
class StrValueException(ValueError):
    def __init__(self, value):
        self.message = '文字列は受けつけられません: ' + value


def calc_except_thirty(n, divide_by):
    """
    :n: 30以外の数値を受け取る
    :divide_by: 0以外の数値を受け取る
    """
    if isinstance(n, str):
        raise StrValueException(n)

    if n == 30:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    return n / divide_by


try:
    result = calc_except_thirty('毎月10日は経理の締めの日です', 3)
except StrValueException as e:
    print(e.message)
```

StrValueException は、 ValueError を継承しているので、 ValueError と同じように捕捉できる。  
(ただし、もちろん、より精度の高い例外処理のためには、継承クラスを指定するほうが望ましい)

```python
class StrValueException(ValueError):
    def __init__(self, value):
        self.message = '文字列は受けつけられません: ' + value


def calc_except_thirty(n, divide_by):
    """
    :n: 30以外の数値を受け取る
    :divide_by: 0以外の数値を受け取る
    """
    if isinstance(n, str):
        raise StrValueException(n)

    if n == 30:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    return n / divide_by


try:
    result = calc_except_thirty('毎月10日は経理の締めの日です', 3)
except ValueError as e:  # StrValueException は ValueError を継承しているので、これでも捕捉できる
    print(e.message)
```

