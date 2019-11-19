#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/11 16:39
# filename: 双端队列.py
from collections import deque

#元素入栈
stack = deque(("Kotln", "Python"))
stack.append("hujianli01")
stack.append("hujianli02")
print("stack入栈后的元素: ",stack)


#元素出栈，先进先出
print(stack.popleft())
print(stack.popleft())
print(stack.pop(0))
print("stack出栈后的元素:",stack)

