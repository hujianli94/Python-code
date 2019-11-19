#!/usr/bin/env python
#-*- coding:utf8 -*-
color = ['red','green','blue']

values = [1,2,3,4]

for i,j in zip(color,values):
    print((i,j))


def add(x,y):
    return x+y
hu = (4,5)

print(add(*hu))


dot = [(1,2),(3,4),(5,6)]

x,y = zip(*dot)
print(x)
print(y)



m = [[1,2],[3,4],[5,6]]
print(list(zip(*m)))

#求2个列表的最大值
a = [1,2,3,4,5,6]
b = [2,3,4,5,6,7]
print(list(map(lambda pair:max(pair),zip(a,b))))

