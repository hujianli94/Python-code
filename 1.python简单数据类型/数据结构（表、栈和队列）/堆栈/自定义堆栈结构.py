#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/19 9:27
# filename: 自定义堆栈结构.py

"""
定义一个堆栈数据结构
"""


class PyStack():
    def __init__(self, size=20):
        self.stack = []  # 用列表创建堆栈
        self.size = size  # 默认堆栈大小
        self.top = -1  # 栈顶的位置

    def push(self, element):
        """
        向堆栈中推入数据
        :return:
        """
        if self.is_Full():
            raise myException("Stack is full, unable to push data")
        else:
            self.stack.append(element)
            self.top += 1

    def pop(self):
        """
        向堆栈中移除数据
        :return:
        """
        if self.is_Empty():
            raise myException("Stack is Empty, unable to pop data")
        else:
            element = self.stack[-1]
            self.top = self.top - 1
            del self.stack[-1]
            return element

    def is_Empty(self):
        """
        判断是否为空栈
        :return:
        """
        if self.top == -1:
            return True
        else:
            return False

    def Top(self):
        """
        返回栈顶的位置
        """
        return self.top

    def is_Full(self):
        """
        判断是否为满栈
        :return:
        """
        if self.top == self.size - 1:
            return True
        else:
            return False

    def clear_Stack(self):
        """
        清空堆栈信息
        :return:
        """
        self.stack = []
        self.top = -1


class myException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


if __name__ == '__main__':
    mytest = PyStack()
    for i in range(10):
        mytest.push(i)
    print("栈顶的位置为：{}".format(mytest.Top()))
    print("开始出栈操作.....")
    for i in range(10):
        print(mytest.pop())

    print("清空堆栈.....")
    mytest.clear_Stack()

    # for i in range(21):   此处将引发异常
    #     mytest.push(i)

