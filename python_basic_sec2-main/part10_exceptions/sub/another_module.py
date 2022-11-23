def func_x():
    return 1 / 0


def func_y():
    return func_x()


def func_z():
    return func_y()
