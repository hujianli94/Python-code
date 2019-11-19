#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/15 16:14
# filename: __dir__方法.py
"""
查看内置属性和方法和所有定义的属性和方法组成列表。
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        pass


if __name__ == '__main__':
    im = Item("鼠标", 29.8)
    print(im.__dir__())
    print(dir(im))
