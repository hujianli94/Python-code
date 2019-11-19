#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 23:26
# filename: 05.标签.py
"""
演示在主窗口中显示创建的各种不同类型的标签组件
"""
import tkinter  # 导入tkinter模块

root = tkinter.Tk()
labell = tkinter.Label(root,
                       anchor=tkinter.E,
                       bg="blue",  # 设置文本的位置
                       fg="red",  # 设置标签背景色
                       text="Python",  # 设置标签中的文本
                       width=30,  # 设置标签的宽度为30
                       height=5)  # 设置标签的高度为5
labell.pack()
label2 = tkinter.Label(root,
                       text="Python GUI\n tkinter",  # 设置标签中的文本,在字符串中使用换行符
                       justify=tkinter.LEFT,  # 设置多行文本为左对齐
                       width=30,
                       height=5)
label2.pack()

label3 = tkinter.Label(root,
                       text="Python GUI\n tkinter",  # 设置标签中的文本,在字符串中使用换行符
                       justify=tkinter.RIGHT,  # 设置多行文本为左对齐
                       width=30,
                       height=5)
label3.pack()

label4 = tkinter.Label(root,
                       text="Python GUI\n tkinter",  # 设置标签中的文本,在字符串中使用换行符
                       justify=tkinter.CENTER,  # 设置多行文本为左对齐
                       width=30,
                       height=5)
label4.pack()

root.mainloop()

