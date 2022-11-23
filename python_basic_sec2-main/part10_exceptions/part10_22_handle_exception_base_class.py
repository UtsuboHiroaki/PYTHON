a = 100
b = 0

try:
    result = a / b
except ArithmeticError as e:  # ArithmeticError は、ZeroDivisionError の親クラス
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, ArithmeticError))  # True
    print(e)  # e.__str__() の結果
    print('ArithmeticError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
