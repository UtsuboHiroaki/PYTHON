from asset_management.asset import Asset
from asset_management.mixins import DealsMixin


class PreciousMetal(DealsMixin, Asset):
    """ DealsMixin, Asset を継承した、貴金属クラス """
    type_name = 'metal'

    def __init__(self, type_name, base_price, total_weight):
        super().__init__(type_name, base_price * total_weight)
        self.total_weight = total_weight

    def __str__(self):
        return f'{self.type_name} {self.total_price} {self.total_weight}'

    def get_info(self):
        return f'{self.type_name} {self.total_weight}グラム 総額{self.total_price:,}円有しています。'


gold = PreciousMetal('gold', 8500, 50)
silver = PreciousMetal('silver', 100, 200)

gold_base_price = gold.check_current_base_price()
print(gold_base_price)

silver_base_price = silver.check_current_base_price()
print(silver_base_price)

gold_total_price = gold.get_total_current_price()
print(gold_total_price)

silver_total_price = silver.get_total_current_price()
print(silver_total_price)

gold_current_value = gold.compare_with_current_value()
print(gold_current_value)

silver_current_value = silver.compare_with_current_value()
print(silver_current_value)