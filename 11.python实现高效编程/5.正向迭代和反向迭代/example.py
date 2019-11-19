#!/usr/bin/env python
#-*- coding:utf8 -*-
L = [1,2,3,4,5,6]
L.reverse()     #反向迭代，改变了原列表的值
print(L)

L1 = [1,2,3,4,5,6]
L2 = L1[::-1]       #使用切片进行反向迭代
print(L1)
print(L2)
