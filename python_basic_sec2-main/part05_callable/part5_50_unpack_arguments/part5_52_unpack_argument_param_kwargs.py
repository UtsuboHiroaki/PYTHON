def weather_news_greetings(**kwargs):
    return f'これから、{kwargs["date"]}の{kwargs["area"]}の天気予報をお伝えします。'


result = weather_news_greetings(date='2020/10/11', area='北陸地方')
print(result)
