#!/usr/bin/env python
#-*- coding:utf8 -*-
class Province:

    #静态字段
    country = "中国"

    def __init__(self,name):
        #普通字段
        self.name = name


#直接访问普通字段
hu = Province("hujianli")
print(hu.name)

#直接访问静态字段
print(Province.country)