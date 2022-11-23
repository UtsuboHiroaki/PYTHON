class MyClass:
    @classmethod
    def some_class_method(cls):
        print('class method が呼ばれました')

    def __init__(self, *args, **kwargs):
        print('init が呼ばれました')

    def __call__(self, **kwargs):
        print('call が呼ばれました')

    def some_instance_method(self):
        print('instnace method が呼ばれました')


# クラスメソッドの呼び出し
MyClass.some_class_method()

# インスタンスの生成
my_object = MyClass()

# インスタンスの呼び出し
my_object()

# インスタンスメソッドの呼び出し
my_object.some_instance_method()
