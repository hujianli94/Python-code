#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 10:46
# filename: 字符串的反转.py
def reverse(s):
    out = ""
    li = list(s)
    for i in range(len(li), 0, -1):
        out += "".join(li[i - 1])
    return out


print(reverse("胡建力啊啊啊啊哈哈哈哈哈"))


def reverse2(s):
    li = list(s)
    li.reverse()
    s = "".join(li)
    return s


print(reverse2("胡建力啊啊啊啊哈哈哈哈哈"))


def reverse3(s):
    return s[::-1]


# 使用lambda来实现
lambda_str = lambda s: s[::-1]
print(lambda_str("hujianlishuaige"))
