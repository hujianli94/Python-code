#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 22:45
# filename: findfat1.py
import tkinter
import tkinter.messagebox, tkinter.simpledialog
import os, os.path
import threading

rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.chk', '.@@@', '.$$$$']


class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        # 创建菜单
        menu = tkinter.Menu(self.root)

        # 创建"系统"子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='关于...', command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label='退出', command=self.MenuExit)
        menu.add_cascade(label='系统', menu=submenu)

        # 创建"清理"子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='扫描垃圾文件', command=self.MenuScanRubbish)
        submenu.add_command(label='删除垃圾文件', command=self.MenuDelRubbish)
        menu.add_cascade(label='清理', menu=submenu)

        # 创建"查找"子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='搜索大文件', command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label='按名称搜索文件', command=self.MenuSearchFile)
        menu.add_cascade(label='搜索', menu=submenu)

        self.root.config(menu=menu)

        # 创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root, anchor=tkinter.W, text='状态', bitmap='hourglass', compound='left')
        self.progress.place(x=10, y=370, width=480, height=15)

        # 创建文本框,显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10, y=10, width=480, height=350)

        # 为文本框添加垂直滚动条
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right', fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title('Windows 【减肥】 工具')
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    def MenuAbout(self):
        """
        关于按钮的触发器
        :return:
        """
        tkinter.messagebox.showinfo("Windows 【减肥工具】",
                                    "这是使用Python编写的Windows优化程序。\n 欢迎使用并提出宝贵的意见！")

    def MenuExit(self):
        """
        退出按钮的触发器
        :return:
        """
        self.root.quit()

    def MenuScanRubbish(self):
        """
        ‘扫描垃圾文件’菜单
        :return:
        """
        result = tkinter.messagebox.askquestion("Windows【减肥工具】",
                                                "扫描垃圾文件将需要较长时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Findfat", "马上开始扫描垃圾文件！")
        # self.ScanRubbish()
        self.drives = GetDirves()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))  # 创建线程
        t.start()  # 开始线程

    def MenuDelRubbish(self):
        """
        ‘删除垃圾文件’菜单
        :return:
        """
        result = tkinter.messagebox.askquestion("Windows【减肥工具】",
                                                "删除垃圾文件将需要较长时间，是否继续？")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Findfat", "马上开始删除垃圾文件！")
        # self.DeleteRubbish()
        self.drives = GetDirves()
        t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))  # 创建线程
        t.start()  # 开始线程

    def MenuScanBigFile(self):
        """
        ‘搜索大文件’菜单
        :return:
        """
        s = tkinter.simpledialog.askinteger('Findfat', '请设置大文件的大小(M)')
        t = threading.Thread(target=self.ScanBigFile, args=(s,))
        t.start()

        # result = tkinter.messagebox.askquestion("Windows【减肥工具】",
        #                                         "扫描大文件将需要较长时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("Findfat", "马上开始扫描大文件！")

    def MenuSearchFile(self):
        """
        ‘按名称搜索文件’菜单
        :return:
        """
        s = tkinter.simpledialog.askstring('Findfat', '请输入文件名的部分字符')
        t = threading.Thread(target=self.SearchFile, args=(s,))
        t.start()

        # result = tkinter.messagebox.askquestion("Windows【减肥工具】",
        #                                         "按名称搜索文件将需要较长时间，是否继续？")
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo("Findfat", "马上开始按名称搜索文件！")

    def ScanRubbish(self, scanpath):
        """
        Scanning 垃圾文件
        :return:
        """
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dir, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':  # 若文件无扩展名
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:  # 扩展名在垃圾文件扩展名中
                                fname = os.path.join(os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                if total % 15 == 0:
                                    self.flist.delete(0.0, tkinter.END)

                                l = len(fname)
                                if l > 50:
                                    self.progress['text'] = fname[:25] + '....' + fname[l - 25:l]

                                self.flist.insert(tkinter.END, fname + "\n")
                                self.progress['text'] = fname
                                total += 1  # 计数

                        except ValueError:
                            pass

                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "找到【%s】个垃圾文件,共占用【%.2fM】磁盘空间" % (total, filesize / 1024 / 1024)

    def DeleteRubbish(self, scanpath):
        """
        Delete垃圾文件
        :return:
        """
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dir, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':  # 若文件无扩展名
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:  # 扩展名在垃圾文件扩展名中
                                fname = os.path.join(os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)

                                try:
                                    os.remove(fname)  # 删除文件

                                    l = len(fname)
                                    if l > 50:
                                        self.progress['text'] = fname[:25] + '....' + fname[l - 25:l]
                                    if total % 15 == 0:
                                        self.flist.delete(0.0, tkinter.END)

                                    self.flist.insert(tkinter.END, fname + "\n")
                                    self.progress['text'] = fname
                                    total += 1  # 计数
                                except:
                                    pass

                        except ValueError:
                            pass

                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "删除 【%s】个垃圾文件,回收 【%.2fM】磁盘空间" % (total, filesize / 1024 / 1024)

    def ScanBigFile(self, filesize):
        """
        寻找大文件
        :param filesize:
        :return:
        """
        total = 0
        filesize = filesize * 1024 * 1024
        for drive in GetDirves():
            for root, dirs, files in os.walk(drive):
                for fil in files:
                    try:
                        fname = os.path.abspath(os.path.join(root, fil))
                        fsize = os.path.getsize(fname)

                        self.progress['text'] = fname  # 在状态标签中显示每一个遍历的文件
                        if fsize >= filesize:
                            total += 1
                            self.flist.insert(tkinter.END, '%s, [%.2f M]\n' % (fname, fsize / 1024 / 1024))
                    except:
                        pass
        self.progress['text'] = "找到 【%s】个超过【%s】M的大文件" % (total, filesize / 1024 / 1024)

    def SearchFile(self, fname):
        """
        寻找大文件
        :param filesize:
        :return:
        """
        total = 0
        fname = str(fname).upper()
        for drive in GetDirves():
            for root, dirs, files in os.walk(drive):
                for fil in files:
                    try:
                        fn = os.path.abspath(os.path.join(root, fil))
                        l = len(fn)
                        if l > 50:
                            self.progress['text'] = fn[:25] + '...' + fn[l - 25:l]
                        else:
                            self.progress['text'] = fn

                        if fil.upper().find(fname) >= 0:
                            total += 1
                            self.flist.insert(tkinter.END, fn + '\n')
                    except:
                        pass

        self.progress['text'] = "找到%s个文件" % (total)


def GetDirves():
    """
    扫描本地所有磁盘，将C盘排除
    :return:
    """
    dirves = []
    for i in range(65, 91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            dirves.append(vol)
    index = dirves.index("C:/")
    # list1.pop(index)
    del dirves[index]
    return tuple(dirves)


if __name__ == '__main__':
    window = Window()
    window.MainLoop()
    # GetDirves()
