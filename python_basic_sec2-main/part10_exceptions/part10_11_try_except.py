a = 100
b = 0
try:
    result = a / b
except ZeroDivisionError:
    print('ZeroDivisionError 例外が発生しました。')
except:
    print('想定外の例外が発生しました。')
else:
    print('例外は発生しませんでした。')
finally:
    print('処理を終了します。')

print('try ... except ... else ... finally の一連のプロックから抜けました')
