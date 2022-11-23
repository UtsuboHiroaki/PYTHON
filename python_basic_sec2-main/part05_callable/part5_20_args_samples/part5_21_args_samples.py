def greetings(pre_str, post_str):
    return pre_str + post_str


result = greetings('こんにちは！', 'ごきげんいかがですか？！')
print(result)

result = greetings(pre_str='こんにちは！', post_str='ごきげんいかがですか？！')
print(result)

result = greetings(post_str='ごきげんいかがですか？！', pre_str='こんにちは！')
print(result)

# result = greetings(pre_str='こんにちは！', 'ごきげんいかがですか？！')
# print(result)
