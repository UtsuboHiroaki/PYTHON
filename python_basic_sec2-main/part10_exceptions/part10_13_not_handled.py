a = 100
b = 0
try:
    result = a / b
except TypeError:
    print('TypeError 例外が発生しました。')

print('try ... except ... else ... finally の一連のプロックから抜けました')
