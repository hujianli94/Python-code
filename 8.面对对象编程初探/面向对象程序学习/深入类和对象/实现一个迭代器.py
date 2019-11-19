#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/15 14:03
# filename: 实现一个迭代器.py
"""
for循环遍历列表、元祖和字典，属于一个迭代器
"""
'''
如果开发者要实现迭代器，只需要实现如下两个方法即可

__iter__(self):该方法返回一个迭代器（iterator），迭代器必须包含一个__next__()方法，该方法返回迭代器的下一个元素

__reversed__(self)：该方法主要为内建的reversed()反转函数提供支持，程序调用reversed()函数时，其实就是在使用
__reversed__此方法
'''


# 实现一个斐波拉契数列 f(n+2)=f(n+1)+f(n)

class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len

    # 定义迭代器所需的__next__方法
    def __next__(self):
        # 如果__len__属性为0，结束迭代
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        self.__len -= 1
        return self.first

    # 定义__iter__方法，该方法返回迭代器
    def __iter__(self):
        return self


# 创建Fibs对象
fibs = Fibs(10)
# print(next(fibs))
# print(fibs.__next__())
# print(fibs.__next__())

for i in fibs:
    print(i, end=" ")

# 将列表、元祖转换为迭代器
my_iter = iter(["千千厥歌", "hu", 'jianli', "python", "java"])
#依次获取迭代器的下一个元素
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())

for i in my_iter:
    print(i)