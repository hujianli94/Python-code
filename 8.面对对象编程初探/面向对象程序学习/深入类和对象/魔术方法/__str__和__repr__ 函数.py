#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
__str__()
__repr__()
'''

class Ppersopn(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "age:{0} name:{1} height:{2} weight:{3}".format(self.name,self.age,self.height,self.weight)

per =Ppersopn("hanmeimei", 18, 170, 60)
print(per)

'''
___str__()调用时使用，是给用户用的，是一个描述对象的方法
__repr__()给机器用的，在python解释器里面直接敲对象名称在
回车后调用的方法，
注意:在没有str时，且有__repe__  str=repr

当一个对象的属性值很多，都需要打印时，
重写了__str__后，简化了代码
'''