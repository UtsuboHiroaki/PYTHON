# ファイルの読み込み、書き込み

## このページの構成

1. 「ファイル内のデータ」についての一般論
2. Pythonでのファイルの読み込み、書き込み
3. CSVデータ、JSONデータの読み込み、書き込み
4. 文字列の「種類」、f文字列、u文字列、b文字列、r文字列

***

## 1. 「ファイル内のデータ」についての一般論

### バイナリファイルとテキストファイル

ファイルは、その中のデータの性質を元にして、以下の2種類に分類できる。

| 分類       | 分類 | 例                                                     |
|----------| --- |-------------------------------------------------------|
| バイナリファイル | 「テキストファイル」として解釈し得えないもの | .pdf ファイル、.mp3 ファイル、 .mp4 ファイル、.zip ファイル、 .exe ファイルなど |
| テキストファイル | 「テキストファイル」として解釈し得るもの | .txt ファイル、 .csv ファイル、 .json ファイルなど                    |

テキストファイルの中身は、何らかの「文字コード」に基づいて文字が記述されている。    
「文字コード」とは、バイナリデータの暗号解読表のようなもの。

「文字コード」の例:

| 文字コード     | 説明                                                                                  |
|-----------|-------------------------------------------------------------------------------------|
| UTF-8     | 「ユニコード」の一種で、多様な文字を有する。<br>今日のデファクトスタンダード。<br>Windowsでも、Windows10以降はいちおうこれが標準とされている。 |
| SHIFT_JIS | Windows環境で長く使われてきた、日本語利用者向けの文字コード。<br>現在でも見かけるし、ある意味悩みのタネ。                          |
| EUC-JP    | Unix環境で使われてきた、日本語利用者向けの文字コード。<br>今日となっては、意識する必要はほぼない。                               |

なお、UTF-8 にも、以下の2種類がある。

| UTF-8 の種類 | 説明                         |
|-----------|----------------------------|
| BOMあり     | BOM と呼ばれるバイト列がデータ先頭に付与される。 |
| BOMなし     | BOM と呼ばれるバイト列がデータ先頭に付与されない。   |

原則として、BOMを使うのが良い。

***

## 2. Pythonでのファイルの読み書き

Python では、文字コードを指定しない場合、デフォルトで UTF-8 が使われる。

ただし、ファイルを開く際には、プラットフォーム(os)によって定められたデフォルトのエンコードで読み込もうとする。  
Windows では、Shift-JIS がデフォルトのエンコード。  
Mac では、UTF-8 がデフォルトのエンコード。

### ファイルを開く

ファイルの読み込み、書き込み用として、従来 open 関数があった。  
pathlib では、Path オブジェクトの open メソッドがある。

以下では、 Path オブジェクトの open メソッドを使う。

#### ファイルの読み書きの「基本」

以下の [1], [2] では、 [2] のほうが望ましい。  
以下の理由から:

- ファイルは、開いたあと、自己の責任で閉じなくてはならない
- 閉じ忘れは避けたい
- with 文を使うと、with 文の終わりで自動的に閉じてくれる

```python
from pathlib import Path

path = Path(__file__).parent
path = path / 'readme.md'

# [1]with コンテクストマネージャを使わない。用が済んだら自分で close する必要がある。
file = path.open(mode='r', encoding='utf-8')
print(file.read())
file.close()

# [2] with コンテクストマネージャを使。用が済んだら自動で close される。  
with path.open(mode='r', encoding='utf-8') as file:
    print(file.read())
```

path.open で使う引数:

| 引数 | 説明                                                               |
| --- |------------------------------------------------------------------|
| mode | ファイルを開くモード。'r' は読み込み専用、'w' は書き込み専用、'a' は追記専用。デフォルトは 'r' (*1)(*2) |
| encoding | ファイルの文字コード。デフォルトは UTF-8。                                         |

(*1) 'x' もあるが気にしなくてよい)  
(*1) 'rb' 等の記法でバイナリデータも開けるが、本講座では取り扱わない。

#### ファイルの読み込み

```python
from pathlib import Path

path = Path(__file__).parent
path = path / 'readme.md'

# 一気に全行読み込む
with path.open(mode='r', encoding='utf-8') as file:
    print(file.read())

# 一行ずつ読み込む(リストは各行の内容。改行コードも含まれる)
with path.open(mode='r', encoding='utf-8') as file:
    for line in file:
        print(line)

# 以下では、改行コードを取り除いて出力する
with path.open(mode='r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
```

