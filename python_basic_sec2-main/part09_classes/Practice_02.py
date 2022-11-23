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

stock_3987 = Stock('3987', 19*pow(10, 3), 100)
print(stock_3987.stock_code, stock_3987.total_price, stock_3987.amount)
print(stock_3987.get_pre_unit_price())

stock_3987.add(100, 18*pow(10, 3))
print(stock_3987.stock_code, stock_3987.total_price, stock_3987.amount)
print(stock_3987.get_pre_unit_price())

print('終了しました')