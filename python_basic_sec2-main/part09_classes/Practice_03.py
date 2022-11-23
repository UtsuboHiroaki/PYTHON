class Stock:
    def __init__(self, stock_code, total_price, amount):
        self.stock_code = stock_code
        self.total_price = total_price
        self.amount = amount

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
        f"Metal({self.type_name}, {self.amount}, {self.total_price})"

    def __add__(self, other):
        return  self.total_price + other.total_price

    def __sub__(self, other):
        return self.total_price - other.total_price

stock_3987 = Stock('3987', 19*pow(10, 3), 100)
stock_1540 = Stock('1540', 75*pow(10, 3), 100)
#call_result = stock_3987()

str_result_1 = str(stock_1540)
total_price = stock_3987 + stock_1540

sub_result = stock_3987 - stock_1540

#print(call_result)
#print(total_price)
print(sub_result)


print('終了しました')