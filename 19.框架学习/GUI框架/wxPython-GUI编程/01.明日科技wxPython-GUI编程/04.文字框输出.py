#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/16 13:56
# filename: 04.文字框输出.py

import wx  # 导入wxPython


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建StaticText 文本", pos=(100, 100), size=(600, 400))
        #创建画板
        panel = wx.Panel(self)
        # 创建标题，并设置字体
        title = wx.StaticText(panel, label="Python之阐---by Tim Peters", pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title.SetFont(font)
        #创建文本
        wx.StaticText(panel, label="Beautiful is better than ugly.", pos=(50, 50))
        wx.StaticText(panel, label="Explicit is better than implicit.", pos=(50, 70))
        wx.StaticText(panel, label="Simple is better than complex.", pos=(50, 90))


if __name__ == '__main__':
    app = wx.App()  # 初始化应用
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用MainLoop()主循环方法
