def greetings(pre_str, post_str):
    return pre_str + post_str


my_list = ['こんにちは！', 'ごきげんいかがですか？！']
result = greetings(*my_list)
print(result)

