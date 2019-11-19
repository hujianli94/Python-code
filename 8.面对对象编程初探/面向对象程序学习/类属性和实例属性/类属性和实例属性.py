#!/usr/bin/env python
#-*- coding:utf8 -*-

class DaYan(object):
    neck = "脖子较长"
    wing = "振翅频率较高"
    leg = "腿是身体的中心支点"       #类属性
    def __init__(self,yumao,hui,eyes):
        self.yumao = yumao
        self.hui = hui
        self.eyes = eyes

    def fly(self):
        print("我的特性是：羽毛：{}，喙:{},眼睛：{}".format(self.yumao,self.hui,self.eyes))
        print("我是{}，我的方法是{}".format(str(self.__class__).strip("<").strip(">").strip("'").split(".")[1], "fly...."))

    def Jump(self, jump="我会跳起来"):
        print("我的特性是{}".format(jump))

    def exterior(self):
        print("我是大雁类 "
              "我的外观是："
              "{}\n{}\n{}".format(DaYan.neck,DaYan.wing,DaYan.leg))

hu = DaYan("灰色","尖尖的","红色")
hu.fly()
hu.Jump("jump....")
hu.Jump()
hu.exterior()