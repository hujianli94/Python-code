#!/usr/bin/env python
#-*- coding:utf8 -*-
wd = "胡建力学python"
wd_encode = wd.encode()
print(wd_encode)
wd_decode = wd_encode.decode()
print(wd_decode)

wd_encode_gb2312 = wd.encode("gb2312")
print(wd_encode_gb2312)
wd_decode_gb2312 = wd_encode_gb2312.decode("gb2312")
print(wd_decode_gb2312)

wd_encode_utf8 = wd.encode("utf-8")
print(wd_encode_utf8)
wd_decode_utf8 = wd_encode_utf8.decode("utf-8")
print(wd_decode_utf8)
