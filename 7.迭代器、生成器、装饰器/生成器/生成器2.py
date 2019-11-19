#!/usr/bin/env python
#-*- coding:utf8 -*-

def myYield(n):
    '''
    :return:rcv用来接收调用者传来的值
    '''
    while n >0:
        rcv = yield n       #rcv用来接收调用者传来的值
        n -=1
        if rcv is not None:
            n = rcv

if __name__ == '__main__':
    my_yield = myYield(3)
    print(my_yield.__next__())
    print(my_yield.__next__())
    print("传给生成器一个值，重新初始化生成器")
    print(my_yield.send(10))
    print(my_yield.__next__())