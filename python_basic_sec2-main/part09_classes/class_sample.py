import json
from datetime import date
import requests

METAL_TYPES = ['gold', 'silver', 'bronze', 'platinum', 'pallatinum', ]
SITE_BASE_URL = 'http://127.0.0.1:5000/metal/'


class MyMetal:
    """
    所有している貴金属の情報を有するクラス

    type_name: 貴金属の種類
    weight: 貴金属の重さ
    base_price: 貴金属の購入時の価格
    base_date: 貴金属の購入日
    """

    def __init__(self, type_name, weight, base_price, base_date=None):
        if type_name not in METAL_TYPES:
            raise ValueError('貴金属の種類が不正です')

        if weight <= 0:
            raise ValueError('重さは0以上である必要があります')

        if base_date is None:
            base_date = date.today()
        if base_price <= 0:
            raise ValueError('購入価格は0以上である必要があります')

        today = date.today()
        if base_date > today:
            raise ValueError('購入日は今日以前である必要があります')

        self.type_name = type_name
        self.weight = weight
        self.base_price = base_price
        self.base_date = base_date

    def __call__(self, *args, **kwargs):
        interval = self.get_interval_days()
        return f'{self.base_date}に購入してから {interval}日保持している {self.type_name} です'

    def __str__(self):
        return f'{self.type_name} {self.weight}グラム、購入価格 {self.base_price}円'

    def get_price_from_website(self):
        """
        send api request to website f'http://127.0.0.1:5000/api/{self.type_name}'
        returns raw json response
        """
        response = requests.get(f'{SITE_BASE_URL}/api/info/{self.type_name}/')
        return response.json()

    def get_expected_total_price(self):
        """
        貴金属の現在の相場を調べ、期待できる販売価格を返す
        """
        price = self.get_price_from_website()['buy']
        return price * self.weight

    def get_expected_profit(self):
        return self.get_expected_total_price() - self.base_price

    def sell(self, weight):
        """
        貴金属を売る

        jsonで type_name, weight を送信する
        status code = 200 の場合は weight の値を減らし、戻り値に含まれる利益額を返す
        status code = 400 の場合は ValueError を投げる
        status code = 500 の場合は Exception を投げる
        """
        if weight > self.weight:
            raise ValueError('販売する重さが足りません')

        payload = {'metal_type': self.type_name, 'weight': weight, 'email': 'foo@bar.com', 'name': 'mr.foo'}
        response = requests.post(
            f'{SITE_BASE_URL}/api/buy/',
            json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        print(response.status_code)
        if response.status_code != 200:
            raise Exception('販売に失敗しました')

        response_json = response.json()
        price = response_json['price']
        self.weight -= weight
        return f'{weight}gを販売して、{price}円を得ました'

    def get_interval_days(self):
        """
        保有日数を数値で返す
        """
        return (date.today() - self.base_date).days


if __name__ == '__main__':
    # my_rare_metal = MyMetal('golden', 10, 100)

    my_gold_date = date(2020, 1, 1)
    my_gold = MyMetal('gold', 15, 175000, my_gold_date)
    print(str(my_gold))
    my_gold_status = my_gold()
    print(my_gold_status)
    print(my_gold.get_expected_total_price())
    my_gold.sell(10)

    my_silver = MyMetal('silver', 2000, 320000)

    print(my_gold.weight)
