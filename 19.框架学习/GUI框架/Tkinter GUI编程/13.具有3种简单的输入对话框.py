#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/5 21:40
# filename: 13.具有3种简单的输入对话框.py
import tkinter
import tkinter.simpledialog  # 导入tkSimpleDialog模块


def InStr():
    r = tkinter.simpledialog.askstring('Python tkinter',  # 创建字符串输入对话框
                                       'Input String',  # 指定提示字符
                                       initialvalue='tkinter')  # 指定初始化文本

    print(r)


def InInt():  # 按键事件处理函数
    r = tkinter.simpledialog.askinteger('Python tkinter', 'Input Integer')
    print(r)  # 创建整数输入对话框


def InFlo():  # 按键事件处理函数
    r = tkinter.simpledialog.askfloat('Python tkinter', 'Input Float')
    print(r)  # 创建浮点数输入对话框


root = tkinter.Tk()
buttonl = tkinter.Button(root, text='Input String',    # 创建按钮
                         command=InStr())  # 指定按钮事件处理函数

buttonl.pack(side='left')

button2 = tkinter.Button(root, text='Input Integer',    # 创建按钮
                         command=InInt())  # 指定按钮事件处理函数
button2.pack(side='left')


button3 = tkinter.Button(root, text='Input Float',    # 创建按钮
                         command=InFlo())  # 指定按钮事件处理函数
button3.pack(side='left')

root.mainloop()