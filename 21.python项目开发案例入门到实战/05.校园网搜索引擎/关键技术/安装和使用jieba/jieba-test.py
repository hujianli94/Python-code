#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/15 10:54
# filename: jieba-te.py
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)  # 全模式
print("Full Mode:", "/".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学")  # 默认精确模式
print("Default Mode:", "/".join(seg_list))

seg_list = jieba.cut_for_search("我来到北京清华大学")  # 搜索引擎模式
print("搜索引擎模式:", "/".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学")
for word in seg_list:
    print(word, end=' ')
