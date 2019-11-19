#!/usr/bin/env python
#-*- coding:utf8 -*-
class Ant:

    def __init__(self, x=0, y=0, color="black"):  #定义构造方法，将实例属性和参数一一绑定
        self.x = x
        self.y = y
        self.color = color

    def crawl(self,x,y):
        self.x = x
        self.y = y
        print("爬行....")
        self.info()

    def info(self):
        print("当前位置({}，{})".format(self.x, self.y))

    def attack(self):
        '模拟攻击'
        print("用嘴咬")

class FlyAnt(Ant):
    '''
    定义FlyAnt类，继承Ant类
    '''
    def attack(self):
        '修改行为，攻击方法不同'
        print("用尾针..！")

    def fly(self,x,y):
        print("飞行.....")
        self.x = x
        self.y = y
        self.info()
flyant = FlyAnt(color="red")   #实例化类
flyant.crawl(3,5)              #模拟爬行
flyant.fly(20,30)              #模拟飞行
flyant.attack()                #模拟攻击
