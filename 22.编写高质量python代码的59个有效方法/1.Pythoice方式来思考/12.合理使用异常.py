#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 13:50
# filename: finally语句.py
"""
1.无论try块是否发生异常，都可利用try/finally复合语句中的finally块来执行清理工作
2.else块可以用来缩减try块中的代码块，并把没有发生异常时所要执行的语句与try/except代码块隔开
3.顺利运行try块后，若想使某些操作能再finally块的清理代码之前执行，则可将这些操作写到else中
"""