#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 7:25
# filename: 实例方法test.py
class Animal(object):
    '''
    定义动物类
    '''

    def __init__(self, age, sex=1, weight=0.0):
        # 定义实例变量
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        """
        定义吃方法
        :return:
        """
        self.weight += 0.5
        print("eat.......")

    def run(self):
        """
        定义跑方法
        :return:
        """
        self.weight -= 0.01
        print("run......")


if __name__ == '__main__':
    a1 = Animal(2, 0, 10.0)
    print("a1体重：{0:0.2f}".format(a1.weight))
    a1.eat()
    print("a1体重：{0:0.2f}".format(a1.weight))
    a1.run()
    print("a1体重：{0:0.2f}".format(a1.weight))

