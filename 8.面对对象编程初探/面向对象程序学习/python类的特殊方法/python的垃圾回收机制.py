#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 15:24
# filename: python的垃圾回收机制.py
import gc


class Furit:
    def __init__(self, name, color):  # 初始化name、color属性
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color  # 返回color

    def setColor(self, color):
        self.__color = color  # 定义color

    def getName(self):
        return self.__name  # 返回name

    def Setname(self, name):
        self.__name = name  # 定义name


class FruitShop:
    def __init__(self):
        self.fruits = []

    def addFruit(self, fruit):
        """
        添加水果
        :param fruit:
        :return:
        """
        fruit.parent = self  # 把Fruit类关联到FruitShop类
        self.fruits.append(fruit)


if __name__ == '__main__':
    shop = FruitShop()
    shop.addFruit(Furit("apple", "red"))  # 向shop对象中添加两个fruit对象
    shop.addFruit(Furit("banana", "yellow"))
    print(gc.get_referrers(shop))  # 打印出shop关联的所有对象
    del shop
    print(gc.collect())  # 显示地调用垃圾回收器
