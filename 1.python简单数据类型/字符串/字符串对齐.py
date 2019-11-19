#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 15:58
# filename: 字符串对齐.py

text = "hello world"
print(text.ljust(20))

print(text.rjust(20))

print(text.center(20))
print()
print("增加填充字段")
print()
print(text.rjust(20, "-"))
print(text.ljust(20, "-"))
print(text.center(20, "-"))
print()
print("format的使用")
print()
print(format(text, ">20"))
print(format(text, "<20"))
print(format(text, "^20"))

print(format(text, "*>20"))
print(format(text, "*<20"))
print(format(text, "*^20"))

print()
print("格式化多个值")
print()
print("{:>10s} {:>10s}".format("hello", "world"))

x = 1.2345
print(format(x, ">10"))
print(format(x, "^10.2f"))

# 使用%进行格式化，较老的格式，不常用
print("%-20s" % text)
print("%20s" % text)

template = "编号， %09d \t公司名称：%s \t官网： http://www.%s.com"     # 定义模板

print()
context1 = (7, "百度", "baidu")
context2 = (9, "百度2", "baidu2")
print(template % context1)
print(template % context2)

print()

template2 = "编号：{:0>9s}\t公司名称: {:s}\t 官网: http://www.{:s}.com"  # 定义模板
context01 = template2.format("7", "百度3", "baidu3")
context02 = template2.format("8", "百度4", "baidu4")
print(context01)
print(context02)

