#!/usr/bin/env python
#-*- coding:utf8 -*-
falg = 9
num = 0
while num < falg:
    num +=1
    for i in range(1,num+1):
        print(num,"*",i,"=",num*i,end=" ")
    print(" ")

