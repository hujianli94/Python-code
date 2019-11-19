#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/26 11:37
# filename: subprocess上交花束.py
import subprocess
processes = []
psum =5

for i in range(psum):
    processes.append(subprocess.Popen(['python', 'protest9.py'],
                                      stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      universal_newlines=True,
                                      shell=True))


processes[0].communicate('0 bouquet of flowers!')
for before,after in zip(processes[:psum],processes[1:]):
    after.communicate(before.communicate()[0])
print("\n Sum of Processes: %d" % psum)
print()
for item in processes:
    print(item.communicate()[0])