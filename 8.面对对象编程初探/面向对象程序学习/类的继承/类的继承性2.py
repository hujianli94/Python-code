#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 22:47
# filename: 类的继承性2.py
class Fruit:
    def info(self):
        '''实例方法'''
        print("我是一个水果！重{}克".format(self.weight))


class Food:
    def taste(self):
        '''实例方法'''
        print("不同食物的口感不同")


# 定义Apple类，继承了Fruit类和Food类
class Apple(Fruit, Food):
    pass


# 创建Apple对象
a = Apple()
a.weight = 5.6
#调用Apple类的info()方法
a.info()

#调用Apple类的teste()方法
a.taste()
