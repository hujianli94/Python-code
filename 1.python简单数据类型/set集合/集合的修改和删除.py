#!/usr/bin/env python
#-*- coding:utf8 -*-
mr = set(['零基础学JAVA','零基础学Android',"零基础学PHP",'零基础学C语言'])    #定义一个集合
mr.add("零基础学python")        #向集合当中添加元素，会自动删除重复的元素
print(mr)

mr.pop()    #随机删除元素
#print(mr)


if "零基础学JAVA" in mr:
    mr.remove("零基础学JAVA")   #移除集合的元素
print(mr)


mr.clear()                      #清空整个集合
print(mr)


# del mr                        #删除整个集合
# print(mr)


#-------------------------------------------------
# python新增jianli3，C减去jianli3
#--------------------------------------------------
python = set(["hujianli","xiaojian","xiaojian2","xiaojian3"])
C = set(["jianli1","jianli2","jianli3","jianli4"])
python.add("jianli3")
C.remove("jianli3")
print(python)
print(C)
