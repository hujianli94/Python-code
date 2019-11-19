#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 18:01
# filename: 同时对文件进行读写.py

# 模拟一个复制文件的操作
with open("foo_bak.txt", "r", encoding="utf-8") as file_read:
    lines = file_read.readlines()
    print(lines)
    copy_file = "foo_bak_01.txt"
    with open(copy_file, "w", encoding="utf-8") as file_write:
        file_write.writelines(lines)
        print("文件复制成功")
