#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/23 14:11
# filename: 1.threading001.py
"""
threading.actice_count():返回当前处于活动状态的线程个数
threading.current_thread():返回当前的Thread对象
threading.main_thread():返回主线程对象，主线程是Python解释器启动的线程

"""
import threading

#当前线程对象
t = threading.current_thread()
#当前线程名
print(t.name)

# 返回当前处于活动状态的线程
print(threading.active_count())

# 主线程名
print(t.name)
