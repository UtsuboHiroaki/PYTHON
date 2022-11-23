def opening_greetings(pre_str, post_str, date='2020/10/07', area='関東地方'):
    return f'{pre_str}{post_str}それではこれから、{date}の{area}の天気予報をお伝えします。'


my_list = ['こんにちは！', 'ごきげんいかがですか？！']
my_dict = {
    'date': '2020/10/11',
    'area': '北陸地方',
}
result = opening_greetings(*my_list, **my_dict)
print(result)