#### ファイルの書き込み

ファイルの書き込みは、以下のように行う。

```python
from pathlib import Path
from datetime import datetime

path = Path(__file__).parent
path = path / 'new_file.md'

# 上書きモードでファイルを開く
with path.open(mode='w', encoding='utf-8') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 最初の一行\n')

# 追記モードでファイルを開く
with path.open(mode='a', encoding='utf-8') as file:
    # ファイルに書き込む
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{now_str}: 2行目\n')
```

***

## 3. CSVデータと、JSONデータ

### 背景

別のシステム間で、データをやりとりする必要がままある。  
例: 「エクセルから弥生会計」、「Google SpreadSheet等のウェブシステムからエクセル」、等々。

ついては、別システム同士でデータをやりとりするときの共通規格が必要。  
ということで、CSVやJSONがある。

| 形式 | 概要                        | 本来の名称 | メモ                  |
|------|---------------------------|------|---------------------|
| CSV | 表形式のデータをテキスト(文字列)で表現したもの。 | Comma Separated Data | TSV とかもあるにはあります     |
| JSON | 構造のあるデータをテキスト(文字列)で表現したもの。 | JavaScript Object Notation | 要は、「JavaScript版の辞書」 |

かつては、構造のあるデータのやりとりにはXMLが使われていた。  
今日では、この目的でのXML利用はあまりない。より扱いやすいというJSONのほうがスタンダード。

### CSVファイル

読み込み/書き込みには、csvモジュールを使う。  
データをリストとして取り扱うか、辞書として取り扱うかで、使うメソッド等が異なる。

辞書として扱うための便利クラスとして、DictReader, DictWriter がある。

#### CSVファイルの読み込み

```python
import pathlib
import csv

path = pathlib.Path(__file__).parent / 'sample.csv'

with path.open(mode='r', encoding='utf-8', newline='') as file:
    # csvファイルのデータをリストとして読み込む
    reader = csv.reader(file)
    for row in reader:
        print(row)

with path.open(mode='r', encoding='utf-8', newline='') as file:
    # csvファイルのデータを辞書として読み込む
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

#### CSVファイルの書き込み

```python
import pathlib
import csv

path = pathlib.Path(__file__).parent / 'sample.csv'

with path.open('w', encoding='utf-8', newline='') as file:
    # csvファイルにデータをリストとして書き込む
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', '田中', '25'])
    writer.writerow(['2', '佐藤', '35'])

with path.open('w', encoding='utf-8', newline='') as file:
    # csvファイルにデータを辞書として書き込む
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '3', 'name': '花子', 'age': '27'})
    writer.writerow({'id': '4', 'name': '太郎', 'age': '37'})
```

#### path.open での newline='' の指定について

<span style="color:#ff0000;">特に、Windowsでの注意点:  
書き込み時には、open時に引数 newline='' を指定すること。  
これがないと、改行の位置がおかしくなる。</span>  
「Windowsでのデフォルト改行コードが \r\n だから」というのが理由です。

参考: 主要OSでの改行コード

| os | 改行コード |
| ---- | ---- |
| Linux | \n |
| mac os | \r |
| Windows | \r\n |

### JSONファイル

JavaScriptという言語の辞書の書式(と、ほぼ同じ)。  
Python辞書と似ているが、微妙に異なる。

具体的な違いを以下に示した:

| 項目    | Python          | Json                               |
|-------|-----------------|------------------------------------|
| bool値 | True            | true                               |
| bool値 | False           | false                              |
| None値 | None            | null                               |
| キー    | immutable ならばOK | ダブルクオートで囲った文字列のみOK<br>シングルクオートでもダメ |
| 値     | 何でもOK         | bool値/数値/文字列のみ (*1)(*2)            |

[公式ドキュメント内の変換表も参照のこと](https://docs.python.org/ja/3/library/json.html#py-to-json-table)

読み込み/書き込みには、jsonモジュールを使う。
json.loads, json.dumps で、Python辞書との相互変換ができる。

```python
import json

