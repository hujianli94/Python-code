#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/17 16:34
# filename: tempfile_file.py

import tempfile

#创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)

fp.write("两情若是久长时,".encode('utf-8'))
fp.write("又岂在朝朝暮暮。".encode('utf-8'))

#將文件指针移到开始处，准备读取文件
fp.seek(0)

print(fp.read().decode("utf-8"))
fp.close()



#通过with语句创建临时文件，with会自动关闭临时文件
with tempfile.TemporaryFile() as fp:
    # 写入内容
    fp.write(b"I Love Python!")
    # 将文件指针移到开始处，准备读取文件
    fp.seek(0)

    #读取文件内容
    print(fp.read())


# 通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print("创建临时目录", tmpdirname)


''' 
第一种方式是手动创建临时文件，读写临时文件后主动关闭它。当程序关闭临时文件时，该文件会被自动删除
第二中方式是使用with语句来创建临时文件，with语句会自动关闭临时文件。
'''