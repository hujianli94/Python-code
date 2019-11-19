#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/12 11:43
# filename: example02.py

class Queue():
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        """
        返回队列信息
        :return:
        """
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self, item):
        """
        程序入队
        :param item:
        :return:
        """
        self.entries.append(item)
        self.length = self.length + 1

    def get(self):
        """
        程序出队
        :return:
        """
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        # self.front-=1
        # self.entries = self.entries[self.front:]
        self.entries = self.entries[1:]
        return dequeued

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def front(self):
        return self.entries[0]

    def size(self):
        """
        获取队列长度大小
        :return:
        """
        return self.length


if __name__ == '__main__':
    hu = Queue()
    for i in range(1, 100):
        hu.put(i)  # 程序入队，先进先出

    print(hu)       # 查看队列信息

    for i in range(hu.size()):
        print(hu.get())  # 程序出队

