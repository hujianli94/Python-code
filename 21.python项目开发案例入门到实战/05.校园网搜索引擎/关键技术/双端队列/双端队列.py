#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/15 11:06
# filename: 双端队列.py
from collections import deque

d = deque()  # 创建双端队列
d.append(3)
d.append(8)
d.append(1)
print(d)
print(len(d))
print(d[0])
print(d[-1])

print()
print()

d = deque(maxlen=20)
for i in range(30):
    d.append(str(i))
print(d)

d = deque(['1', '2', '3', '4', '5'])
d.extend([0])
print(d)
d.extendleft([8, 9])
print(d)

# 从后删掉一个元素
d.pop()
print(d)

# 从前删掉一个元素
a = d.popleft()
print(a)
