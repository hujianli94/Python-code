#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/5 13:26
# filename: thinkergame01.py
import tkinter as tk
import random

number = random.randint(0, 1024)  # 玩家要猜的数字
running = True
num = 0  # 猜的次数
nmaxnn = 1024  # 提示范围的最大数
nminn = 0  # 提示范围的最小数


def eBtnClose(event):
    """
    “关闭”按钮事件函数
    :param event:
    :return:
    """
    root.destroy()


def eBtnGuess(event):
    """
    “猜”按钮事件函数
    :param event:
    :return:
    """
    global num
    global nmaxnn
    global nminn
    global running

    if running:
        val_a = int(entry_a.get())  # 获取猜的数字并转换成数字
        if val_a == number:
            labelqval("恭喜答对了！")
            num += 1
            running = False
            numGuess()  # 显示猜的次数

        elif val_a < number:            #猜小了
            if val_a > nminn:
                nminn = val_a  # 修改提示猜测范围的最小数
                num += 1
                labelqval("小了哦。请输入" + str(nminn) + "到" + str(nmaxnn) + "之间任意整数：")
        else:
            if val_a < nmaxnn:
                nmaxnn = val_a  # 修改提示猜测范围的最大数
                num += 1
                labelqval("大了哦，请输入" + str(nminn) + "到" + str(nmaxnn) + "之间任意整数：")
    else:
        labelqval("你已经答对啦.....")


def numGuess():
    """
    显示猜的次数
    :return:
    """
    if num == 1:
        labelqval("一次答对！")
    elif num < 10:
        labelqval("==十次机会以内答对了牛。。。。尝试次数:{}".format(num))
    else:
        labelqval("尝试超过10次机会.....尝试次数：{}".format(num))


def labelqval(vText):
    """
    修改提示标签文字
    :return:
    """
    label_val_q.config(label_val_q, text=vText)  # 修改提示标签文字


root = tk.Tk(className="猜数字游戏")
root.geometry("400x90+200+200")
label_val_q = tk.Label(root, width="80")  # 提示标签
label_val_q.pack(side='top')

entry_a = tk.Entry(root, width="40")  # 单行输入文本框
btnGuess = tk.Button(root, text="猜")  # "猜"按钮
entry_a.pack(side="left")
entry_a.bind('<Return>', eBtnGuess)  # 绑定事件
btnGuess.bind('<Button-1>', eBtnGuess)  # "猜"按钮
btnGuess.pack(side='left')

btnClose = tk.Button(root, text="关闭")  # "关闭"按钮
btnClose.bind('<Button-1>', eBtnClose)
btnClose.pack(side="left")
labelqval("请输入0-1024之间任意整数：")
entry_a.focus_set()
print(number)
root.mainloop()
