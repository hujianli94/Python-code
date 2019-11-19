#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 19:50
# filename: 10.绘制图形.py
import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root,
                        width=600,  # 指定Canvas组件的宽度为600
                        height=480,  # 指定Canvas组件的高度为480
                        bg="white")  # 指定Canvas组件的背景色为白色
im = tkinter.PhotoImage(file="Am.gif")
canvas.create_image(300, 70, image=im)  # 使用create_image将图片添加到Canvas组件中

canvas.create_text(302, 77,  # 使用create_text方法绘制文字
                   text="Use Canvas",  # 所绘制文字的内容
                   fill="gray")  # 所绘制文字的颜色为灰色

canvas.create_text(300, 75,  # 使用create_text方法绘制文字
                   text="Use Canvas",  # 所绘制文字的内容
                   fill="blue")  # 所绘制文字的颜色为蓝色

canvas.create_polygon(290, 114, 316, 114,  # 使用create_polygon绘制六边形
                      330, 130, 310, 146, 284, 146, 270, 130)

canvas.create_oval(280, 120, 320, 140,  # 使用create_oval绘制椭圆
                   fill="white")  # 设置椭圆用白色填充

canvas.create_line(250, 130, 350, 130)  # 使用create_line绘制直线
canvas.create_line(300, 100, 300, 160)

canvas.create_rectangle(90, 190, 510, 410,
                        width=5)  # 使用create_rectangle绘制一个矩形，设置矩形线宽为5像素

canvas.create_arc(100, 200, 500, 400, start=0, extent=240, fill='pink')  # 使用create_arc绘制圆弧，设置圆弧的起止角度
canvas.create_arc(103, 203, 503, 403, start=241, extent=112, fill='red')  # 使用create_arc绘制圆弧，设置圆弧的起止角度
canvas.pack()  # 将Canvas添加到主窗口
root.mainloop()
