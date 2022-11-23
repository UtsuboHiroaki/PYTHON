a = 100
b = 0

try:
    result = a / b
except Exception as e:  # Exception は、すべての例外の親クラス
    print(isinstance(e, ZeroDivisionError))  # True
    print(isinstance(e, ArithmeticError))  # True
    print(isinstance(e, Exception))  # True
    print(e)  # e.__str__() の結果
    print('Exceptionをハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
