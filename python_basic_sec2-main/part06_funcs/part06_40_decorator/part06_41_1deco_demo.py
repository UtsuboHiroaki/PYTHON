def print_timestamp(func):
    print('天気予報を開始します。')
    print('現在時刻は、2020/10/07 12:00:00 です。')

    func()

    print('現在時刻は、2020/10/07 12:00:01 です。')
    print('天気予報完了までにかかった時間は1秒でした。')


def show_weather_info():
    print('\t昨日の天気は、晴れでした。')
    print('\t今日の天気は、晴れです。')
    print('\t明日の天気は、くもりです。')
    print('\t明後日の天気は、雨です。')


print_timestamp(show_weather_info)
