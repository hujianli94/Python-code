#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/20 14:17
# filename: math模块.py
import math

# 大于等于1.4的最小整数
print(math.ceil(1.4))

# 小于等于1.4的最小整数
print(math.floor(1.4))

# 1.4进行四舍五入
print(round(1.4))

print(math.ceil(1.5))
print(math.floor(1.5))
print(round(1.5))

print(math.ceil(1.6))
print(math.floor(1.6))
print(round(1.6))

print("*" * 100)
# 对数运算，math.log(a[,base])返回以base为底的a的对手，省略底数base，是a的自然数对数
print(math.log(8, 2))

# 幂运算，返回2的3次幂的值
print(math.pow(2, 3))

print(math.log(8))

# 返回1.6的平方根
print(math.sqrt(1.6))

"""
math 模块中提供的三角函数有如下几种。
    
    math. sin(a) ： 返回弧度a 的三角正弦。
    math.cos(a): 返回弧度a 的三角余弦。
    math.tan(a) ： 返回弧度a 的三角正切。  
    math.asin(a) ： 返回弧度a 的反正弦。
    math.acos(a) ： 返回弧度a 的反余弦。
    math.atan(a) ： 返回弧度a 的反正切。
上述函数中a 参数是弧度。有时需要将弧度转换为角度， 或将角度转换为弧度， math 模块中提供了弧度和角度函数。
    math.degrees(a) ： 将弧度a 转换为角度。
    math.radians(a) ： 将角度a 转换为弧度。
"""

print(math.degrees(0.5 * math.pi))
print(math.radians(180 / math.pi))
a = math.radians(45 / math.pi)
print(a)

print(math.sin(a))
print(math.asin(math.sin(a)))
print(math.asin(0.2474))
print(math.asin(0.24740395925452294))
print(math.cos(a))
print(math.acos(0.9689124217106447))
print(math.acos(math.cos(a)))
print(math.tan(a))
print(math.atan(math.tan(a)))
print(math.atan(0.255334192122103627))