class Stock:
    def __init__(self, stock_code, total_price, amount):
        self.stock_code = stock_code
        self.total_price = total_price
        self.amount = amount

    def get_pre_unit_price(self):
        """1株あたりの価格を算出する"""
        return self.total_price / self.amount

stock_3987 = Stock('3987', 40*pow(10, 3), 100)
print(stock_3987.stock_code, stock_3987.total_price, stock_3987.amount)

stock_1540 = Stock('1540', 75*pow(10, 3), 100)
print(stock_1540.stock_code, stock_1540.total_price, stock_1540.amount)

stock_1542 = Stock('1542', 81*pow(10, 3), 100)
print(stock_1542.stock_code, stock_1542.total_price, stock_1542.amount)

print('終了しました')