#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 16:00
# filename: 事件绑定.py

"""

python提供了更灵活的事件绑定方式，所有Widget组件都提供了一个bind()方法，该方法可以为“任意”事件绑定事件处理方法
"""

# 单击、双击绑定实际处理方法的示例
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.show = Label(self.master, width=30, bg="white", font=('times', 20))
        self.show.pack()
        bn = Button(self.master, text="单击我或双击我")
        bn.pack(fill=BOTH, expand=YES)

        # 为左键单击事件绑定处理方法
        bn.bind("<Button-1>", self.one)

        # 为左键双击事件绑定处理方法
        bn.bind("<Double-1>", self.double)

    def one(self, event):
        self.show['text'] = "左键单击:{}".format(event.widget['text'])

    def double(self, event):
        print("左键双击，退出程序：", event.widget['text'])
        import sys;sys.exit()

root = Tk()
root.title("简单绑定")
App(root)
root.mainloop()