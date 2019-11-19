#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/14 13:59
# filename: 使用metaclass.py

# metaclass类的__new__方法的作用就是：当丞相使用class定义新类时，如果指定了metaclass，那么metaclass的__new__方法就会被自动执行

class ItemMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # 为该类动态添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)


# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ["name", "price", "_discount"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义CellPhone
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ["price", "_discount"]

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


if __name__ == '__main__':
    b = Book("python入门到精通", 99)
    b.discount = 0.95
    # 创建Book对象的cal_price()方法
    print(b.cal_price())

    hu = CellPhone(2000)
    hu.discount = 0.85
    # 创建CellPhone对象的cal_price()方法
    print(hu.cal_price())
