#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/14 14:25
# filename: 多态性2.py

# class Canvas:
#     def draw_pric(self, shaps):
#         print("开始绘图".center(100, "-"))
#         shaps.shop(self)

def draw_pric(shaps):
    print("开始绘图".center(100, "-"))
    shaps.shop()


class Rectangle:
    def __init__(self, name):
        self.name = name

    def shop(self):
        print("在{}上绘制矩形".format(self.name))


class Triangle:
    def __init__(self, name):
        self.name = name

    def shop(self):
        print("在{}上绘制三角形".format(self.name))


class Circle:
    def __init__(self, name):
        self.name = name

    def shop(self):
        print("在{}上绘制圆形".format(self.name))

# c = Canvas()
#
# hu = Rectangle()
#
# # 传入Rectangle参数绘制矩形
# c.draw_pric(Rectangle())
#
# # 传入Triangle参数绘制三角形
# c.draw_pric(Triangle())
#
# #传入Circle参数绘制圆形
# c.draw_pric(Circle())


juxing = Rectangle("白纸上")
sanjiaoxing = Rectangle("黑板上")
yuanxing = Rectangle("衣服上")

draw_pric(juxing)
draw_pric(sanjiaoxing)
draw_pric(yuanxing)