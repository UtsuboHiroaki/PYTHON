# クラスとインスタンス

- クラス
    - オブジェクトの雛形
    - インスタンスを生成するための設計図

- インスタンス
    - クラスから生成されたオブジェクト
    - インスタンスはクラスの実体
    - ひとつのクラスから別々の複数のインスタンスを生成できる

「クラス」と「インスタンス」のうち、主役はどちからと言えば、「インスタンス」のほう。  
ということで、まずは、「インスタンス」について説明する。
当初は、「クラス」については、「インスタンス」の説明のための最低限に留める。

ただし、本格的に話をはじめる前に...以下について整理しておきたい。

## 「オブジェクト」なのか「インスタンス」なのか問題

### 先に、結論:

Pythonでは(本講座では)、以下のとおりに言い分ける。

| 名前      | 説明                                 |
|---------|------------------------------------|
| オブジェクト  | Python登場するすべての実体                 |
| インスタンス  | オブジェクトのうち、特に、別途定義されたクラスを元にして作られた実体 |

### 解説

インスタンスとは、クラスから生成されたオブジェクトである。

一方、Pythonでは、すべてのものがオブジェクﾄである。  
文字や数字等のビルトインのオブジェクトをを含めて、あらゆるものが、クラスを元にして作られている。

ということで、以下のとおりに説明してもある意味正しい。

- Pythonでは、すべてのオブジェクトはインスタンスである
- Pythonでは、すべてのインスタンスはオブジェクトである

もっとも、ビルトインのオブジェクトを指して「インスタンス」と呼ぶことはあまりない。

| 分類                       | 「オブジェクト」<br>と称されるか | 「インスタンス」<br>と称されるか |
|--------------------------|--------------------|----------------|
| ビルトインオブジェクト              | ○                  | △              |
| 別途定義されたクラスを元に<br>生成されたオブジェクト | ○                  | ○              |

△: 「インスタンス」ではないのか？といえば、もちろんインスタンス。ただ、そう呼ばれることはあまりなというだけ。

## インスタンスの生成

クラスを呼び出すとインスタンスを生成できる。
クラスを呼び出す都度、別々のインスタンスを生成できる。

インスタンスは、「属性(attribute)」を持つ。
属性は、「メソッド」と「プロパティ」に分類できる。
「メソッド」と「プロパティ」の違いは、「呼び出し可能」かどうか。「呼び出し可能」なのがメソッド。

インスタンスの属性に関係する関数3つ:

| 名前      | 引数                      | 説明                                              |
|---------|-------------------------|-------------------------------------------------|
| setattr | object, name, value     | object に、 name という属性を追加する。その値は value とする        |
| hasattr | object, name            | object に、 name  という属性があるかどうかを boolean 値で返す      |
| getattr | object, name[, default] | object の、 name という属性を取得する。見つからない場合は default を返す |

もっとも、以下のように直接書いてしまってもよい。

| やること      | 書き方(インスタンス内部での記述例)         |
|-----------|----------------------------|
| 設定        | self.name = value          |
| プロパティの取得  | retrun_value = self.name   |
| メソッドの呼び出し | retrun_value = self.name() |

```python
"""
クラスインスタンスの生成時には、クラス内部で __init__ が呼び出される(初期化)

生成されたインスタンスは、クラス内の属性にアクセスできる。
属性とは、「プロパティ」と「メソッド」のこと。
"""
import time
from datetime import datetime


class MyClass:
    def __init__(self, *args, **kwargs):
        """
        インスタンスの生成時に呼ばれる
        """
        for arg in args:
            setattr(self, arg, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_created_datetime(self):
        """
        クラスメソッドの第一引数 self は、クラス自身を指す(呼び出し時には指定しない)
        """
        now_str = self.created.strftime('%Y-%m-%d %H:%M:%S,%f')
        result = f'{self.my_id}の生成時刻は{now_str}です'
        return result


obj1 = MyClass(my_id=1, created=datetime.now())
time.sleep(0.5)
obj2 = MyClass(my_id=2, created=datetime.now())

print(obj1.get_created_datetime())
print(obj2.get_created_datetime())
```

## クラスの継承

クラスは、他のクラスを継承することができる。  
これにより、定義済のクラスを改変して新しいクラスを作ることが可能。

イメージとしては、「哺乳類クラス」を元にして、「ウマクラス」を作るようなもの。

何らかのクラスを継承して作られたクラスのことを、「サブクラス」と言う。

```python
import time
from datetime import datetime


class MyClass:
    def __init__(self, *args, **kwargs):
        for arg in args:
            setattr(self, arg, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_created_datetime(self):
        now_str = self.created.strftime('%Y-%m-%d %H:%M:%S,%f')
        result = f'{self.my_id}の生成時刻は{now_str}です'
        return result


class MySubClass(MyClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_created_datetime(self):
        now_str = self.created.strftime('%Y-%m-%d %H:%M:%S,%f')
        result = f'{self.my_id}の生成時刻は{now_str}です。継承元のメソッドをオーバーライドしています'
        return result


obj1 = MyClass(my_id=1, created=datetime.now())
time.sleep(0.5)
obj2 = MySubClass(my_id=2, created=datetime.now())

print(obj1.get_created_datetime())
print(obj2.get_created_datetime())
```

なお、 isinstance 関数は、オブジェクトが指定したクラスのインスタンスかどうかを判定する。  
このとき、引数に指定したクラスが、継承元のクラスであっても True となる。

```python
class MyClass:
    pass


class MySubClass(MyClass):
    pass


print(isinstance(obj1, MyClass))
print(isinstance(obj1, MySubClass))
```

## クラスの多重継承

クラスの定義時、複数のクラスを多重継承することができる。
これにより、複数のクラスの機能を継承することができる。

イメージとしては、「角クラス」と「羽クラス」と「哺乳類クラス」とを元にして、「ユニコーンクラス」を作るようなもの。

```python
import time
from datetime import datetime


class MyMixin:
    def get_id(self):
        return f'MyMixin: {self.my_id}'


class MyClass:
    def __init__(self, *args, **kwargs):
        for arg in args:
            setattr(self, arg, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_created_datetime(self):
        now_str = self.created.strftime('%Y-%m-%d %H:%M:%S,%f')
        result = f'{self.my_id}の生成時刻は{now_str}です'
        return result


class MySubClass(MyMixin, MyClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_created_datetime(self):
        now_str = self.created.strftime('%Y-%m-%d %H:%M:%S,%f')
        result = f'{self.my_id}の生成時刻は{now_str}です。継承元のメソッドをオーバーライドしています'
        return result


obj1 = MySubClass(my_id=1, created=datetime.now())
time.sleep(0.5)
obj2 = MySubClass(my_id=2, created=datetime.now())

print(obj1.get_created_datetime())
print(obj2.get_created_datetime())

print(obj1.get_id())
print(obj2.get_id())
```







