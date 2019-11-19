#自定义异常
class xError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

#定义一个会抛出xError的方法
def call(xName):
    if xName=='牛牛':
        raise xError('严重错误！不许给牛牛打电话！：P')
    else:
        print('确定要给',repr(name),"打电话吗？")

#调用call方法
try:
    name=input("请问您要跟谁打电话？")
    call(name)
except xError as e:
    print(e.value)
    raise


