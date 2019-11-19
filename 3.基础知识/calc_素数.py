#!/usr/bin/env python
#-*- coding:utf8 -*-
x = (int(input("请输入开始的数：")),int(input("请输入结束的数：")))
x1 = min(x)
x2 = max(x)
for n in range(x1,x2+1):
    for i in range(2, n-1):
        if n % i == 0:
            break
    else:
        print(n,"是素数。")
