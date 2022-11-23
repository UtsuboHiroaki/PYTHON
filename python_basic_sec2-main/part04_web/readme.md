# ウェブからのデータ取得

## 全体の流れ:

1. ウェブサーバに対して「リクエスト」を発行し、ウェブサーバから「レスポンス」を受け取る。
2. レスポンスの「ステータスコード」から、正常にデータを受け取れたことを確認する。
3. レスポンスの「レスポンスボディ」を取得する。
4. レスポンスボディの内容を、適切なライブラリを使って処理する。

以下は、一連の処理の例:

```python
import json
import requests

url = 'https://flask.pc5bai.com/metal/api/info/gold/'
response = requests.get(url)
if response.status_code != 200:  # ステータスコードが200であることを確認する
    print(response.status_code)
    exit(1)

result_dict = json.loads(response.text)  # jsonデータを辞書型に変換する

print(result_dict['metal_type'], result_dict['buy'], result_dict['sell'], )
```

***

### 「レスポンス」の基本構成

サーバは、リクエストに対し、レスポンスを返す。  
レスポンスは、以下の構成を取る。(ウェブからのデータ取得に特に関係するもののみまずは紹介)

- レスポンスヘッダー
    - 「ステータスコード」を含む。   
      ステータスコードは、 ```response.status_code``` で取得できる。

- レスポンスボディ
    - これの中身を解析する。  
      レスポンスボディは、 ```response.text``` で文字列として取得できる。 

#### ステータスコード

「ステータスコード」は、大きく分けて、以下のとおりに分類できる。

| 分類                                                        | 概要        | メモ                                    |
|-----------------------------------------------------------|-----------|---------------------------------------|
| [100番台](https://httpwg.org/specs/rfc9110.html#status.1xx) | 処理中       | まず見ない...というか、見たことないです。            | 
| [200番台](https://httpwg.org/specs/rfc9110.html#status.2xx) | 正常に処理された  | 200番台なら解析を行ってよい                       | 
| [300番台](https://httpwg.org/specs/rfc9110.html#status.3xx) | 転送        | レスポンスヘッダー内に記載の転送先を調べ、改めてそのページにリクエストする | 
| [400番台](https://httpwg.org/specs/rfc9110.html#status.4xx) | クライアントエラー | リクエスト内容が不正なので却下された                    | 
| [500番台](https://httpwg.org/specs/rfc9110.html#status.5xx)                                                 | サーバエラー    | リクエストの処理中にサーバ側でエラーが発生した               | 

具体例:  
[Status Code Registration](https://httpwg.org/specs/rfc9110.html#status.code.registration)

#### レスポンスボディの解析

ウェブから取ってくるデータの代表的な形式は、以下の4つ

| 形式   | 概要                      | メモ                                |
|------|-------------------------|-----------------------------------|
| CSV  | 表形式のデータ。                | 表形式ならまずこれ                         |
| JSON | 外部のプログラムに読ませるために準備されたデータ。 | 構造を有するデータならまずこれ                   | 
| XML  | 外部のプログラムに読ませるために準備されたデータ。 | 構造を有するデータでは、かつては XML が主流だった       | 
| HTML | ブラウザで表示させるために準備されたデータ。  | 人間に見せるようのページのデータ。いわゆる「スクレイピング」の対象 |

JSONとXMLでは、JSONのほうが今日では一般的。  
XMLは、HTMLをスクレイピングする要領で解析できる。

##### CSVデータに固有の注意点

JSON, HTML とも、 response.text で得られた文字列をすぐに解析できる。  
しかし、 CSV ではそうは行かない。

なぜかというと、既出の csv.reader や csv.DictReader は、文字列を受け取る仕様ではないから。

csv.reader や csv.DictReader は、以下のいずれかを受け取る。

- ファイル(厳密には、 file-like object)
- 文字列を次々に返すイテレータ

[csv --- CSV ファイルの読み書き csv.reader](https://docs.python.org/ja/3/library/csv.html#csv.reader)

そこで、CSVデータについては、受け取ったレスポンスに対し、以下のいずれかの処理を行う必要がある。

| 解決策                     | 解決策                             |
|-------------------------|---------------------------------|
| ファイルのように扱う              | StringIO で、「ファイルのように扱う」ための準備をする |
| 文字列を次々に返すイテレータにする | splitlines() で処理をする             |

```python
"""
StringIO を使う場合

StringIO は、メモリ内にあるデータをローカルにあるファイルのように扱いたいときに使う
"""
import csv
from io import StringIO
import requests

url = 'https://flask.pc5bai.com/stock/info/csv/'
response = requests.get(url)

if response.status_code != 200:  # ステータスコードが200であることを確認する
    print(response.status_code)
    exit(1)

with StringIO(response.text) as string_io:
    reader = csv.reader(string_io)
    for row in reader:
        print(row)

with StringIO(response.text) as string_io:
    dict_reader = csv.DictReader(string_io)
    for row in dict_reader:
        print(row)
```

```python
"""
.splitlines() を使う場合
"""
import csv
import requests

url = 'https://flask.pc5bai.com/stock/info/csv/'
response = requests.get(url)

if response.status_code != 200:  # ステータスコードが200であることを確認する
    print(response.status_code)
    exit(1)

text_lines = response.text.splitlines()

reader = csv.reader(text_lines, )
for row in reader:
    print(row)

dict_reader = csv.DictReader(text_lines, )
for row in dict_reader:
    print(row)
```
