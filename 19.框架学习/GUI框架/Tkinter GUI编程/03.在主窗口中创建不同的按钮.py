#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 14:43
# filename: 03.在主窗口中创建不同的按钮.py
import tkinter          #导入tkinter模块
root = tkinter.Tk()
button1 = tkinter.Button(root,
                         anchor=tkinter.E,      #指定文本对齐方式
                         text='Button1',            #指定按钮的文本
                         width=40,              #指定按钮的宽度，相当于40个字符
                         height=5)              # 指定按钮的高度，相当于5行字符
button1.pack()          #将按钮添加到窗口

button2 = tkinter.Button(root,
                         text='Button2',
                         bg="blue")         #指定按钮的背景色
button2.pack()


button3 = tkinter.Button(root,
                         text='Button3',            #指定按钮的文本
                         width=14,              #指定按钮的宽度，相当于14个字符
                         height=1)              # 指定按钮的高度，相当于1行字符
button3.pack()          #将按钮添加到窗口


button4 = tkinter.Button(root,
                         text='Button4',            #指定按钮的文本
                         width=60,              #指定按钮的宽度，相当于40个字符
                         height=5,              # 指定按钮的高度，相当于5行字符
                         state=tkinter.DISABLED)            #指定按钮为禁用状态
button4.pack()          #将按钮添加到窗口

root.mainloop()

