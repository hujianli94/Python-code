#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 8:26
# filename: 15.颜色选择对话框实例.py
import tkinter
import tkinter.colorchooser


def ChooseColor():
    r = tkinter.colorchooser.askcolor(title='Python tkinter')  # 创建颜色选择对话框
    print(r)  # 输出返回值


root = tkinter.Tk()
button = tkinter.Button(root, text='Choose Color',  # 创建按钮
                        command=ChooseColor)  # 指定按钮事件处理函数
button.pack()
root.mainloop()                                 # 进入消息循环
