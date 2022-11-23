class StrValueException(ValueError):
    def __init__(self, value):
        self.message = '文字列は受けつけられません: ' + value


def calc_except_thirty(n, divide_by):
    """
    :n: 30以外の数値を受け取る
    :divide_by: 0以外の数値を受け取る
    """
    if isinstance(n, str):
        raise StrValueException(n)

    if n == 30:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    return n / divide_by


try:
    result = calc_except_thirty('毎月10日は経理の締めの日です', 3)
except ValueError as e:
    print(e.message)
