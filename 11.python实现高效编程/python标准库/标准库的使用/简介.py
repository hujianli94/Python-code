#!/usr/bin/env python
#-*- coding:utf8 -*-
'''内置模块，默认内置模块保存路径在 C:\Python35\lib
通过一些方式获取内置模块的路径:
'''
# import sys
# for i in sys.path:
#     print(i)

'''
模块导入的方式如下：
'''
# import sys
# from sys import path
# for i in path:
#     print(i)

"""
给导入的模块起一个别名
"""
# from sys import path as path_alias
# for i in path_alias:
#     print(i)

'''
添加默认的环境变量，当前生效
'''
# import sys
# import os
# NAME=os.path.dirname(os.path.abspath(os.path.basename(__file__)))
# sys.path.append(NAME)
# print(sys.path[-1])

'''
模块导入顺序
先在当前脚本目录寻找有没有与导入模块名称相同的文件，如果有就把这个文件当作模块导入（据不完全统计，这是个坑，测试re模块没有问题，但是测试sys模块就有问题了）
查找模块路径下面有没有对应的模块名
如果没有找到模块名就报错
'''

'''
import是如何工作的？
模块在被导入的时候会执行以下三个步骤：
通过环境变量找到模块文件；
编译成字节码文件，如果有字节码文件则导入字节码文件；
执行模块中的代码来创建所定义的对象；
以上的三个步骤只有在程序运行时，模块被第一次导入时才会进行。如果已经导入了这个模块然后再次导入的时候会跳过上面的三个步骤，它会直接提取内存中已经加载的模块对象。
Python已经导入的模块会保存在sys.modules字典中。
'''