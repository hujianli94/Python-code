#!/usr/bin/env python
#-*- coding:utf8 -*-

#包名 + 模块名导入
import home.size
print('width:',home.size.width)
print('height:',home.size.height)


print()
#from 包名 + import 模块名
from home import size
print('width:',size.width)
print('height:',size.height)


print()
#from 包名.模块名 import 定义函数或变量
from home.size import height,width
print('width:',width)
print('height:',height)