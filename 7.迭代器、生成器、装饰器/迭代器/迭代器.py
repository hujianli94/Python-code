#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
__iter__() 方法返回对象本身，是for遇见使用迭代器的要求
__next__() 方法返回容器中下一个元素或数据，当容器中数据用尽时，引发StopIteration异常
"""
#自定义迭代器
class MyIterator:
    def __init__(self,x=2,xmax=100):
        '''
        定义构造方法，初始化属性
        '''
        self.__mul,self.__x = x,x
        self.__xmax = xmax

    def __iter__(self):
        """
        :return:定义迭代器协议方法，返回类本身
        """
        return self

    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration

if __name__ == '__main__':
    myiter = MyIterator()
    for i in myiter:
        print("迭代器的数据元素为{}".format(i))