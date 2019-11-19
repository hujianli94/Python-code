#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 8:56
# filename: 16.自定义对话框.py
import tkinter
import tkinter.messagebox as tkMessageBox  # 导入tkMesageBox类


class MyDialog:  # 定义对话框类
    def __init__(self, root):  # 对话框初始化
        self.top = tkinter.Toplevel(root)  # 生成Toplevel组件
        label = tkinter.Label(self.top, text='Please Input')  # 生成标签组件
        label.pack()
        self.entry = tkinter.Entry(self.top)  # 生成文本框组件
        self.entry.pack()
        self.entry.focus()  # 让文本框获得焦点
        button = tkinter.Button(self.top, text='Ok',  # 生成按钮
                                command=self.Ok)  # 设置按钮事件处理函数
        button.pack()

    def Ok(self):  # 定义按钮事件处理函数
        self.input = self.entry.get()  # 获取文本框中的内容，保存为input
        self.top.destroy()  # 销毁对话框

    def get(self):  # 返回在文本框输入的内容
        return self.input


class MyButton():
    def __init__(self, root, type):
        self.root = root
        if type == 0:
            self.button = tkinter.Button(root, text='Create', command=self.Create)  # 设置Create按钮处理函数
        else:
            self.button = tkinter.Button(root, text='Quit', command=self.Quit)  # 设置Quit按钮的事件处理函数
        self.button.pack()

    def Create(self):
        d = MyDialog(self.root)  # 生成对话框
        self.button.wait_window(d.top)  # 等待对话框结束
        tkMessageBox.showinfo('Python', 'You input:\n' + d.get())  # 获取对话框中输入值，并输出

    def Quit(self):  # Quit按钮的事件处理函数
        self.root.quit()  # 退出主窗口


root = tkinter.Tk()
MyButton(root, 0)
MyButton(root, 1)
root.mainloop()
