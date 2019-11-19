#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 14:46
# filename: Pack布局管理器.py
from tkinter import *

root = Tk()
root.title("Pack布局")
for i in range(3):
    lab = Label(root, text="第{}个label".format(i + 1, bg='#eeeeee'))
    #调用pack进行布局
    lab.pack()

root.mainloop()