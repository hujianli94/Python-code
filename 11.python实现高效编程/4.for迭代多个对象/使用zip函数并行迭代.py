#!/usr/bin/env python
#-*- coding:utf8 -*-
from random import randint
chinease = [randint(10, 100) for _ in range(40)]
math = [randint(10, 100) for _ in range(40)]
English = [randint(10, 100) for _ in range(40)]

total = []
num = 1
for c,m,e in zip(chinease,math,English):
    print("学生{}的三科成绩如下："
          "语文：{} "
          "数学：{} "
          "英语：{}".format(num,c,m,e))
    print()
    num +=1
    total.append(c+m+e)
for nu, total1 in enumerate(total):
    print("学生{}：  总分：{}".format(nu+1,total1))


