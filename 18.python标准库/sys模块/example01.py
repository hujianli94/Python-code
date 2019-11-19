#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/15 17:52
# filename: example01.py
import sys

# 显示本地字节序的指示符
print(sys.byteorder)

# 显示与Python解释器有关的版权信息
print(sys.copyright)

# 显示Python解释器在磁盘上的存储路径
print(sys.executable)  # C:\Users\18793\Anaconda3\python.exe

# 显示在当前系统中保存文件所用的字符集
print(sys.getfilesystemencoding())  # mbcs
# 显示python整数支持的最大值
print(sys.maxsize)  # 9223372036854775807

# 显示python解释器所在的平台
print(sys.platform)  # win32

# 显示当前python解释器的版本信息
print(sys.version)  # 3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  5 2016, 11:41:13) [MSC v.1900 64 bit (AMD64)]

# 返回当前python解释器的主版本号
print(sys.winver)  # 3.5

args = sys.argv
if len(args) < 2:
    print(args[0])  # D:/21-DAY-Python/18.python标准库/sys模块/example01.py
    print("请传入参数！")
else:
    print(args[0])
    print(args[1])


# 动态修改模块加载路径
sys.path.append("D:/21-DAY-Python/18.python标准库/sys模块/")
import test
print(test.hello)