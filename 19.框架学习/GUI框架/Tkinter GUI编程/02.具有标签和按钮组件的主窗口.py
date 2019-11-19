#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 13:35
# filename: 02.具有标签和按钮组件的主窗口.py
import tkinter
root = tkinter.Tk()                                    # 生成root主窗口
label = tkinter.Label(root, text="Hello tkinter")       #生成标签
label.pack()        #将标签添加到root主窗口
button1 = tkinter.Button(root, text="Button1")  #生成button1
button1.pack(side=tkinter.LEFT)     #将button1添加到root主窗口
button1 = tkinter.Button(root, text="Button2")  #生成button2
button1.pack(side=tkinter.RIGHT)     #将button2添加到root主窗口
root.mainloop()             #进入消息循环