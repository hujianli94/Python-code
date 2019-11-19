#!/usr/bin/env python
# -*- coding:utf8 -*-
# 上下文管理器是指实现上下文管理协议方法的对象，主要用于安全地释放资源（如打开的文件、数据库连接或网络连接、
# 对对象的锁定等 ）；对于上下文管理器对象可以使用with语句来使用它，在with语句中可以使用上下文管理器或提供资源
# 当退出with语句时，由上下文管理器来负责安全地释放资源
'''
__enter__(self)
__exit__(self,type,value,tb)
__enter__(self)方法时进入上下文时调用的，它创建并返回一个可以引用的资源对象。供with语句块中的程序使用
__exit__(self,type,value,tb)方法是退出上下文时调用的，它主要用来安全地释放源对象
方法中参数type、value、tb用于跟踪退出错误时发生的错误类型、值和跟踪信息
'''


class FileMgr:

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        self.f = open(self.filename, encoding="utf-8")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()


if __name__ == '__main__':
    with FileMgr("a10_4.py") as f:
        for line in f.readlines():
            print(line, end='')


# 代码中先定义一个管理文件资源对象的上下文管理器FileMgr.它实现了上西屋管理器的协议方法
# 退出时关闭文件，然后使用一个with语句来使用这个上下文管理器，打开指定的文件，并输出其中的内容


# 模拟open函数
class Open:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.f = open(self.path, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()


with Open("hujianli.txt", "w") as f:
    f.write("hello world\n")
    f.write("hello Python\n")

