from .bond import Bond


def create_us_bond_instance(price):
    return Bond('米国債', price)


def add_bond_price(bond, price):
    return bond + price
