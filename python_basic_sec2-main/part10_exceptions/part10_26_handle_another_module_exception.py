from sub.another_module import func_z

try:
    func_z()
except ZeroDivisionError as e:
    print(e)
    print('ZeroDivisionError 例外をハンドルしました')
else:
    print('例外は発生しませんでした')
finally:
    print('処理を終了します')

print('try ... except ... else ... finally の一連のプロックから抜けました')
