class Metal:
    type_name = "sliver"
    total_price = 10000
    amount = 2000

    def get_per_unit_price(self):
        """ 1グラムあたりの単価を返す """
        return self.total_price / self.amount


my_sliver = Metal()

print(my_sliver.amount, my_sliver.total_price)

result = my_sliver.get_per_unit_price()
print(result)
