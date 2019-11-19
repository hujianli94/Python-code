#!/usr/bin/env python
#-*- coding:utf8 -*-
square = [i**i for i in range(1,11)]
print(square)

#字典推导式
keys = ["name","age","weight"]
values = ["hujianli",21,120]
dic_tuidao = {k:v for k,v in zip(keys,values)}
print(dic_tuidao)

