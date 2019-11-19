#!/usr/bin/env python
#-*- coding:utf8 -*-
import module_test

module_test.m_t_pr()            #调用导入模块的函数
print("使用module_test模块中的变量：",module_test.name)


#通过路径查找之后导入模块
import sys,os
PATH = os.path.dirname(os.path.abspath(__file__)) + "\module"
sys.path.append(PATH)
import module_test2
module_test2.m_t_pr()
print("使用module_test模块中的变量：",module_test2.name)
