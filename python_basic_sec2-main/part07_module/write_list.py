import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min', type=int, default=3, help='初期値を指定します')
    parser.add_argument('-i', '--items', type=int, default=5, help='出力する要素数を指定します')

    args = parser.parse_args()

    min_value = args.min
    max_value = args.min + args.items

    result_list = list(range(min_value, max_value, ))
    print(result_list)
