#!/usr/bin/env python
#-*- coding:utf8 -*-
class Fruit():
    def grow(self):
        print("grow....")

def update():
    print("grow..........")

if __name__ == '__main__':
    fruit = Fruit()
    fruit.grow()
    fruit.grow = update     #使用update函数来更新方法
    fruit.grow()
