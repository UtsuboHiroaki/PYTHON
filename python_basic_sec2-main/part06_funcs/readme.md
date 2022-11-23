# 関数

関数は、別のプログラムから呼び出されてなんらかの処理を行うオブジェクト。  
「処理」とは、大きく分けて以下の2つ。

|処理| 説明                                        |
|----|-------------------------------------------|
|破壊的変更を行う| 関数の外側の変数等の内容を変更する。「副作用を持つ」というような言われ方もされる。 |
|戻り値を返す| return 文で値を返す。                            |

関数に限らず、 callable であれば、上記の少なくともいずれかの処理を行う場合がほとんど。

1. 破壊的変更を行い、戻り値は返さない関数の例:

```python
# 以下の関数は、リストのすべての要素を2倍にしている
def double_list_items(my_list):
    """
    リストのすべての要素を2倍にする
    """
    for i in range(len(my_list)):
        my_list[i] *= 2


base_list = [7, 1, 3, 5, 4]

double_list_items(base_list)
print(base_list)  # リストの内容は破壊的に変更されている
```

2. 破壊的変更を行わず、戻り値を返す例:

```python
# 以下の関数は、リストのすべての要素の2倍を合計した値を返す
def sum_list(my_list):
    """
    リストのすべての要素の2倍を合計した値を返す
    """
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i] * 2
    return sum


base_list = [7, 1, 3, 5, 4]

result = sum_list(base_list)
print(result)  # 戻り値を得られる

print(base_list)  # リストの内容は変更されていない
```

3. 破壊的変更を行い、戻り値も返す例:

```python
def double_list_items(my_list):
    """
    リストのすべての要素を2倍にする
    完了したら「完了しました」という文字列を返す
    """
    for i in range(len(my_list)):
        my_list[i] *= 2

    return '完了しました'


base_list = [7, 1, 3, 5, 4]

result = double_list_items(base_list)
print(result)  # 戻り値を得られる
print(base_list)  # リストの内容は破壊的に変更されている
```

4. 破壊的変更を行わず、戻り値も返さない」例:

```python
# 以下の関数は、リストのすべての要素をコンソールに出力する
def print_list(my_list):
    """
    リストのすべての要素をコンソールに出力する
    """
    for i in range(len(my_list)):
        print(my_list[i])


base_list = [7, 1, 3, 5, 4]

print_list(base_list)  # リストの内容は変更されていない

```

## 関数の定義と呼び出し

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
```

関数定義のポイントは以下の通り。

- 関数名は、変数名と同様に、アルファベット、数字、アンダースコアのみで構成される。(snake_case で記述する) (*1)
    - 別モジュールから呼び出させるつもりがない場合は、関数名の先頭にアンダースコアを付けてもよい。 (*2)
- 引数は、関数に渡される値。引数は、0個以上指定できる。
- 引数には、位置引数とキーワード引数の2種類がある。
- 関数の定義では、位置引数は、キーワード引数より前に書かなければならない。

***

## より高度な関数の機能

以下は、やや高度です。  
最初は仕組みの理解が追いつかなくても良いので、まずは、結果だけ受け入れてください。

「同様の実装をできるようになる」というのは、半年くらい先になってもおかしくありません。  
とはいえ、人が書いたコードではちょこちょこ登場するので、見かけたときにびっくりしないようにという意味で紹介します。

ポイント:

1. 関数の引数として、関数等を渡すことができる。
2. 関数の戻り値として、関数を返すことができる。
3. 関数内に関数を記述することができる。

### 1. 関数の引数として、関数等を渡すことができる。

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

### 2. 関数の戻り値として、関数を返すことができる

以下では、関数の戻り値として、関数を返している。

```python
def get_func_to_use(func_name):
    """
    受け取った文字列によって、返す関数を変える
    """
    if func_name == 's':
        return sum
    elif func_name == 'x':
        return max
    elif func_name == 'n':
        return min
    else:
        return len


base_list = [7, 1, 3, 5, 4]

func = get_func_to_use('s')
result = func(base_list)
print(result)

func = get_func_to_use('x')
result = func(base_list)
print(result)

func = get_func_to_use('n')
result = func(base_list)
print(result)

func = get_func_to_use('z')
result = func(base_list)
print(result)
```

### 3. 関数内に関数を記述することができる

```python
def print_first_message():
    def show_greetings():
        print('こんにちは。')

    def show_program_title():
        print('お昼のニュースの時間です。')

    show_greetings()
    show_program_title()


