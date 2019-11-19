#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 23:00
# filename: 多重继承2.py
class Item:
    def info(self):
        print("Item中方法：", "这是一个商品")


class Product:
    def info(self):
        print("Product中方法：", "这是一个工业商品")


# 开始多继承1
class Mouse_I(Item, Product):
    pass


# 开始多继承2
class Mouse_P(Product, Item):
    pass


hu = Mouse_I()
hu.info()       #Item中方法： 这是一个商品

hu2 = Mouse_P()
hu2.info()      #Product中方法： 这是一个工业商品
