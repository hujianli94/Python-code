#!/usr/bin/env python
#-*- coding:utf8 -*-
import zipfile, os
#以w的方式的时候是打开文件并清空，如果是a方式那么就是追加文件了
File_path = os.path.abspath(os.path.basename(__file__))
Dir_path = os.path.dirname(os.path.dirname(__file__))

z = zipfile.ZipFile("zip_file.zip","w")
#把文件放入压缩包
z.write(File_path)
#也可以是一个目录
z.write(Dir_path)
#关闭文件
z.close()

#查看包里面的内容列表
print(z.namelist())

#在包里面追加内容
z = zipfile.ZipFile('zip_file.zip','a')
z.write("D:/GitHub/21天python/10.python进阶/上下文管理器模块contextlib")
z.close()

#查看包内的内容
print(z.namelist())

#解压
z = zipfile.ZipFile('zip_file.zip', 'r')
# extractall把所有的文件解压到当前目录
z.extractall()

#解压一个单独的文件
z = zipfile.ZipFile('zip_file.zip', 'r')
# 返回文件所在路径
z.extract("tmp/folder/sc.pyc")
'/home/ansheng/tmp/folder/sc.pyc'