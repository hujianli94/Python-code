#!/usr/bin/env python
#-*- coding:utf8 -*-
import subprocess
prcs = subprocess.Popen(['python','check_port.py'],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        shell=True)
prcs.communicate("These strings are from stdin.")
print("subprcess pid: .", prcs.pid)
print('\nSTDOUT: ')
print(str(prcs.communicate()[0]))
print('STDERR: ')
print(str(prcs.communicate()[1]))

