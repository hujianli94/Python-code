#!/usr/bin/env python
#-*- coding:utf8 -*-
Var1_name = "hujianli_Var1"
def change_local():
    Var1_name = "hujianli_local_Var1"
    #打印局部命名空间的字典
    print("locals:",locals())

print(Var1_name)

#打印全局命名空间的字典
change_local()
print("global: ", globals())