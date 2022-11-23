from sub.bond_sample import create_us_bond_instance, add_bond_price

us_bond = create_us_bond_instance(200000)

try:
    result = add_bond_price(us_bond, 200)
except AttributeError as e:
    print(e)

print('try ... except ... else ... finally の一連のプロックから抜けました')
