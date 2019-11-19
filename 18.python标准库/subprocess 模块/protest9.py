#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/26 11:41
# filename: protest9.py
a = input()
a = a.split(" ")
a[0] = str(int(a[0])+1)
print(" ".join(a))