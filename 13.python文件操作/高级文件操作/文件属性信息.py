#!/usr/bin/env python
#-*- coding:utf8 -*-
import os

def fomatTime(logtime):
    '''
    格式化时间函数
    :param logtime:
    :return:
    '''
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(logtime))


def formatByte(number):
    '''
    格式化文件大小的函数
    :param number:
    :return:
    '''
    for (scale,label) in [(1024*1024*1024,'GB'),(1024*1024,'MB'),(1024,'KB')]:
        if number >= scale:     #大于等于1KB
            return "%.2f &s" %(number*1.0/scale,label)
        elif number == 1:
            return "1 字节"
        else:       #处理文件大小小于1KB
            byte = '%.2f' % (number or 0)
    return (byte[:-3] if byte.endswith(".00") else byte) + "字节"




fileinfo = os.stat('重命名文件.py')      #获取文件的基本信息
print("文件完整路径: ", os.path.abspath('重命名文件.py')) #获取文件完整路径
#输出文件的基本信息
print("索引号: ",fileinfo.st_ino)
print("设备名：",fileinfo.st_dev)
print("文件大小: ",formatByte(fileinfo.st_size))
print("最后一次访问时间: ",fomatTime(fileinfo.st_atime))
print("最后一次修改时间: ",fomatTime(fileinfo.st_mtime))
print("最后一次状态变化时间: ",fomatTime(fileinfo.st_ctime))
