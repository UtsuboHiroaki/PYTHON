import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--min', type=int, default=3, help='初期値を指定します')
parser.add_argument('-i', '--items', type=int, default=5, help='出力する要素数を指定します')
parser.add_argument('-c', '--count', action='store_true', help='要素数を返します')
args = parser.parse_args()

print(args.min)
print(args.items)
print(args.count)

my_list = list(range(args.min, args.min + args.items))
print(my_list)
if args.count:
    print(len(my_list))
