#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 15:17
# filename: 断言.py
s_age = input("请输入年龄：")
age = int(s_age)

assert 20 < age < 80
print("您输入的年龄在20和80之间")
