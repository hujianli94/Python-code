#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/20 16:36
# filename: 继承中self的使用.py

class Base1:
    def f1(self):
        print("Base1:f1")

    def f2(self):
        print("Base1:f2")


class Base2:
    def f1(self):
        print("Base2:f1")

    def f2(self):
        print("Base2:f2")

    def f3(self):
        print("Base2:f3")
        self.f1()


class Foo(Base1, Base2):
    def f0(self):
        print("Foo:f0")
        self.f3()


if __name__ == '__main__':
    obj = Foo()
    obj.f0()

#遵循原则，多继承先找左边
# self是实例化的实例，先从实例后的实例里面开始找