print_first_message()
```

以下では、引数を受け取る関数と、関数に渡すべき引数を print_first_message に渡している。

```python
def print_first_message(message, title):
    def show_greetings(_message):
        print(_message)

    def show_program_title(_title):
        print(_title)

    show_greetings(message)
    show_program_title(title)


print_first_message('こんばんは。', '夜のニュースの時間です。')
```

## デコレータ

「関数を加工して、機能追加した別の関数を作りたい」という場合がある。  
たとえば、ある関数の前後に開始、終了の出力をしたいとする。

これを、以下のように、「デコレータ」によって簡易に記述できる。

```python
def print_timestamp(func):
    def wrapper():
        print('天気予報を開始します。')
        print('現在時刻は、2020/10/07 12:00:00 です。')

        func()

        print('現在時刻は、2020/10/07 12:00:01 です。')
        print('天気予報完了までにかかった時間は1秒でした。')

    return wrapper


@print_timestamp
def show_weather_info():
    print('\t昨日の天気は、晴れでした。')
    print('\t今日の天気は、晴れです。')
    print('\t明日の天気は、くもりです。')
    print('\t明後日の天気は、雨です。')


show_weather_info()
```

上に紹介したものをデコレータを使わないで書くと、以下のようになる。

```python
def print_timestamp(func):
    def wrapper():
        print('天気予報を開始します。')
        print('現在時刻は、2020/10/07 12:00:00 です。')

        func()

        print('現在時刻は、2020/10/07 12:00:01 です。')
        print('天気予報完了までにかかった時間は1秒でした。')

    return wrapper


def show_weather_info():
    print('\t昨日の天気は、晴れでした。')
    print('\t今日の天気は、晴れです。')
    print('\t明日の天気は、くもりです。')
    print('\t明後日の天気は、雨です。')


show_weather_info = print_timestamp(show_weather_info)  # 元の関数 show_weather_info は上書きされる

show_weather_info()
```

「横に並べると長くなるので、縦に書いた。縦に書くときは、 @func_name と書くのだ」と、やや乱暴だが、そんな理解で良いかと。

## 無名関数

### 「関数名」のない関数を定義することができる

lamba 式とも呼ばれる。  
中学で学んだ、以下のような関数の書き方のイメージ:  
```f(x, y) = 5 * x + 4 * y + 2```

上記を lambda 式で書くと以下のようになる。

```python
lambda x, y: 5 * x + 4 * y + 2
```

用途としては、リスト等のイテラブルの各要素に対して、関数を適用する場合などに使う。

たとえば、以下では、リストの各要素を id の値で並べ替えている。

```python
base_list = [
    {'id': 3, 'name': '山田', 'score': 50},
    {'id': 1, 'name': '田中', 'score': 90},
    {'id': 2, 'name': '鈴木', 'score': 70},
    {'id': 4, 'name': '佐藤', 'score': 60},
    {'id': 5, 'name': '高橋', 'score': 80},
]

new_list = sorted(base_list, key=lambda x: x['id'])
print(new_list)
```

上記の lambda 式を def で定義した関数で書くと以下のようになる。

```python
def get_id(x):
    return x['id']


base_list = [
    {'id': 3, 'name': '山田', 'score': 50},
    {'id': 1, 'name': '田中', 'score': 90},
    {'id': 2, 'name': '鈴木', 'score': 70},
    {'id': 4, 'name': '佐藤', 'score': 60},
    {'id': 5, 'name': '高橋', 'score': 80},
]

new_list = sorted(base_list, key=get_id)
print(new_list)
```

以下では、リストの各要素を2倍した新しいリストを作成している。

```python
base_list = [
    {'id': 3, 'name': '山田', 'score': 50},
    {'id': 1, 'name': '田中', 'score': 90},
    {'id': 2, 'name': '鈴木', 'score': 70},
    {'id': 4, 'name': '佐藤', 'score': 60},
    {'id': 5, 'name': '高橋', 'score': 80},
]

filter_result = filter(lambda x: x['score'] > 60, base_list)
new_list = list(filter_result)
print(new_list)
```

上に紹介したものを def で定義した関数で書くと以下のようになる。

```python
def is_over_60(x):
    return x['score'] > 60


base_list = [
    {'id': 3, 'name': '山田', 'score': 50},
    {'id': 1, 'name': '田中', 'score': 90},
    {'id': 2, 'name': '鈴木', 'score': 70},
    {'id': 4, 'name': '佐藤', 'score': 60},
    {'id': 5, 'name': '高橋', 'score': 80},
]

filter_result = filter(is_over_60, base_list)
new_list = list(filter_result)
print(new_list)
```
