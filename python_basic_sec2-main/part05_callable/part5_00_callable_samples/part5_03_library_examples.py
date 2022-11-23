from pathlib import Path

from bs4 import BeautifulSoup

# 1. 関数の呼び出し
builtin_func_result = sum([1, 2, 3, 4, 5])
sorted_result = sorted([7, 5, 3, 1, 2, 4, 6])

# 2. クラスメソッドの実行
classmethod_result = Path.cwd()

# 3. インスタンスの生成
soup = BeautifulSoup('<html><title></title><body><p>こんにちは</p></body></html>', "html.parser")

# 4. インスタンスの呼び出し
call_result = soup()

# 5. インスタンスメソッドの呼び出し
method_result = soup.select_one('p')
