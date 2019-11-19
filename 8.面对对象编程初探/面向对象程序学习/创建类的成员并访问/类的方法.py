#!/usr/bin/env python
#-*- coding:utf8 -*-

class smplclass:
    def info(self):
        print("我定义的类")

    def mycacl(self,x,y):
        return x + y


hu = smplclass()
print("调用info的方法！")
hu.info()
print("".ljust(50,"-"))
print("调用mycalc方法")
print(hu.mycacl(2,4))