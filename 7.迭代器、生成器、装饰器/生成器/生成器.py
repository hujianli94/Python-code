#!/usr/bin/env python
#-*- coding:utf8 -*-

def myYield(n):
    '''
    定义一个生成器（03.函数）
    '''
    while n>0:
        print("开始生成......")
        yield n
        print("完成一次......")
        n -= 1
if __name__ == '__main__':
    for i in myYield(4):
        print("遍历得到的值：",i)
    print()

    my_yield = myYield(3)      #生成一个生成对象
    print("已经实例化生成器对象")
    my_yield.__next__()
    print("第二次调用__next__()方法：")
    my_yield.__next__()

