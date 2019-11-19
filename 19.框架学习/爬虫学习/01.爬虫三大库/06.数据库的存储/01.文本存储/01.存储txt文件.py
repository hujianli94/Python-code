#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 14:49
# filename: 01.存储txt文件.py

# 追加内容
with open('explore.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join(['question', 'author', 'answer']))
    f.write('\n' + '=' * 50 + '\n')


# 保存时，清空原文内容
with open('explore.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(['question', 'author', 'answer']))
    f.write('\n' + '=' * 50 + '\n')