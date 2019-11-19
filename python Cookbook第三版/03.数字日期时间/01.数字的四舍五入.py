#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/30 10:27
# filename: 01.数字的四舍五入.py
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.22355, 3))

# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面。比如：
a = 134546565
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

print()
# 格式化只是输出小数的宽度
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print("value is {:0.3f}".format(x))
