#!/usr/bin/env python
#-*- coding:utf8 -*-
# 把User类创建的过程委托给元类去做，这样代码的分离性比较好

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "test"

if __name__ == '__main__':
    #python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建User类
    my_obj = User(name="derek")
    print(my_obj)    #test