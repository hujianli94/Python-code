#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 14:29
# filename: th_test001.py
from tkinter import *

#创建tk对象，tk代表窗口
root = Tk()

root.title("航海王")

# 创建label对象，第一个参数指定将该label放入root内
w = Label(root, text="Hello Tkinter!")

#调用pack进行布局
w.pack()

#启动主窗口
root.mainloop()