#!/usr/bin/env python
#-*- coding:utf8 -*-
# 创建一个插口IntTuple，包含内置插口tuple，行为一致.tuple是一个不可变对象，所以我们不能从self来删除一些数据
class IntTuple(tuple):
    #__new__的参数是一个类对象，此时我们来修改它
    def __new__(cls,iterable):
        # 使用生成器对象
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)


    def __init__(self,iterable):
        # py2需要在__init__里面传参
        print(self) #此时已经创建好了
        super(IntTuple,self).__init__()


t = IntTuple([1,-1,'abc',6,['x','y'], 3])
print(t)
