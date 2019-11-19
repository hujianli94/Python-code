#!/usr/bin/env python
# -*- coding:utf8 -*-
import subprocess

'''
import subprocess
prcs = subprocess.Popen(['python','te.py'],
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
'''


def execute_cmd(cmd):
    prcs = subprocess.Popen(cmd,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = prcs.communicate()
    if prcs.returncode != 0:
        return prcs.returncode, stderr

    return prcs.returncode, prcs.stdout
