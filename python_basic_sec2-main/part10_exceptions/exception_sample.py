def calc_except_thirty(n, divide_by):
    """
    :param n: 30以外の数値を受け取る
    :param n: 0以外の数値を受け取る
    :return: n / divide_by
    """
    if n == 30:
        raise ValueError('3だけは受けつけられません。ごめんなさい')
    result = n / divide_by  # divide_by = 0 のとき、 ZeroDivisionError が発生する
    return result


def get_calc_result(n, divide_by):
    """
    :param n: 30以外の数値を受け取る
    :param n: 0以外の数値を受け取る
    :return: n / divide_by
    """
    try:
        result = calc_except_thirty(n, divide_by)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    # except Exception as e:
    #     print(e)
    #     raise e
    else:
        print(result)
    finally:
        print('raise 文が含まれていない限り、 finally は必ず実行されます')


if __name__ == '__main__':
    get_calc_result(30, 2)
    get_calc_result(10, 0)
    get_calc_result('こんにちはこんばんは', 2)
    get_calc_result(10, 2)
