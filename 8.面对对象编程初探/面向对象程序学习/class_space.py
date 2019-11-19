#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 17:34
# filename: class_space.py

class User:
    name = "hujianli"
    def walk(self):
        print(self,"正在慢慢的行走")


#通过类调用实例方法
User.walk("hujianli")

hu = User()
User.walk(hu.name)