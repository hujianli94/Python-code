#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/21 9:42
# filename: print_test.py

class Foo(object):
    def __init__(self):
        pass

    @staticmethod
    def __display(arg):
        print("私有方法", arg)

    def func(self):
        return self.__display("123")

    @staticmethod
    def get_display():
        return Foo.__display("789")

    def __str__(self):
        pass


if __name__ == '__main__':
    obj = Foo()
    # print(dir(obj))
    obj._Foo__display("456")        #通过这种方式也可以方法
    # obj.__display()     #无法访问
    obj.func()

    Foo.get_display()
