#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 15:11
# filename: GUI001.py
from tkinter import *
from translate import translate_Word


def leftClick(event):
    en_str = Entry1.get()
    print(en_str)
    vText = translate_Word(en_str)
    Entry1.config(Entry2, text=vText)  # 修改翻译结果框文字
    s.set("")
    Entry2.insert(0, vText)


def leftClick2(event):
    s.set("")
    # Entry1.insert(0, "")
    Entry2.insert(0, "")


root = Tk()
root.title("单词翻译器")
root["width"] = 250
root["height"] = 130
Label(root, text="输入要翻译的内容： ", width=15).place(x=1, y=1)  # 绝对坐标(1,1)

Entry1 = Entry(root, width=20)
Entry1.place(x=110, y=1)  # 绝对坐标(110,1)
Label(root, text="翻译的结果： ", width=15).place(x=1, y=20)  # 绝对坐标(1,20)

s = StringVar()
s.set("大家好，这是测试")

Entry2 = Entry(root, width=20, textvariable=s)
Entry2.place(x=110, y=20)  # 绝对坐标(110,1)
Button1 = Button(root, text="翻译", width=8)
Button1.place(x=40, y=80)  # 绝对坐标(40,80)

Button2 = Button(root, text="清空", width=8)
Button2.place(x=110, y=80)  # 绝对坐标(110,80)

# 给Button绑定鼠标监听事件
Button1.bind("<Button-1>", leftClick)
Button2.bind("<Button-1>", leftClick2)
root.mainloop()
