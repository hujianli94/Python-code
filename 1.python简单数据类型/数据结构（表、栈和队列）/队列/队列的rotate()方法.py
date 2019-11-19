#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/11 16:47
# filename: 队列的rotate()方法.py
from collections import deque
q = deque(range(5))
print("q中的元素：",q)

#执行旋转，使之首尾相连
q.rotate()
print("q中的元素：",q)

#再次执行旋转，使之首尾相连
q.rotate()
print("q中的元素：",q)