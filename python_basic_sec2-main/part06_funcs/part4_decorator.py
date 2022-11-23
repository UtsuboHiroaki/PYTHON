import time
from datetime import datetime


def my_decorator(func):
    """
    関数実行前と実行後の時刻を print するデコレーター関数
    """

    def wrapper(*args, **kwargs):
        # 前処理
        print(f'開始日時: {datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")}')
        result = func(*args, **kwargs)
        # 後処理
        print(f'終了日時: {datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")}')
        return result

    return wrapper


def expo_scores1(expo, *args):
    print('\nexpo_scores1 開始')
    total = 0
    for x in args:
        total += x ** expo
        time.sleep(0.1)  # 1秒待機
    return total


print(expo_scores1(2, 1, 2, 3, 4, 5))

new_func = my_decorator(expo_scores1)
print(new_func(2, 1, 2, 3, 4, 5))


@my_decorator
def expo_scores2(expo, *args):
    print('\nexpo_scores2 開始')
    total = 0
    for x in args:
        total += x ** expo
        time.sleep(0.5)
    return total


print(expo_scores2(2, 1, 2, 3, 4, 5))
