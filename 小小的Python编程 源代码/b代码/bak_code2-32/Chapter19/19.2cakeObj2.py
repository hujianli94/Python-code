#对象示例2
from Xcake import XcakePlus                         #引入类

#创建对象
cake1=XcakePlus(12,2)                               #实例化

#直接使用类变量
print("品种：",XcakePlus.name)
print("单价：",XcakePlus.price)

#展示对象的方法
cake1.preview()
cake1.sumPrice()
