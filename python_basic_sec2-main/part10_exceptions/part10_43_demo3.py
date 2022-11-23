from datetime import date


class DateError(ValueError):
    def __init__(self, message, dt):
        self.message = message
        self.dt = dt
        super().__init__(message)

    def __str__(self):
        return f'{self.message}: {self.dt.strftime("%Y/%m/%d")}'


class PastDateError(DateError):
    def __init__(self, dt):
        super().__init__('過去の日付は指定できません', dt)


class HolidayError(DateError):
    def __init__(self, dt):
        super().__init__('休日は指定できません', dt)


class FiveTenDayError(DateError):
    def __init__(self, dt):
        super().__init__('5, 10日は指定できません', dt)


def add_task(task, dt):
    """
    タスクを追加する

    ただし、以下の条件のいずれかを満たす場合は拒絶する
        - 過去の日付
        - 休日
        - 5, 10日

    :param task: 追加するタスク
    :param dt: タスクの実行予定日
    :return: タスクと実行日と固い約束を含めた文字列
    """
    if dt < date.today():
        raise PastDateError(dt)

    if dt.weekday() in [5, 6]:
        raise HolidayError(dt)

    if dt.day % 5 == 0:
        raise FiveTenDayError(dt)

    return f'{task} を {dt.strftime("%Y月%m月%d日")} に必ず実行するとお約束します！'


if __name__ == '__main__':
    try:
        result = add_task('月次決算をまとめる仕事', date(2022, 11, 27))
    except DateError as e:
        print(e)
    else:
        print(result)
    finally:
        print('処理を終了します')
