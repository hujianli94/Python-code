#!/usr/bin/env python
#-*- coding:utf8 -*-

#向字典里面添加元素
dict1 = {"1":"hujianli","2":"xiaojian","3":"xiaojian3"}
dict1["4"] = "xiaojian4"
print(dict1)

#修改字典的元素
dict1['1'] = "hujianli1"
dict1['2'] = "hujianli2"
print(dict1)

#删除元素
del dict1['1']
del dict1['2']

#进行判断，判断键是否在字典当中
if "1" in dict1:
    del dict1['1']
print(dict1)



