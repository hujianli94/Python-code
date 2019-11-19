#!/usr/bin/env python
#-*- coding:utf8 -*-
#定义一个函数，求绝对值
def func(x,y):
    return (abs(x),abs(y))

class Ant:
    """
    定义类
    """
    def __init__(self,x=0,y=0):
        """
        构造方法
        :param x: 0
        :param y: 0
        :return:
        """
        self.x = x
        self.y = y
        self.disp_potion()          #用属性调用自身的方法

    def move(self,x, y):
        """
        :param x: 过绝对值函数后的x值
        :param y: 过绝对值函数后的y值
        :return:
        """
        x,y = func(x, y)        #调用外部函数
        self.edit_potion(x, y)
        self.disp_potion()

    def edit_potion(self, x, y):
        """
        对初始值0修改，进行+，加的值是edit方法的2个参数
        :param x:
        :param y:
        :return:
        """
        self.x += x
        self.y += y

    def disp_potion(self):
        print("当前位置{} {}".format(self.x,self.y))


hujianli = Ant()
hujianli.move(2,4)
hujianli.move(-9,6)