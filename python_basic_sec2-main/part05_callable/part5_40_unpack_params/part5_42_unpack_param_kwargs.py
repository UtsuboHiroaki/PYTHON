def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


my_dict = {'date': '2020/10/11', 'area': '北陸地方'}
result = weather_news_greetings(**my_dict)
print(result)
