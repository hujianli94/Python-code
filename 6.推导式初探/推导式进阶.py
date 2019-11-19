#!/usr/bin/env python
#-*- coding:utf8 -*-
#获得一个1~10中所有数的平方，且平方值为偶数的一个列表
square_odd = [i**i for i in range(1,11) if i**i %2 == 1]
print(square_odd)
