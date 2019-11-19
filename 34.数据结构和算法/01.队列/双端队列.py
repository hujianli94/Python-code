#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/28 21:05
# filename: 双端队列.py
class Deque:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        """
        :return: 清空队列
        """
        return self.item == []

    def addFront(self, item):
        """
        :param item: 插入值
        :return: 在队列尾部插入
        """
        self.item.append(item)

    def addRear(self, item):
        """

        :param item: 插入值
        :return: 在队列首部插入
        """
        self.item.insert(0, item)

    def removeFront(self):
        """
        :return: 返回队列尾部值
        """
        return self.item.pop()

    def removeRear(self):
        """
        :return: 返回队列首部值
        """
        return self.item.pop(0)

    def size(self):
        """
        :return: 返回队列长度
        """
        return len(self.item)


if __name__ == '__main__':
    hu = Deque()
    print(hu.isEmpty())
    hu.addRear(4)
    hu.addFront("dog")
    hu.addFront("cat")
    hu.addFront(True)
    print(hu.size())
    print(hu.isEmpty())
    hu.addRear(8.8)
    print(hu.removeRear())
    print(hu.removeFront())
