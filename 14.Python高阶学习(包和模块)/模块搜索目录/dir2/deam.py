#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
#1.添加临时目录
sys.path.append("D:\\GitHub\\21天python\\14.Python高阶学习(包和模块)\\模块搜索目录\\dir1")
import calculate
calculate.test()


#2.添加\Lib\site-packages目录下.pth文件实现，只在当前python版本中可以使用



#3.添加环境PythonPATH变量
''' window 右击属性----环境变量 '''