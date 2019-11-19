#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 14:42
# filename: 02.类型检查.py

# 几何图形
class Figure:
    def draw(self):
        print("绘制Figure.......")


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print("绘制Ellipse.......")


# 三角形
class Triangle(Figure):
    def draw(self):
        print("绘制Trangle.........")


f1 = Figure()  # 没有发生多态
f1.draw()

f2 = Ellipse()  # 发生多态
f2.draw()

f3 = Triangle()  # 发生多态
f3.draw()

print(isinstance(f1, Triangle))
print(isinstance(f2, Triangle))
print(isinstance(f3, Triangle))
print(isinstance(f2, Figure))
