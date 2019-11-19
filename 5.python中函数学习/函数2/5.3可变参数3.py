#!/usr/bin/env python
#-*- coding:utf8 -*-
def sign(**sign):
    for key,value in sign.items():
        print(key,'的星座是:',value)
    print()
dict1 = {"胡建力":'巨蟹座'}

dict2 = {'小健':"狮子座", '小胡':'双子座', '建力':'巨蟹座'}
sign(**dict1)       #解包，收集参数
sign(**dict2)