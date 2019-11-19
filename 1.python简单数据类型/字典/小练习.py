#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 14:57
# filename: 小练习.py
submit = input("Please input String to tuple:")

submit_tuple = tuple(submit.split())
# print(submit_tuple)

print("".center(100, "*"))
print("输出元祖*3的结果为:")
print(submit_tuple * 3)


print("".center(100, "*"))
print("输出元祖+(fkjava,crazyit)的结果为:")
print(submit_tuple + ("fkjava", "crazyit"))
