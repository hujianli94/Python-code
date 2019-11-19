#类的继承实验
from Derive import *
cake1=Cake()                    #Cake类的对象
cake2=Xcake()                   #Xcake类的对象
cake3=XcakePlus(12,2)           #XcakePlus类的对象

#展示Cake的特征
cake1.showClass()               #显示类名
print("名称：",cake1.name)
print("Cake中定义的eat方法：",cake1.eat())
print("Cake中定义的preview方法：",cake1.preview())
print()

#展示Xcake的特征
cake2.showClass()               #显示类名
print("名称：",cake2.name)
print("新的属性shape：",cake2.shape)
print("新的方法drink：",cake2.drink())
print("继承自父类Cake的方法preview：",cake2.preview())
print()

#展示XcakePlus的特征
cake3.showClass()               #显示类名
print("名称：",cake3.name)
print("继承来的属性color：",cake3.color)
print("新的属性price=",cake3.price)
print("执行继承自父类的eat方法：",cake3.eat())
print("执行新的方法sumPrice：")
cake3.sumPrice()
print("执行重写的方法preview：")
cake3.preview()
print("执行继承自父类Cake的preview方法：")
print(Cake.preview(cake3))      #使用类名调用类方法
