#!/usr/bin/env python
# -*- coding:utf8 -*-
class PyQueue:
    # 创建队
    def __init__(self, size=20):
        self.queue = []  # 队
        self.size = size  # 队大小
        self.end = -1  # 尾队

    def setSize(self, size):
        # 设置队大小
        self.size = size

    def In(self, element):
        # 入队
        if self.end < self.size - 1:
            self.queue.append(element)
            self.end = self.end + 1
        else:
            raise QueueException("PyQueueEmpty")

    def Out(self):
        # 出队
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end - 1
            return element
        else:
            raise QueueException("PyQueueEmpty")

    def End(self):
        # 输出尾队
        return self.end

    def empty(self):
        # 清除队
        self.queue = []
        self.end = -1


class QueueException(Exception):
    # 自定义异常类
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


if __name__ == '__main__':
    queue = PyQueue()
    print("入队10个元素")
    for i in range(10):
        queue.In(i)  # 元素入队
    print()
    print("输出队尾的元素：")
    print(queue.End())  # 输出尾队
    print()
    print("出队10个元素")
    for i in range(10):
        print(queue.Out())  # 元素出队
    print()
    print("入队20个元素")
    for i in range(20):
        queue.In(i)  # 元素入队
    print()
    print("出队20个元素")
    for i in range(20):  # 引发异常，队为空队
        print(queue.Out())
    print()
    print("清空队列....")
    queue.empty()       #清空队
