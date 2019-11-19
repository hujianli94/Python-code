#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
1.实例方法
2.类方法
3.静态方法
"""


#类中的方法都是实例方法
#定义静态方法需要用@staticmethod进行修饰
#定义类方法需要使用装饰器@classmethod进行修饰

class DemoMthd:
    @staticmethod           #静态方法不要传入self，类.方法名调用/实例名.方法名调用
    def static_mthd():
        print("调用静态方法！")

    @classmethod
    def class_mthd(cls):
        print("调用了类方法！")
DemoMthd.static_mthd()        # 未实例化，通过类名进行调用静态方法
DemoMthd.class_mthd()         # 未实例化，通过类名调用类方法
print("".center(100,"*"))
print("实例化类之后，调用静态方法和类方法.")
hu = DemoMthd()
hu.static_mthd()        #通过类实例调用静态方法
hu.class_mthd()         #通过类实例调用类方法

