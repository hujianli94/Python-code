#!/usr/bin/env python
#-*- coding:utf8 -*-
class Duck():
    def __init__(self, input_name): #构造函数
        self.__name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.getter
    def set_name(self, put_name):
        print("开始设置属性:name的值")
        self.__name = put_name



if __name__ == '__main__':
    name = "hujianli"
    hu = Duck(name)
    print(hu.name)
    print("分割线".center(100, "-"))
    hu.set_name = "xiaojian"
    print(hu.name)
    print()
    print(hu._Duck__name)