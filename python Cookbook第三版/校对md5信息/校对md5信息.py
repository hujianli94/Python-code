#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/25 10:49
# filename: 校对md5信息.py
import hashlib
import os


def md5sum(old_file, new_filename):
    """
    用于获取文件的md5值
    """
    if not os.path.isfile(old_file) or not os.path.isfile(new_filename):  # 如果被校验old_file或者new_file的md5的文件不是文件，返回空
        return
    myhash = hashlib.md5()
    with open(old_file, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)

    old_md5 = myhash.hexdigest()

    with open(new_filename, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)

    new_md5 = myhash.hexdigest()

    return old_md5, new_md5


print(md5sum('test.txt', 'test1.txt'))


def md5_update(file):
    """
    :param file:文件名称
    :return:更新返回True，没更新返回False
    """
    if not os.path.isfile(file):  # 如果不是文件就返回空
        return
        # 创建MD5对象
    md5obj = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            md5obj.update(b)
    md5code = md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print("数据没有更新.....")
        return False
    else:
        # 把新的md5写入文件中
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print("数据更新")
        return True


md5_update('test.txt')
