#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:41
# filename: 10.如何实现用户的历史记录功能.py

"""
使用容量为n的队列存储历史记录

使用deque双端循环队列存储历史记录（deque是保存到内存中，下次启动历史记录会消失）
如果想保存到硬盘中，使用pickle模块，以便下次启动使用
"""

from random import randint
from collections import deque
import pickle


def guess(n, k):
    if n == k:
        print('猜对了，这个数字是%d' % k)
        return True
    if n < k:
        print('猜大了，比%d小' % k)
    elif n > k:
        print('猜小了，比%d大' % k)
    return False


def main():
    n = randint(1, 100)
    i = 1
    hq = deque([], 5)
    while True:
        line = input('[%d]请输入一个数字：' % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(n, k):
                break
        elif line == 'quit':
            break
        elif line == 'history':
            print(hq)


if __name__ == '__main__':
    main()
