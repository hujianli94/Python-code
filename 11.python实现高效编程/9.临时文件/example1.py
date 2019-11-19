#!/usr/bin/env python
#-*- coding:utf8 -*-
from tempfile import TemporaryFile,NamedTemporaryFile
f = TemporaryFile()
f.write(b"abcdef" *  100000)
f.seek(0)
print(f.read(100))


# ntf = NamedTemporaryFile(delete=False)   #创建一个临时文件，不会被回收删除
ntf = NamedTemporaryFile()
print(ntf.name)             #创建一个临时文件