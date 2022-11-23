import datetime


class DayError(ValueError):
    def __init__(self ):
        super().__init__(self.message)


class PastDayError(DayError):
    def __init__(self, day):
        self.message = f'過去の日付は指定できません。: {day.strftime("%Y/%m/%d")}'
        super().__init__()


class NotWeekDayError(DayError):
    def __init__(self, day):
        self.message = f'平日ではありません。: {day.strftime("%Y/%m/%d")}'
        super().__init__()


class FileTenDayError(DayError):
    def __init__(self, day):
        self.message = f'5, 10日は忙しいので無理です。: {day.strftime("%Y/%m/%d")}'
        super().__init__()


def set_execute_day(task, day):
    if day < datetime.date.today():
        raise PastDayError(day)

    if day.weekday() in [5, 6]:
        raise NotWeekDayError(day)

    if day.day % 5 == 0:
        raise FileTenDayError(day)

    return f'{task} を {day} に実行するとお約束します！'


try:
    result = set_execute_day('月次決算をまとめる仕事', datetime.date(2022, 11, 12))
except PastDayError as e:
    print(e)
except NotWeekDayError as e:
    print(e)
except FileTenDayError as e:
    print(e)
else:
    print(result)
