class Bond:
    """
    資産クラス
    """
    type_name = 'asset'

    def __init__(self, type_name, total_price, ):
        self.type_name = type_name
        self.total_price = total_price

    def __add__(self, other):
        return self.total_price + other.total_price

