# callableと引数

## callable とは

- callable (カラブル)とは
    - 「呼び出し可能オブジェクト」のこと  
      [3. データモデル - 3.2. 標準型の階層 - 呼び出し可能型 (callable type)](https://docs.python.org/ja/3/reference/datamodel.html#the-standard-type-hierarchy)

- もうちょっと分かりやすく...
    - オブジェクトの識別子の末尾に () をつけて呼び出せるオブジェクトのこと
        - () 内に引数を指定することもある
        - どんな引数を受け取るかは、その callable の定義による

### callable の具体例

1. 関数の呼び出し
2. クラスメソッドの実行
3. インスタンスの生成
4. インスタンスの呼び出し
5. インスタンスのメソッドの実行

なお、以下、比較のために...「callable」でないオブジェクトの例を挙げてみた。  
文字列, 数値, リスト, タプル, 辞書, ...
                    
***

## callable 呼び出しの例

以下、現段階では読めなくても問題ありません。

### 1. 関数の呼び出し

関数呼び出しの構文。オブジェクトの識別子の末尾に () をつけて呼び出している

```python
def func():
    print('func')
    return 1


result = func()  
```

### 2. クラスメソッドの実行

クラスメソッドの呼び出し。オブジェクトの識別子の末尾に () をつけて呼び出している

```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        print('class method が呼ばれました')

    def __call__(self, **kwargs):
        print('call が呼ばれました')

    def __init__(self, *args, **kwargs):
        print('init が呼ばれました')

    def some_instance_method(self):
        print('instnace method が呼ばれました')


MyClass.some_class_method()
```

### 3. インスタンスの生成

クラスインスタンスの生成時には、クラス内部で __init__ が呼び出される(初期化)

```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        print('class method が呼ばれました')

    def __call__(self, **kwargs):
        print('call が呼ばれました')

    def __init__(self, *args, **kwargs):
        print('init が呼ばれました')

    def some_instance_method(self):
        print('instnace method が呼ばれました')


obj = MyClass()  
```

### 4. インスタンスの呼び出し

クラスインスタンスを呼び出すと、クラス内部で  __call__ が呼び出される

```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        print('class method が呼ばれました')

    def __call__(self, **kwargs):
        print('call が呼ばれました')

    def __init__(self, *args, **kwargs):
        print('init が呼ばれました')

    def some_instance_method(self):
        print('instnace method が呼ばれました')


my_obj = MyClass()

my_obj()  
```

### 5. インスタンスメソッドの実行

```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        print('class method が呼ばれました')

    def __call__(self, **kwargs):
        print('call が呼ばれました')

    def __init__(self, *args, **kwargs):
        print('init が呼ばれました')

    def some_instance_method(self):
        print('instnace method が呼ばれました')


my_obj = MyClass()

# メソッド呼び出しの構文。オブジェクトの識別子の末尾に () をつけて呼びしている
my_obj.some_instance_method()

```

## callable の「引数」

### 引数、仮引数、実引数

呼び出し可能オブジェクトは、呼び出される際に「引数」を受け取ることがある。  
(受け取らないかもしれない。呼び出される側のオブジェクトの定義次第)

```python
def greetings(pre_str, post_str):
    return pre_str + post_str


result = greetings('こんにちは！', 'ごきげんいかがですか？！')
print(result)
```

呼び出される側が受け取る引数を「仮引数(parameter)」と呼ぶ。  
呼び出し側が渡す値を「実引数(argument)」と呼ぶ。

...と書いてはみたがかなり厳密な表現。  
「実引数」、「仮引数」といった言葉が使われることはまずない。  
通常、どちらも「引数」と呼ぶことが多い。

### 位置引数、キーワード引数

引数の名前を指定しない引数、指定する引数を、それぞれ、「位置引数」「キーワード引数」と呼ぶ。

引数の分類

| 分類 | 書き方     |
| ---- |---------|
| 位置引数 | 横並び     |
| キーワード引数 | 引数名=初期値 |

位置引数とキーワード引数を混在させることも可能。  
その場合は、位置引数を先に書く。

以下は、仮引数に位置引数、キーワード引数の両方を使った例

```python
def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


result = opening_greetings('こんにちは！', '12時のニュースの時間です。', date='2020/10/08')
print(result)
```

上の例からも分かるとおり、キーワード引数で、は初期値を設定する。

また、キーワード引数については、呼び出し側から値を渡さなくても良い。    
その場合、定義で指定された初期値が使われる。

### 仮引数が位置引数のとき

位置引数については、呼び出し側は、引数名を明示してもしなくても良い。

以下は、位置引数のみでの実装例

```python
def greetings(pre_str, post_str):
    return pre_str + post_str


result = greetings('こんにちは！', 'ごきげんいかがですか？！')
print(result)
```

位置引数については、呼び出し側は、引数名を「明示してもしなくても良い。」  
つまりは、「しなくてもよい」が、「しても良い」。

以下では、引数名を明示するを紹介する。

```python
def greetings(pre_str, post_str):
    return pre_str + post_str


result = greetings(pre_str='こんにちは！', post_str='ごきげんいかがですか？！')
print(result)
```

引数名を明示した場合は、呼び出し側が引数を渡すときの順序は定義と同じでなくてもよい。

```python
def greetings(pre_str, post_str):
    return pre_str + post_str


result = greetings(post_str='ごきげんいかがですか？！', pre_str='こんにちは！')
print(result)
```

ただし、キーワード引数として渡す引数は、位置引数の後に配置する必要がある。  
以下はNG例。

```python
def greetings(pre_str, post_str):
    return pre_str + post_str

# result = greetings(pre_str='こんにちは！', 'ごきげんいかがですか？！')
# print(result)
```

### 仮引数がキーワード引数のとき

キーワード引数では、定義時に初期値を設定する。(*1)  
キーワード引数については、呼び出し時に値を渡すことを省略できる。

```python
def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


result = weather_news_greetings(date='2020/10/08', area='山陰地方')
print(result)
```

呼び出し側でのキーワード引数の順序を変更しても問題ない。

```python
def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


result = weather_news_greetings(area='中国地方', date='2020/10/10')
print(result)
```

初期値を設定しているキーワード引数は、呼び出し時に値を指定しなくても良い。

```python
def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


result = weather_news_greetings()
print(result)
```

キーワード引数についても、位置引数のような値の渡し方ができないこともない。  
(が、やめておくほうが無難)

```python
def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


result = weather_news_greetings('2020/10/11', '北陸地方')
print(result)
```

(*1) 初期値は、 immutable なものにする。でないと、挙動の制御が難しくなる。(後述)

### 仮引数が位置引数とキーワード引数の両方を含むとき

位置引数とキーワード引数の両方を含む場合は、位置引数を先に記述する。

```python
def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


result = opening_greetings('こんにちは！', '12時のニュースの時間です。', date='2020/10/08', area='甲信越地方')
print(result)
```

仮引数では位置引数とされているものについても、呼び出し時にキーワード引数として渡しても問題ない。  
キーワード引数として渡される引数同士の配置順序は入れ替わっても構わない。

```python
def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


result = opening_greetings(pre_str='こんにちは！', post_str='12時のニュースの時間です。', )
print(result)
```

### キーワード引数の初期値には、イミュータブルな値を指定する (*1)

キーワード引数の初期値には、イミュータブルな値を指定する。  
(イミュータブルな値とは、変更できない値のこと。例えば、数値や文字列、タプルなど)

イミュータブルな値を初期値に指定し、その値を変更するとどうなるか。  
なんと、次回以降の呼び出しでは、変更後の値が初期値となってしまう。

以下は、NG例。

```python
from datetime import datetime


def write_all_list_strings(list_strings=[]):
    print(len(list_strings))
    last_str = '出力日時: ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
    list_strings.append(last_str)
    for list_string in list_strings:
        print(list_string)
    print('出力を終了しました\n')


write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
```

以下は、解決先の例。None型等のイミュータブルな値を初期値に指定する。

```python
from datetime import datetime


def write_all_list_strings(list_strings=None):
    if list_strings is None:
        list_strings = []

    print(len(list_strings))
    last_str = '出力日時: ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
    list_strings.append(last_str)
    for list_string in list_strings:
        print(list_string)
    print('出力を終了しました\n')


write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
write_all_list_strings()
```

## アンパック

アンパックという手法で、リストやタプル等、あるいは辞書等を引数に変換することができる。

### 実引数のアンパック

実引数にアスタリスクを1つ付けると、リストの要素をアンパックして、複数の実引数に変換できる。

```python
def greetings(pre_str, post_str):
    return pre_str + post_str


my_list = ['こんにちは！', 'ごきげんいかがですか？！']
result = greetings(*my_list)
print(result)
```

実引数にアスタリスクを2つ付けると、辞書のキーと値をアンパックして、複数のキーワード引数に変換できる。

```python
def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


my_dict = {
    'date': '2020/10/11',
    'area': '北陸地方',
}
result = weather_news_greetings(**my_dict)
print(result)
```

以下は、両者を組み合わせた例。

```python
def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


my_list = ['こんにちは！', 'ごきげんいかがですか？！']
my_dict = {
    'date': '2020/10/11',
    'area': '北陸地方',
}
result = opening_greetings(*my_list, **my_dict)
print(result)
```

### 仮引数のアンパック

仮引数にアスタリスクを1つ付けると、引数をタプルとして受け取ることができる。

```python
def greetings(*args):
    return args[0] + args[1]


result = greetings('こんにちは！', 'ごきげんいかがですか？！')
print(result)
```

仮引数にアスタリスクを2つ付けると、アンパックされた複数の引数を受け取ることができる。

```python
def weather_news_greetings(**kwargs):
    return f'これから、{kwargs["date"]}の{kwargs["area"]}の天気予報をお伝えします。'


result = weather_news_greetings(date='2020/10/11', area='北陸地方')
print(result)
```

以下は、両者を組み合わせた例。

```python
def opening_greetings(*args, **kwargs):
    return f'{args[0]}{args[1]}それではこれから、{kwargs["date"]}の{kwargs["area"]}の天気予報をお伝えします。'


result = opening_greetings('こんにちは！', 'ごきげんいかがですか？！', date='2020/10/11', area='北陸地方')
print(result)
```

アンパックはかなり強力な手法で、慣れてしまえばかなりの助けになる。

#### 位置引数、キーワード引数、アンパックを組み合わせた例

なお、最終形態は、以下のような、「arg1, arg2, *args, key1=value, key2=value2, **kwargs」という形態。

すぐに理解できなくて良いが、以下のような記述もできる。  
自分で書くことは当面ないだろうが、見かけることはあるかもしれない。

ここまでに紹介してきた引数設定の仕方、引数の渡し方のいずれも、以下のより簡易なパターンにしかすぎない。  
なので、以下を理解できれば、この「callable の『引数』」の項での学習は完了と言える。

```python
def full_stack_openings(pre_str, post_str, *args, date='2020/10/07', area='関東地方', **kwargs):
    print(pre_str + post_str)
    if args:
        print('\nはじめに、季節の話題です。')
        for arg in args:
            print(arg)
    if kwargs:
        print('\n最初に、警報と注意報をお伝えします。')
    if kwargs.get('danger'):
        print('警報をお知らせします。')
        print(kwargs.get('danger'))
    if kwargs.get('warning'):
        print('注意報をお知らせします。')
        print(kwargs.get('warning'))

    print(f'\nそれでは、これから、{date}の{area}の天気予報をお伝えします。')


full_stack_openings('おはようございます。', '天気予報の時間です。',

                    # 以下の文字列は、すべて、 args にリストとして入る
                    '秋も深まり、長野県の◯◯村では、ぶどうの収穫が最盛期です。',
                    '東京や名古屋からぶどう狩りに来る観光客もたくさんいます。',
                    'さっそく、取材映像をご覧いただきましょう。',
                    'この品種のぶどうは、ほかの品種に比べて収穫時期が遅いそうです。',
                    '来週いっぱいまでは紅葉を楽しめるだろうということです。',

                    date='2020/10/11', area='九州地方',

                    # 以下の2つは、 kwargs に辞書として入る
                    danger='東北地方に強風警報がでています',
                    warning='北海道に大雪注意報がでています'
                    )
```

```python
def full_stack_openings(pre_str, post_str, *args, date='2020/10/07', area='関東地方', **kwargs):
    print(pre_str + post_str)
    if args:
        print('\nはじめに、季節の話題です。')
        for arg in args:
            print(arg)
    if kwargs:
        print('\n最初に、警報と注意報をお伝えします。')
    if kwargs.get('danger'):
        print('警報をお知らせします。')
        print(kwargs.get('danger'))
    if kwargs.get('warning'):
        print('注意報をお知らせします。')
        print(kwargs.get('warning'))

    print(f'\nそれでは、これから、{date}の{area}の天気予報をお伝えします。')


info_list = [
    'おはようございます。',
    '天気予報の時間です。'
    '秋も深まり、長野県の◯◯村では、ぶどうの収穫が最盛期です。',
    '東京や名古屋からぶどう狩りに来る観光客もたくさんいます。',
    'さっそく、取材映像をご覧いただきましょう。',
    'この品種のぶどうは、ほかの品種に比べて収穫時期が遅いそうです。',
    '来週いっぱいまでは紅葉を楽しめるだろうということです。',
]
cautions = {
    'danger': '東北地方に強風警報がでています',
    'warning': '北海道に大雪注意報がでています',
    'date': '2020/10/11',
}

full_stack_openings(*info_list, **cautions)
```

### callableの引数として、関数等を渡すことができる。

最後に、callable が引数として関数を受け取ることができるということにも触れておく。

以下では、関数の引数として、関数を渡している。

```python
def show_greetings():
    print('こんにちは。')


def show_program_title():
    print('お昼のニュースの時間です。')


def print_first_message(func1, func2):
    func1()
    func2()


print_first_message(show_greetings, show_program_title)
```

以下では、引数を受け取る関数と、内部で呼び出される各関数が受け取るべきき引数を print_first_message に渡している。

```python
def show_greetings(message):
    print(message)


def show_program_title(title):
    print(title)


def print_first_message(func1, func2, message, title):
    func1(message)
    func2(title)


print_first_message(show_greetings, show_program_title, 'こんばんは。', '夜のニュースの時間です。')
```

以下では、第一引数に関数、第二引数に、その関数に渡す引数をリストとして渡している。

```python
def average(args):
    return sum(args) / len(args)


def execute_func(func, args):
    return func(args)


base_list = [7, 1, 3, 5, 4]

result = execute_func(sum, base_list)
print(result)

result = execute_func(len, base_list)
print(result)

result = execute_func(max, base_list)
print(result)

result = execute_func(min, base_list)
print(result)

result = execute_func(average, base_list)
print(result)
```