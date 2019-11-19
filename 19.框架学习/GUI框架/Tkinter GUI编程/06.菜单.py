#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 23:34
# filename: 06.菜单.py
import tkinter

root = tkinter.Tk()

menu = tkinter.Menu(root)  # 生成菜单
submenu = tkinter.Menu(menu, tearoff=0)  # 生成下拉菜单

submenu.add_command(label="Open")  # 向下拉菜单中添加Open命令
submenu.add_command(label="Save")  # 向下拉菜单中添加Save命令
submenu.add_command(label="Close")  # 向下拉菜单中添加Close命令
menu.add_cascade(label="File", menu=submenu)  # 将下拉菜单添加到菜单中
submenu = tkinter.Menu(menu, tearoff=0)  # 生成下拉菜单

submenu.add_command(label="Copy")  # 向下拉菜单中添加Copy命令
submenu.add_command(label="Paste")  # 向下拉菜单中添加Paste命令
submenu.add_separator()  # 向下拉菜单中添加分隔符
submenu.add_command(label="Cut")  # 向下拉菜单中添加Cut命名
menu.add_cascade(label='Edit', menu=submenu)  # 将下拉菜单添加到菜单中
submenu = tkinter.Menu(menu, tearoff=0)  # 生成下拉菜单

submenu.add_command(label="About")  # 向下拉菜单中添加About命令
menu.add_cascade(label="Help", menu=submenu)  # 将下拉菜单添加到菜单中
root.configure(menu=menu)
root.mainloop()

