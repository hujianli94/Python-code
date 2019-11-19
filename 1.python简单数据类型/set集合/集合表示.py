#!/usr/bin/env python
#-*- coding:utf8 -*-
#集合用来保存不重复的元素，最常用的是去重

#定义空的集合
set()       #set()函数可以将列表转换为集合


#集合的创建
set1 = {"水瓶座","射手座","双鱼座","双子座"}    #定义了一个集合，集合和字典一样，是无序的
print(set1)                                     #因为是无序的，所以无法通过索引来获取

set2 = {"水瓶座","射手座","双鱼座","双子座","水瓶座"}  #去重复了
print(set2)


python = {"hujianli1","hujianli2","hujianli3","hujianli4","xiaojian1"}
C = {"xiaojian1","xiaojian2","xiaojian3","xiaojian4"}
print(python | C)   #求并集
print(python & C)   #求交集
