#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 18:14
# filename: 08.单选框和复选框.py
import tkinter

root = tkinter.Tk()

r = tkinter.StringVar()  # 使用StringVar生成字符串变量用于单选框组件
r.set('1')  # 初始化变量的值
radio = tkinter.Radiobutton(root,  # 生成单选框组件
                            variable=r,  # 设置单选框关联的变量
                            value="1",  # 设置单选框中关联变量的值，即r的值
                            text="Radio1")  # 设置单选框显示的文本
radio.pack()

radio = tkinter.Radiobutton(root,  # 生成单选框组件
                            variable=r,  # 设置单选框关联的变量
                            value="2",  # 当选中该单选框时，r的值为2
                            text="Radio2")  # 设置单选框显示的文本
radio.pack()

radio = tkinter.Radiobutton(root,  # 生成单选框组件
                            variable=r,  # 设置单选框关联的变量
                            value="3",  # 当选中该单选框时，r的值为3
                            text="Radio3")  # 设置单选框显示的文本
radio.pack()

radio = tkinter.Radiobutton(root,  # 生成单选框组件
                            variable=r,  # 设置单选框关联的变量
                            value="4",  # 当选中该单选框时，r的值为3
                            text="Radio4")  # 设置单选框显示的文本
radio.pack()
c = tkinter.IntVar()  # IntVar生成整型变量用于复选框
c.set(1)
check = tkinter.Checkbutton(root,
                            text="Checkbutton", #设置复选框文本
                            variable=c,         #设置复选框关联变量
                            onvalue=1,          #当选中复选框时，c的值为1
                            offvalue=2)         #当末选中复选框时，c的值为2

check.pack()
root.mainloop()
print(r.get())
print(c.get())
