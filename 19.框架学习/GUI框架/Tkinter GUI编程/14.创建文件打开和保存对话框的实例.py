#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/5 21:53
# filename: 14.创建文件打开和保存对话框的实例.py
import tkinter
import tkinter.filedialog  # 导入tkFileDialog模块


def FileOpen():
    r = tkinter.filedialog.askopenfile(title='Python tkinter',
                                       filetypes=[('Python', '*.py *.pyw'), ('All files', '*')])
    # 指定文件类型为python程序
    # 输出返回值
    print(r)


def FileSave():
    r = tkinter.filedialog.asksaveasfilename(title='Python tkinter',  # 创建保存文件对话框
                                             initialdir=r'D:\GitHub',  # 指定初始化目录
                                             initialfile='test2.py',
                                             )   # 指定初始化文件

    print(r)


root = tkinter.Tk()
button1 = tkinter.Button(root, text="File Open",  # 创建按钮
                         command=FileOpen())  # 指定按钮事件处理函数
button1.pack(side='left')

button2 = tkinter.Button(root, text="File Save",  # 创建按钮
                         command=FileSave())  # 指定按钮事件处理函数
button2.pack(side='left')

root.mainloop()
