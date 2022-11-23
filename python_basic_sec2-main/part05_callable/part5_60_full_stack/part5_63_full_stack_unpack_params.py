def full_stack_openings(pre_str, post_str, *args, date='2020/10/07', area='関東地方', **kwargs):
    print(pre_str + post_str)
    if args:
        print('\nはじめに、季節の話題です。')
        for arg in args:
            print(arg)
    if kwargs:
        print('\n最初に、警報と注意報をお伝えします。')
    if kwargs.get('danger'):
        print('警報をお知らせします。')
        print(kwargs.get('danger'))
    if kwargs.get('warning'):
        print('注意報をお知らせします。')
        print(kwargs.get('warning'))

    print(f'\nそれでは、これから、{date}の{area}の天気予報をお伝えします。')


info_list = [
    'おはようございます。',
    '天気予報の時間です。'
    '秋も深まり、長野県の◯◯村では、ぶどうの収穫が最盛期です。',
    '東京や名古屋からぶどう狩りに来る観光客もたくさんいます。',
    'さっそく、取材映像をご覧いただきましょう。',
    'この品種のぶどうは、ほかの品種に比べて収穫時期が遅いそうです。',
    '来週いっぱいまでは紅葉を楽しめるだろうということです。',
]
cautions = {
    'danger': '東北地方に強風警報がでています',
    'warning': '北海道に大雪注意報がでています',
    'date': '2020/10/11',
}

full_stack_openings(*info_list, **cautions)
