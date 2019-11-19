#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
subprocess模块用于创建新的进程，并获取它的输入，输出以及错误信息，提供更高级的接口，
可以替换os.sysytem、os.spawn*、popen等
'''
import subprocess
print("call() test: ",subprocess.call(['python', 'te.py']))   #创建新进程运行程序，输入和输出绑定到父进程，返回新进程退出码
print('')
print('check_call() test:',subprocess.check_call(['python', 'te.py']))    #退出码为0整除返回，否则引发异常
print('')
print('getstatusoutput() test:',subprocess.getstatusoutput(['python', 'te.py']))  #元祖形式返回新进程的退出码和输出
print('')
print('check_output() test:',subprocess.check_output(['python', 'te.py']))    #返回新进程的输出

