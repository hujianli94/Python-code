#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
1.实例属性
2.类属性
"""


class Demo_Property:
    class_name = "hujianli_class"  # 定义类属性

    def __init__(self, x=0):
        self.x = x  # 实例属性

    def class_info(self):
        print("类属性是{}".format(Demo_Property.class_name))
        print("实例属性是{}".format(self.x))

    def chang(self, x):
        'update class实例属性'
        self.x = x

    def chang_cn(self, name):
        Demo_Property.class_name = name




testa = Demo_Property()
testb = Demo_Property()
print("初始化两个实例：")
testa.class_info()
testb.class_info()
print("-" * 100)
print('修改testa实例变量：')
testa.chang(3)
testa.class_info()
testb.class_info()
print("-" * 100)
print('修改testb实例变量：')
testb.chang(10)
testa.class_info()
testb.class_info()
print("-" * 100)
print('修改testa类变量：')
testa.chang_cn(30)
testa.class_info()
testb.class_info()
print("-" * 100)
print('修改testb类变量：')
testb.chang_cn(100)
testa.class_info()
testb.class_info()
