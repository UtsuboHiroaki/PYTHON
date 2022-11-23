"""
天気予報プログラムです
"""


def weather_news(pre_str, post_str, *args, date="明日", area="東京", **kwargs):
    print(pre_str + post_str)

    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        if k == 'danger':
            print('警報です：' + v)
        else:
            print('注意報です：' + v)

    print('それでは、これから' + date + "の" + area + "の天気予報をお伝えします")


weather_news("こんにちは。", "天気予報の時間です。",

             '秋も深まり、長野県の◯◯村では、ぶどうの収穫が最盛期です。',
             '東京や名古屋からぶどう狩りに来る観光客もたくさんいます。',
             'さっそく、取材映像をご覧いただきましょう。',
             'この品種のぶどうは、ほかの品種に比べて収穫時期が遅いそうです。',
             '来週いっぱいまでは紅葉を楽しめるだろうということです。',

             date="今日", area="大阪",
             danger='東北地方に強風警報がでています', warning='北海道に大雪注意報がでています'
             )