# JSON文字列をPython辞書に変換
json_str = '{"a": 1, "b": false, "c": null}'
python_dict = json.loads(json_str)
print(type(python_dict), python_dict)
```

```python
import json

# Python辞書をJSON文字列に変換
json_dump_result = json.dumps({'a': 1, 'b': False, 'c': None})
print(type(json_dump_result), json_dump_result)
```

```python
import json
from pathlib import Path

# JSONファイルを読み込む
read_path = Path(__file__).parent / 'data' / 'json_sample.json'
with read_path.open('r', encoding='utf-8') as file:
    data_str = file.read()
    result_dict = json.loads(data_str)
    print(result_dict)
```

```python
import json
from pathlib import Path

# JSONファイルに書き込む(indent, ensure_ascii を指定)
write_path = Path(__file__).parent / 'data' / 'json_write_sample.json'
data_dict = {"a": 1, "b": False, "c": None}
with write_path.open('w', encoding='utf-8') as file:
    json_str = json.dumps(data_dict, indent=2, ensure_ascii=False, )
    file.write(json_str)
```

[json.loads についての公式ドキュメント解説](https://docs.python.org/ja/3/library/json.html#json.loads)  
[json.dumps についての公式ドキュメント解説](https://docs.python.org/ja/3/library/json.html#json.dumps)

(*1)
JSONの制約であって、JavaScriptの制約ではない。  
JavaScript の辞書でも、値にオブジェクトを持つことができる。

(*2)
たとえば日付については、 辞書 -> Json 変換では、datetime.datetime.fromisoformat を使って文字列にする。

以下はエラー

```python
from datetime import datetime
import json

now = datetime.now()
json_data = json.dumps(now)  # TypeError: Object of type datetime is not JSON serializable (*3)
```

以下はOK(naive な場合)

```python
from datetime import datetime
import json

now = datetime.now()
iso_now = datetime.isoformat(now)
json_data = json.dumps(iso_now)
print(json_data)  # "2022-09-28T21:15:20.943701"
```

以下はOK(aware な場合)

```python
from datetime import datetime
from zoneinfo import ZoneInfo
import json

now = datetime.now()
now = now.replace(tzinfo=ZoneInfo("Asia/Tokyo"))
iso_now = datetime.isoformat(now)
json_data = json.dumps(iso_now)

print(json_data)  # '"2022-09-28T21:15:04.273942+09:00"'
```

(*3)
"serialize" とは:  
(英語の「シリーズ(series)」の「 -lize 系」サッカーが好きな方向けに書くと、イタリア1部リーグ「セリエA」とかも語源は同じ)    
原義は、「一連の○○にする」的な意味。  
つまり、ここでは、「文字列にしている」という意味。  
「オブジェクトという立体的でもふもふしたものの情報の一部を取り出して、LANケーブルを通じて渡せる文字列情報にした」というような理解をしていただければと。

## 文字列の「種類」、f文字列、u文字列、b文字列, r文字列

最後に、文字列の種類についてのメモ:

| 文字列の種類 | 概要                                                                                                   | 例                                                 |
|--------|------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 文字列    | Pythonでは、デフォルトは、UTF-8でエンコードされた文字列。                                                                   | "あいうえお"                                           |
| f文字列   | 先頭にfをつけると、中に変数や演算結果等を埋め込める。<br>文字列の .format メソッドと機能的に似ている。                                           | f'これは、{num}回目の作業です！'                              |
| u文字列   | 先頭にuをつけると、unicode だということを明示。<br>ただし、今日デフォルトUTF-8なので、使われない。<br>(UTF-8は unicode の一種)                      | u"これは unicode  文字列です"                             |
| b文字列   | 先頭にbをつけると、バイト列として扱う。<br>テキスト形式で開けないファイルの場合、これを使うことになる。<br>テストコードを書く時にたまに使うくらい。                       | b"This is byte strings."                          |
| r文字列   | 先頭にrをつけると、「正規表現(*4)」用の文字列となる。<br>バックスラッシュ「\」記号がエスケープ文字と解釈されない。<br>その性質から、Windowsのパスを表現するのに使われることがある。 | r"C:\Program Files\Microsoft Office\root\Office16" |

上記については、ここまでの講座内で得られた知識以上のことは当面必要ないかと。

(*4) 「正規表現」とは、文字列の検索手法のひとつ。かなり高度。