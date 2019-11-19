#!/usr/bin/env python
#-*- coding:utf8 -*-
class DaYan(object):
    def __init__(self,yumao,hui,eyes):
        self.yumao = yumao
        self.hui = hui
        self.eyes = eyes

    def fly(self):
        print("我的特性是：羽毛：{}，喙:{},眼睛：{}".format(self.yumao,self.hui,self.eyes))
        print("我是{}，我的方法是{}".format(str(self.__class__).strip("<").strip(">").strip("'").split(".")[1], "fly...."))

    def Jump(self, jump="我会跳起来"):
        print("我的特性是{}".format(jump))

hu = DaYan("灰色","尖尖的","红色")
hu.fly()
hu.Jump("jump....")
hu.Jump()