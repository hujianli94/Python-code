#!/usr/bin/env python
#-*- coding:utf8 -*-
adct = {"a":1,"b":2}
print(adct)

'''
print(adct.get("a"))  #获取a的值
print(adct.get("d","hujianli")) #获取不存在键时对应的值

print(adct.items()) #返回字典的键值对

print(adct.keys())  #返回字典的键
print(adct.values())    #返回字典的值
'''
adct.update({"b":12})
print(adct)    #使用另外一个字典存在的键去更新adct字典

