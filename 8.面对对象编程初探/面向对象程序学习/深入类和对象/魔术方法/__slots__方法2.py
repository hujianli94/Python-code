#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/14 13:02
# filename: __slots__方法2.py

class Dog:
    __slots__ = ["walk", "walk2", "age", "name"]

    def __init__(self, name):
        self.name = name


def hujianli(self):
    print("预先定义的hujianli方法")
    print("【{}】正在慢慢走向你".format(self.name))


# __slots__属性指定的限制只对当前的类的实例起作用，对子类不起作用。
class GunDog(Dog):
    def __init__(self,name):
        super(GunDog, self).__init__(name)
        pass


hujianli_Class = GunDog("hujianli")
hujianli_Class.speed = 99
print(hujianli_Class.speed)