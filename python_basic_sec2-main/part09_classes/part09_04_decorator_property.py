class Metal:
    type_name = "sliver"
    total_price = 10000
    total_weight = 2000

    @property
    def per_gram_price(self):
        """ 1グラムあたりの単価を返す """
        return self.total_price / self.total_weight

    def add(self, price, weight):
        self.total_price += price
        self.total_weight += weight


my_sliver = Metal()

print(my_sliver.total_weight, my_sliver.total_price)

result = my_sliver.per_gram_price
print(result)

my_sliver.add(price=10000, weight=3000)

print(my_sliver.total_weight, my_sliver.total_price)

result = my_sliver.per_gram_price
print(result)
