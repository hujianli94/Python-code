#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/5 18:42
# filename: 12.对话框001.py
import tkinter
import tkinter.messagebox


def cmd():
    global n
    global buttontext
    n = n + 1
    if n == 1:
        tkinter.messagebox.askokcancel('Python tkiner', 'askokcancel')  # 使用askokcancel函数
        buttontext.set('skquestion')  # 更改按钮上的文字
    elif n == 2:
        tkinter.messagebox.askokcancel('Python tkiner', 'skquestion')  # 使用skquestion函数
        buttontext.set('askyeson')
    elif n == 3:
        tkinter.messagebox.askokcancel('Python tkiner', 'askyeson')  # 使用askyeson函数
        buttontext.set('showerror')
    elif n == 4:
        tkinter.messagebox.askokcancel('Python tkiner', 'showerror')  # 使用showerror函数
        buttontext.set('showinfo')
    elif n == 5:
        tkinter.messagebox.askokcancel('Python tkiner', 'showinfo')  # 使用showinfo函数
        buttontext.set('showwarning')
    else:
        n = 0
        tkinter.messagebox.showwarning('Python tkinter', 'showwarning')  # 使用showwarning函数
        buttontext.set('askokcancel')


n = 0
root = tkinter.Tk()
buttontext = tkinter.StringVar()  # 生成关联按钮文字的变量
buttontext.set('askokcancel')  # 设置buttontext值
button = tkinter.Button(root, textvariable=buttontext, command=cmd)  # 设置事件处理函数
button.pack()
button.mainloop()
