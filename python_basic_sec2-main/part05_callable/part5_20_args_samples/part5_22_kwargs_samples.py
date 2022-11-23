def weather_news_greetings(date='2020/10/07', area='関東地方'):
    return f'これから、{date}の{area}の天気予報をお伝えします。'


result = weather_news_greetings(date='2020/10/08', area='山陰地方')
print(result)

result = weather_news_greetings(area='中国地方', date='2020/10/10')
print(result)

result = weather_news_greetings()
print(result)

# 以下は、いちおうOKだがおすすめしない
result = weather_news_greetings('2020/10/11', '北陸地方')
print(result)

result = weather_news_greetings('2020/10/13', )
print(result)
