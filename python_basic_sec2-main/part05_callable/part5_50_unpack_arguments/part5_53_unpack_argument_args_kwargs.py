def opening_greetings(*args, **kwargs):
    return f'{args[0]}{args[1]}それではこれから、{kwargs["date"]}の{kwargs["area"]}の天気予報をお伝えします。'


result = opening_greetings('こんにちは！', 'ごきげんいかがですか？！', date='2020/10/11', area='北陸地方')
print(result)
