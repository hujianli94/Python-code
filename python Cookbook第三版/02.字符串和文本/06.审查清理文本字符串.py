#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/30 9:54
# filename: 06.审查清理文本字符串.py

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # delete
}
a = s.translate(remap)

print(a)


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


print(clean_spaces(s))

