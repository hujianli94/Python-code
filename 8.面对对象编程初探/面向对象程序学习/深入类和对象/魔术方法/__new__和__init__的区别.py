#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
__new__方法如果不返回对象，不会执行init方法
'''
'''
class User:
    def __new__(cls, *args, **kwargs):
        print("in new")

    def __init__(self,name):
        print("in init")
        self.name = name

# new是用用来控制对象的生成过程，在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
if __name__ == '__main__':
    user = User("derek")
'''


class User:
    def __new__(cls, *args, **kwargs):
        print("in new")         #in new
        print(cls)              #cls是当前class对象    <class '__main__.User'>
        print(type(cls))        #<class 'type'>
        return super().__new__(cls)   #必须返回class对象，才会调用__init__方法

    def __init__(self, name):
        print("in init")        #in init
        print(self)             #self是class的实例对象      <__main__.User object at 0x00000000021B8780>
        print(type(self))       #<class '__main__.User'>
        self.name = name

# new是用用来控制对象的生成过程，在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
if __name__ == '__main__':
    user = User(name="derek")

#总结
# __new__ 用来创建实例，在返回的实例上执行__init__，如果不返回实例那么__init__将不会执行
# __init__ 用来初始化实例，设置属性什么的
