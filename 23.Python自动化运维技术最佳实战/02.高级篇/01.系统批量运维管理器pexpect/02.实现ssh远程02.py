#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 17:44
# filename: 02.实现ssh远程02.py
import pexpect
import sys

# 通过spawn类启动和控制子应用程序
child = pexpect.spawn('ssh root@192.168.0.100')
# 将pexpect的输入输出信息写到mylog.txt文件中
fout = open('mylog.txt', 'w')
child.logfile = fout

child.expect(['password:'])
# 字符串匹配则使用sendline进行回应-----send：发送命令，不回车、sendline：发送命令，回车、sendcontrol：发送控制符，如：sendctrol('c')等价于‘ctrl+c'、sendeof：发送eof
child.sendline('admin#123')
child.expect("#")
child.sendline('ls /home')
child.expect("#")
print("before:" + child.before)
print("after:" + child.after)
