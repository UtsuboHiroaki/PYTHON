# html文書、xml文書の解析

## html文書、xml文書について

### html文書

ウェブページの構造を示す、タグでマークアップされた文書。  
HTML: HyperText Markup Language

HTMLページの例については、 data/index.html を参照のこと。  
[デモサイトのトップページ](https://flask.pc5bai.com/) でも同じものが得られます。

### xml文書

XMLについては、「HTMLの親戚」くらいに思っておけばまあ間違いではない。  
(近年は、jsonに取って代わられている)  
XML: eXtensible Markup Language

## html文書、xml文書の解析

HTML, XML を解析する方法として、代表的なのは以下の2つ

| 手法 | 特徴                                              |
| ---- |-------------------------------------------------|
| xml.etree.ElementTreeモジュール | pip 不要ですぐに使える                                   |
| BeautifulSoupモジュールを使う | ```pip install bs4``` が必要だが、利便性は ElementTreeモジュール より上。推奨 |

## スクレイピング

### スクレイピングとは？

HTMLページの内容を解析して、欲しい情報をプログラム的に取得すること。

scrape: 「ひっかく」とか、「削り取る」とか、そういう意味。

参考1: アイスクリームを掬う道具は「スクレイパー」  
参考2: 高層ビルは「スカイスクレイパー」

「ウェブページの上をひっかいて、必要な情報を掬い取っていく」というようなイメージ。

### スクレイピングの実際

#### 基本方針

HTML内に存在する以下を元にして絞りこんでいく。

- タグ
- id
- class
- 属性

#### BeautifulSoup の頻出メソッド

| メソッド                 | 概要             | 戻り値の型 |
|----------------------|----------------|-------|
| .select()            | CSS セレクタで絞り込む  | Tagオブジェクトのリスト |
| .select_one()        | CSSの セレクタで絞り込む | Tagオブジェクト |
| .find()              | タグ名で絞り込む       | Tagオブジェクト |
| .find_all()          | タグ名で絞り込む       | Tagオブジェクトのリスト |
| .find_all(属性名="属性値") | 属性名と属性値で絞り込む   | Tagオブジェクトのリスト |

実際には、 .select(), .select_one() だけでほぼほぼなんとかなる。  
.find*() 系の手法は、「別解」といったところ。

#### 最初に覚えたい CSS セレクターの代表的な記法

複雑な動きをするウェブページでなければ(*2)、以下を追求すればまあなんとかなる。

| 書き方             | 意味          | 用例                                                  | 
|-----------------|-------------|-----------------------------------------------------| 
| tag             | タグで絞りこむ     | ```anchors = soup.select('a')```                    |
| #id             | idで絞りこむ     | ```div_metal = soup.select('#galapagos-metal')```   |
| .class          | クラスで絞りこむ    | ```company_divs = soup.select('.company-link')```   |
| .class1.class2  | 複数クラスで絞りこむ  | ```div_stock = soup.select('.company-link.stock')``` |
| tag.class       | タグとクラスで絞りこむ | ```company_divs = soup.select('div.company-info')``` |
| tag[attr=value] | タグと属性で絞りこむ  | ```anchors = soup.select('a[target="_blank"]')```   |
| 条件1 条件2         | 複数条件で絞りこむ   | ```footer_links = soup.select('select a')```  |

とりあえず上記をマスターしたうえで、以下のページやウェブ上のまとめ記事で次第にバリエーションを増やしていくのがよい。  
[MDN Web Docs: CSS セレクター](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Selectors)

(*2)  
「複雑な動きをするページ」とは、ウェブページの表示が画面遷移しないままでコロコロ変わるようなページのこと。

#### サンプルコード

```python
from pathlib import Path
from bs4 import BeautifulSoup

path = Path(__file__).parent / 'data' / 'html' / 'index.html'
with path.open('r', encoding='utf8') as file:
    html = file.read()

# まずは、html文書を BeautifulSoup に取りこませる
soup = BeautifulSoup(html, "html.parser")

# 取り込めたことを確認してみる
print(soup)

anchors = soup.select('a')  # a タグをすべてリスト
for anchor in anchors:
    print(anchor.getText(), anchor['href'])

# 以下のように、次第に絞りこんでいくこともできる
footer = soup.select_one('footer')
footer_links = footer.select('a')
for link in footer_links:
    print(link.getText(), link['href'])
```

