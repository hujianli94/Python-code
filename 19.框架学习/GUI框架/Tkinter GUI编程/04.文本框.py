#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 14:53
# filename: 04.文本框.py
import tkinter
root = tkinter.Tk()

entry1 = tkinter.Entry(root,                    #生成单行文本框组件
                       show="*",)               #输入文本框中的字符被显示为*
entry1.pack()               #将文本框添加到窗口中

entry2 = tkinter.Entry(root,                    #生成单行文本框组件
                       show="#，",              #输入文本框中的字符被显示为*
                        width = 50)             # 将文本框的宽度设置为50
entry2.pack()

entry3 = tkinter.Entry(root,                    #生成单行文本框组件
                      bg = "red",               # 将文本框中的背景色设置为红色
                      fg = "blue")             # 将文本框中的前景色设置为蓝色
entry3.pack()


entry4 = tkinter.Entry(root,                    #生成单行文本框组件
                      selectbackground = "red",               # 将选中文本的背景色设置为红色
                      selectforeground = "gray")             # 将选中文本的前景色设置为蓝色
entry4.pack()

entry5 = tkinter.Entry(root,
                    state = tkinter.DISABLED)                # 将文本设置为禁用
entry5.pack()

edit1 = tkinter.Text(root,                                  #生成多行文本框组件
                     selectbackground = "red",              #将选中文本的背景色设置为红色
                     selectforeground = "gray")             #将选中文本的前景色设置为蓝色
edit1.pack()

root.mainloop()

