#!/usr/bin/env python
#-*- coding:utf8 -*-
#hassattr()和setattr()
'''
hasattr(object,name)  #测试某个对象是否有某个属性
    object:被测试的对象（类或函数等）
    name:属性名（字符串格式）
'''

'''
setattr(object,name,value)
    object:要设置的对象（类或函数等）
    name:要设置的属性名（字符串格式）
    value:要设置的属性值
'''
class DemoClass:
    class_val = 3
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.info()

    def info(self):
        print("类属性class_val:",DemoClass.class_val)
        print("实例属性x:",self.x)
        print("实例属性y:",self.y)

if __name__ == '__main__':
    dc = DemoClass()
    if hasattr(DemoClass,"class_val"):
        setattr(DemoClass,'class_val',1000)   #设置类属性的值
    if hasattr(dc,"x"):
        setattr(dc,"x","xxxxxxxx")            #设置实例设置的值
    if hasattr(dc,"y"):
        setattr(dc,'y','yyyyyyyy')
    dc.info()
    setattr(dc,'z','zzzzzzzzz')             #添加并设置实例属性的值
    print('添加的属性z：', dc.z)