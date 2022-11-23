def average(args):
    return sum(args) / len(args)


def execute_func(func, args):
    return func(args)


base_list = [7, 1, 3, 5, 4]

result = execute_func(sum, base_list)
print(result)

result = execute_func(len, base_list)
print(result)

result = execute_func(max, base_list)
print(result)

result = execute_func(min, base_list)
print(result)

result = execute_func(average, base_list)
print(result)
