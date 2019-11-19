#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/16 13:28
# filename: 02.直接使用wx.App的方式.py
import wx
app = wx.App()      #实例化wx类
frame = wx.Frame(None,title="Hello wxPython")       #初始化wx.App类
frame.Show()                #显示窗口
app.MainLoop()              #调用wx.App类的MailLoop()主循环方法