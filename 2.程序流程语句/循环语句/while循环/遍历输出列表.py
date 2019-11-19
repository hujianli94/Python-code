#!/usr/bin/env python
#-*- coding:utf8 -*-
alst = [1,2,3,4,5]
total = len(alst)

i = 0
while i < total:
    print("{} 的平方是{}".format(alst[i], alst[i]*alst[i]))
    i = i +1
else:
    print("循环结束 ！！")