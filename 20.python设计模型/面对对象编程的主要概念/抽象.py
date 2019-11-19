#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
    它提供一个简单的客户端接口，客户端可以通过该接口与类的对象进行交互，并可以
    调用该接口中定义的各个方法

    它将内部类的复杂性抽象为一个接口，这样客户端就不需要知道内部是如何实现的了
'''

class Base(object):
    def __init__(self):
        '''
        构造方法，self.sum初始值为0
        :return:
        '''
        self.sum = 0
    def add(self,vlaue):
        """
        :param vlaue: 带一个参数的方法
        :return:self.sum = self.sum + vlaue
        """
        self.sum += vlaue

acc = Base()
for i in range(10):
    #累加10以内的数值之和
    acc.add(i)

print(acc.sum)