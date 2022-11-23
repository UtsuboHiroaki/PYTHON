from sub import func

print(f'{__file__} の __name__ は: {__name__}')
if __name__ == "__main__":
    print(f"{__file__} は直接呼び出されました")
    func()
