"""
破壊的変更も行わず、戻り値も返さない例

以下の関数は、受け取ったリストのすべての要素を2倍にする
戻り値を返す(返す戻り値はリストではない)
"""


def print_list(my_list):
    """
    リストのすべての要素をコンソールに出力する
    """
    for i in range(len(my_list)):
        print(my_list[i])


base_list = [7, 1, 3, 5, 4]

print_list(base_list)  # リストの内容は変更されていない
