import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min', type=int, default=3, help='初期値を指定します')
    parser.add_argument('-i', '--items', type=int, default=5, help='出力する要素数を指定します')
    parser.add_argument('-l', '--length', action='store_true', help='要素数を返します')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    for i in sys.argv:
        print(i)
    print('sysm.argv の出力を終了しました\n')

    args = parse_args()
    min_value = args.min
    max_value = args.min + args.items
    length_only = args.length

    result_list = list(range(min_value, max_value, ))

    if length_only:
        print(len(result_list))
    else:
        print(result_list)
