def func_a():
    return 1 / 0


def func_b():
    return func_a()


def func_c():
    return func_b()


if __name__ == '__main__':
    func_c()
