#!/usr/bin/env python
#-*- coding:utf8 -*-
#定义装饰类的装饰器，采用的方法是：定义内嵌类的函数，返回新类

#定义一个类装饰器及其使用的例子
def abc(myclss):
    class InnerClass:
        def __init__(self, z=0):
            self.z = 0
            self.wrapper = myclss()     #实例化被装饰的类

        def position(self):
            self.wrapper.position()
            print('z axis:',self.z)
    return InnerClass                   #返回新定义的类


'''
定义一个能够装饰类的装饰器abc，定义了一个内嵌类InnerClass用于代替被装饰的类，并返回新的内嵌类，实例化普通类
之后，得到的就是被装饰器装饰后的类
'''
@abc
class coordination:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        print("x axis:", self.x)
        print("y axis:", self.y)

if __name__ == '__main__':
    coor = coordination()
    coor.position()