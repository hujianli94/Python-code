#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 22:53
# filename: while和for最后加else.py
i = 0

while i * i < 10:
    i += 1
    print("{0}*{0}={1}".format(i, i * 1))
else:
    print("while Over!")

print("".center(10, "*"))


# 当for循环中条件满足break语句执行时，程序不会进入else语句，不会输出“for over”
for i in range(10):
    if i == 3:
        break
    print("Count is :{0}".format(i))
else:
    print("for Over!")
