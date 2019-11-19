#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/16 13:22
# filename: 01.创建一个wx.app子类.py
import wx

class App(wx.App):
    ''' 创建wx.App的子类App'''

    def OnInit(self):
        '''初始化方法'''
        frame = wx.Frame(parent=None,title="Hello wypython")    #创建窗口
        frame.Show()    #显示窗口
        return True

if __name__ == '__main__':
    app = App()         #实例化App类
    app.MainLoop()      #调用App类中的MainLoop()主循环方法