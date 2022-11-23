from .deep_module import func_in_deep_module
from ..related import func_in_related
# from ...sub import func1, func2, func3


def func_in_base():
    print("func_in_base() が呼び出されました")


func_in_deep_module()
func_in_related()
