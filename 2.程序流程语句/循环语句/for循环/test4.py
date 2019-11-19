#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/5 18:33
# filename: test4.py
for item in range(1, 20, 2):
    print("Count is :{}".format(item))

print("-----------------------------------")
for item2 in range(0, -20, -3):
    print("Count is {}".format(item2))

alst = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, alst)))
