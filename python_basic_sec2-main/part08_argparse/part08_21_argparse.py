import argparse

parser = argparse.ArgumentParser()
parser.add_argument('min', type=int, help='初期値を指定します')
parser.add_argument('items', type=int, help='最大値を指定します')
args = parser.parse_args()

print(args.min)
print(args.items)

my_list = list(range(args.min, args.min + args.items))
print(my_list)

