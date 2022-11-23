"""
破壊的変更を行うサンプル

以下の関数は、受け取ったリストのすべての要素を2倍にする
戻り値は返さない
"""


def double_list_items(my_list):
    """
    リストのすべての要素を2倍にする
    """
    for i in range(len(my_list)):
        my_list[i] *= 2


base_list = [7, 1, 3, 5, 4]

double_list_items(base_list)
print(base_list)  # リストの内容は破壊的に変更されている
