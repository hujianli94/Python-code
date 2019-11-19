#!/usr/bin/python
#-*- coding:utf-8 -*-
#进行编码，转化为bytes
str = "我爱python"
wd_utf8 = str.encode()#默认编码格式为utf-8
print(wd_utf8)

#进行解码，返回字符串类型的数据
print(wd_utf8.decode())

#进行编码为gb2312格式的bytes
wd_gb_bit = str.encode("gb2312")  # type: bytes
print(wd_gb_bit)

#print(wd_gb_bit.decode()) #会报错！
#编码和解码要遵循类型一致的原则
print(wd_gb_bit.decode("gb2312"))




