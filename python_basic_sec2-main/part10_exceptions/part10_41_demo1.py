from datetime import date


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
        raise ValueError('過去の日付は指定できません')

    if dt.weekday() in [5, 6]:
        raise ValueError('休日は指定できません')

    if dt.day % 5 == 0:
        raise ValueError('5, 10日は指定できません')

    return f'{task} を {dt.strftime("%Y月%m月%d日")} に必ず実行するとお約束します！'


if __name__ == '__main__':
    try:
        result = add_task('月次決算をまとめる仕事', date(2022, 11, 10))
    except ValueError as e:
        print(e)
    else:
        print(result)
    finally:
        print('処理を終了します')
