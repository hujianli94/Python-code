#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/8 22:07
# filename: subprocess01.py
import subprocess

pingP = subprocess.Popen(args='ping -n 4 www.baidu.com', shell=True, stdout=subprocess.PIPE)  # 生成ping进程
pingP.wait()  # 等待进程完成
print(pingP.stdout.read())  # 读取进程的输出信息
print(pingP.pid)
print(pingP.returncode)  # 打印进程返回值
