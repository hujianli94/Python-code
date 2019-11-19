#对象示例
from Xcake import Xcake                             #引入类
cake1=Xcake()                                       #实例化
print("这个蛋糕有：",cake1.colorNumber,"种颜色")    #使用对象的属性
print("蛋糕的颜色有：",cake1.color)
print("吃蛋糕时，它会说：",cake1.eat())             #使用对象的方法
print("出售时，它会说：",cake1.sell())
