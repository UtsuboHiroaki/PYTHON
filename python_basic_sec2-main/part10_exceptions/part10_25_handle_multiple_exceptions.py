a = 100
b = 0

try:
    result = a / b
except (ZeroDivisionError, TypeError) as e:
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, TypeError))  # True
    print(e)  # e.__str__() の結果
    print('ZeroDivisionError または TypeError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
