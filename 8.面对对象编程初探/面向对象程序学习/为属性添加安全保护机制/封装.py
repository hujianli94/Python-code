#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 16:59
# filename: 封装.py
class User:
    def __hide(self):
        return ("示范隐藏的hide方法")

    def getname(self):
        return self.__name

    def setname(self,name):
        if len(name) <3 or len(name) > 8:
            raise ValueError("用户名长度必须在3~8之间")
        self.__name = name

    name = property(getname,setname)



    def setage(self,age):
        if age < 18 or age > 70:
            raise ValueError("用户年龄必须在18~80之间")
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)



if __name__ == '__main__':
    u = User()
    u.name = "hujianli"
    u.age = 19
    print(u.name)
    print(u.age)
    print(dir(u))
    print(u._User__hide())