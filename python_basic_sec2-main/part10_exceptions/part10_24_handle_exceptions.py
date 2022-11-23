a = 100
b = 0
c = 'moji'
d = [1, 2, 3]

try:
    result = a / b
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
    print('ZeroDivisionError 例外をハンドルしました')
except TypeError as e:
    print(isinstance(e, TypeError))
    print(e)
    print('TypeError 例外をハンドルしました')
except Exception as e:
    print(isinstance(e, Exception))
    print(e)
    print('Exceptionをハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
