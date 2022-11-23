"""
戻り値を返すサンプル

受け取ったリストの内容は変更しない
以下の関数は、戻り値を返している
"""


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
