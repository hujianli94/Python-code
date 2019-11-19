#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 15:06
# filename: GUI界面.py
import tkinter
from tkinter import *
from tkinter.messagebox import *
from DB_info import Question_bank


class Game_UI:
    def __init__(self):
        pass

    def callNext(self):
        global k
        global score
        useranswer = r.get()
        print(r.get())
        if useranswer == values[k][5]:
            showinfo("恭喜", "恭喜你答对了！")
            score += 10
        else:
            showinfo("遗憾", "遗憾您答错了！")
        k = k + 1
        if k >= len(values):  # 判断用户是否做完
            showinfo("提示", "题目做完了")
            return
            # 显示下一题
        timu['text'] = values[k][0]  # 题目信息
        radio1['text'] = values[k][1]  # A选项
        radio2['text'] = values[k][2]  # B选项
        radio3['text'] = values[k][3]  # C选项
        radio4['text'] = values[k][4]  # D选项
        r.set('E')

    def callResult(self):
        showinfo("成绩", "你的成绩是：{}分".format(str(score)))


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Python智力问答游戏')
    root.geometry('500x200')
    r = tkinter.StringVar()
    r.set('E')
    k = 0
    score = 0
    v = Question_bank()  # 获取sqllite数据库读取到的内容
    values = v.read_info()
    if not values:
        v.create_db()  # 创建数据库
    values = v.read_info()
    timu = tkinter.Label(root, text=values[k][0])  # 题目
    timu.pack()
    f1 = Frame(root)  # 创建第一个Frame组件
    f1.pack()

    radio1 = tkinter.Radiobutton(f1, variable=r, value='A', text=values[k][1])
    radio1.pack()

    radio2 = tkinter.Radiobutton(f1, variable=r, value='B', text=values[k][2])
    radio2.pack()

    radio3 = tkinter.Radiobutton(f1, variable=r, value='C', text=values[k][3])
    radio3.pack()

    radio4 = tkinter.Radiobutton(f1, variable=r, value='D', text=values[k][4])
    radio4.pack()

    f2 = Frame(root)  # 创建第二个Frame组件
    f2.pack()

    hujianli = Game_UI()
    Button(f2, text='下一题', command=hujianli.callNext).pack(side=LEFT)
    Button(f2, text='结  果', command=hujianli.callResult).pack(side=LEFT)
    root.mainloop()
