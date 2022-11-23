"""
破壊的変更を行うサンプル

以下の関数は、受け取ったリストのすべての要素を2倍にする
戻り値を返す(返す戻り値はリストではない)
"""


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
