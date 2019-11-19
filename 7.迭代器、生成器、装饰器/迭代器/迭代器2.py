#!/usr/bin/env python
#-*- coding:utf8 -*-】
class Counter:
    '''
    定义用于计数的类
    '''
    def __init__(self,x=0):
        #定义构造函数，初始化实例属性x
        self.x = x

counter = Counter()  #实例化类

def used_iter():
    #修改计数类中实例属性的值
    counter.x +=2
    return counter.x

for i in iter(used_iter,8):         #8为哨兵，迭代到8立刻停止
    print("本次遍历的数值：{}".format(i))

