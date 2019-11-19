#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 12:42
# filename: 拆分路径.py
import os

path = "/home/lmx/t/access.log"
# 返回一个元祖，包含路径和文件名
print(os.path.split(path))
# 返回文件的路径
print(os.path.dirname(path))
# 返回文件的名称
print(os.path.basename(path))
# 返回一个除去文件扩展名和扩展名的二元组
print(os.path.splitext(path))

# 获取文件路径
print(os.getcwd())
print(os.path.abspath('.'))
# 返回本路径的上一层路径
print(os.path.abspath('..'))
# 拼接上层路径 + /hu/a.py
print(os.path.abspath('../hu/a.py'))
# 拼接上层路径 + /hu/hu.py
print(os.path.join(os.path.abspath('.'), 'hu', 'hu.py'))
