#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/21 9:14
# filename: print_test.py
class Foo(object):
    name = "类变量"

    def __init__(self, name):
        self.name = name

    # 实例方法
    def func(self):
        print(self.name)

    # 静态方法,如果方法中无需使用对象封装的值，可以使用静态方法
    @staticmethod
    def display():
        '''
        直接使用类名.方法名调用
        也可以实例化后，实例名.方法名调用
        :return:
        '''
        print("6666666")

    @classmethod
    def show(cls):
        """
        类方法，参数为cls，调用时使用类名.方法名.
        默认会将当前类传到参数中，
        如果在方法中会使用到当前类，就可以使用类方法。
        :return:
        """
        print("类方法")
        print("类方法调用:", cls.name)


if __name__ == '__main__':
    obj = Foo("李雷和韩梅梅")
    obj.func()          # 实例方法
    Foo.display()       # 静态方法
    Foo.show()          # 类方法
