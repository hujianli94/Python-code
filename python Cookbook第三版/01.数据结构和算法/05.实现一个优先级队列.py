#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 16:38
# filename: 05.实现一个优先级队列.py
import heapq


class PriorityQueue:
    """
    定义一个优先级队列。 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
    """

    def __init__(self):
        # 定义一个初始化列表
        self._queue = []
        # 定义index值为0
        self._index = 0

    # 入队,队列和优先级
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Item({!r})".format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()  # 实例化类
    q.push(Item("foo"), 1)
    q.push(Item("hu"), 5)
    q.push(Item("jian"), 6)
    q.push(Item("li"), 1)

    # 第一个 pop() 操作返回优先级最高的元素,当出现相同优先级别的元素时，根据被插入的顺序返回
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())