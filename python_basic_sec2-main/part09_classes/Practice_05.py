class Stock:
    def __init__(self, stock_code, total_price, amount, **kwargs):
        self.stock_code = stock_code
        self.total_price = total_price
        self.amount = amount

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_pre_unit_price(self):
        """1株あたりの価格を算出する"""
        return self.total_price / self.amount
    def add(self, new_amount, new_todal_price):
        """追加で入手した株の値段と数量を追加する"""
        self.amount += new_amount
        self.total_price += new_todal_price

    def __call__(self, *args, **kwargs):
        """インスタンスを関数のように呼び出す"""
        return f'{self.get_pre_unit_price()}円相当の{self.stock_code}を有しています'

    def __str__(self):
        return f'銘柄コ－ド {self.stock_code} {self.amount}株 {self.total_price}円'

    def __repr__(self):
        f"Metal({self.stock_code}, {self.amount}, {self.total_price})"

    def __add__(self, other):
        return  self.total_price + other.total_price

    def __sub__(self, other):
        return self.total_price - other.total_price

stock_3987 = Stock('3987', 19*pow(10,3), 100,
                   data = '2022-11-06', store="SMBC日興證券", memo='真理子',)

print('終了しました')