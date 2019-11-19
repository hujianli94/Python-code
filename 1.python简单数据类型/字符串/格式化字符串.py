#!/usr/bin/env python
# -*- coding:utf8 -*-
print("I am %s stduy %s" % ("hujianli", "python"))
print("I am {0} stduy {1}".format("hujianli", "python"))
str = "I am {0} stduy {1}"
name = ("hujianli", "python")
print(str.format(*name))

print("%d + %d = %d" % (2, 3, 2 + 3))
print("%d + %d = %d" % (3, 7, 3 + 7))

print(" 分割线 ".center(100, "*"))

template = '编号:%09d\t 公司名称：%s \t 官网 ：http://www.%s.com'
arg1 = (7, "xxx方", "futong")
print(template % arg1)

template2 = "编号:{:0>9s}\t公司名称：{:s} \t 官网:http://www.{:s}.com "
context1 = template2.format("7", "百度", "baidu")
print(context1)

print("圆周率PI 的值为：%.2f" % 3.14)
print("圆周率PI 的值为：%10f" % 3.141593)  # 字段宽度为10
print("保留2位小数，圆周率PI 的值为：%10.2f" % 3.141593)  # 字段宽度为10，字符串占据4个
print("保留2位小数， 圆周率PI的值为：%.2f" % 3.141593)  # 输出，没有字段宽度参数
print("字符串精度获取：%.5s " % ('hello world'))  # 打印字符串前5个字符

print("".center(100, "*"))
## 打印浮点数
number = 123
print("%f" % number)
print("%.2f" % number)
print("%.4f" % number)
print()

print("{:.2f}".format(number))
print("{:+.2f}".format(number))

# 指定占位符宽度
print("".center(100, "*"))
number = "ABCDE"
print("%6s" % number)
print("%06s" % number)
print("%8s" % number)
