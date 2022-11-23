def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


result = opening_greetings('こんにちは！', '12時のニュースの時間です。', date='2020/10/08', area='甲信越地方')
print(result)

result = opening_greetings(pre_str='こんにちは！', post_str='12時のニュースの時間です。', )
print(result)
