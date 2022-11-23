def my_average(args):
    return sum(args) / len(args)


def get_func_to_use(func_name):
    """
    受け取った文字列によって、返す関数を変える
    """

    if func_name == 'a':
        return my_average
    elif func_name == 's':
        return sum
    elif func_name == 'x':
        return max
    elif func_name == 'n':
        return min
    else:
        return len


base_list = [7, 1, 3, 5, 4]

func = get_func_to_use('a')
result = func(base_list)

func = get_func_to_use('s')
result = func(base_list)
print(result)

func = get_func_to_use('x')
result = func(base_list)
print(result)

func = get_func_to_use('n')
result = func(base_list)
print(result)

func = get_func_to_use('z')
result = func(base_list)
print(result)
