import datetime


class DateError(ValueError):
    def __init__(self, message, date):
        self.message = message
        self.date = date
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.date.strftime("%Y/%m/%d")}'


def set_execute_day(task, day):
    """
    仕事を実行する日を設定する。

    ただし、以下のいずれかに合致する日を指定された場合は例外を発生して拒絶する
        - 過去の日付
        - 休日
        - 5, 10日

    :param task: 実行する仕事
    :param day: 実行予定日
    :return: 「必ず実行する」というお約束のお返事
    """
    if day < datetime.date.today():
        raise DateError('過去の日付は指定できません', day)

    if day.weekday() in [5, 6]:
        raise DateError('平日ではありません', day)

    if day.day % 5 == 0:
        raise DateError('5, 10日は忙しいので無理です', day)

    return f'{task} を {day.strftime("%Y/%m/%d")} に必ず実行するとお約束します！'


try:
    result = set_execute_day('月次決算をとりまとめる仕事', datetime.date(2022, 11, 12))
except DateError as e:
    print(e)
else:
    print(result)
