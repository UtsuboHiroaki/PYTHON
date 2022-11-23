def greetings(*args):
    return args[0] + args[1]


result = greetings('こんにちは！', 'ごきげんいかがですか？！')
print(result)
