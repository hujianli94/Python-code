#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/10 17:07
# filename: 小试牛刀之-批量文件重命名.py
import os
import time


def batch_rename(path):
    """
    批量文件重命名
    :return:
    """
    global img_num
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False

    if os.path.isfile(path):
        # 分割出目录与文件
        file_path = os.path.split(path)
        # 分割出文件与文件扩展名
        lists = file_path[1].split(".")

        # 取出后缀名
        file_ext = lists[-1]

        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg', 'html']
        if file_ext in img_ext:
            # print(file_ext)
            os.rename(path, file_path[0] + "/" + lists[0] + "_cn." + file_ext)
            img_num += 1
    elif os.path.isdir(path):
        for item in os.listdir(path):
            file = os.path.join(path, item).replace("\\", "/")
            # 递归调用
            batch_rename(os.path.join(file))


if __name__ == '__main__':
    img_dir = 'D:\\21-DAY-Python\\前端知识学习\\CSS'
    img_dir = img_dir.replace("\\", "/")
    start = time.time()
    img_num = 0
    batch_rename(img_dir)
    end = time.time()
    print("总共处理了{0}个文件,耗时：{1}".format(img_num, end - start))
