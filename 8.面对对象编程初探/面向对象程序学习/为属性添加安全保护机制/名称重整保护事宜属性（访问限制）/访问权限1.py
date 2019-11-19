#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
_foo        #protected 保护类型的成员，只允许类本身和子类可以访问，可以通过实例名称来访问.
            当 from modulename import * 时将不会引入以单下划线卡头的变量和函数
            单前置下划线,私有化属性或方法，禁止通过from modules import *导入,但是类对象和子类可以访问

__foo       #使用类型的成员，只允许定义它类本身可以访问，不可以通过实例名称来访问，需要使用dir()查看后访问
__foo__     #系统定义的名字，特殊的方法
'''

class Swan:
    '''
    天鹅类
    '''
    _neck_swan = '天鹅的脖子很长'      #受保护类型的属性
    __neck_swan2 = '天鹅的脖子很长'      #私有类型的属性


    def __init__(self):
        print('这是构造方法中受到保护类型的属性', Swan.__neck_swan2)  #访问保护类型的属性

    def my(self):
        print("my方法: ", Swan.__neck_swan2)

swan = Swan()   #创建Swan类的实例(对象)
print('直接访问:', swan._neck_swan) #通过实例类型来访问受保护类型的属性

print()
swan1 = Swan()
print('私有类型的属性： ', swan1._Swan__neck_swan2)

swan1._Swan__neck_swan2 = "我修改了私有属性,天鹅的脖子很很很长"
print('修改私有属性后：',swan1._Swan__neck_swan2)

print()
swan1.my()      #修改的私有属性，在方法中不会生效
