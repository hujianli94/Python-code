#!/usr/bin/env python
#-*- coding:utf8 -*-

#编号迭代
for i,item in enumerate("hujianli"):
    print(" %s ----> %s " %(i,item))

#排序迭代
for i in sorted([3,2,7,6,8]):
    print(i)


#并行迭代,注意，当长度不一致时，只遍历最短的序列
a = [1,2,3,4]
b = ["hu","liu","zhang"]
for i,j in zip(a,b):
    print("%s:%s" %(i,j))