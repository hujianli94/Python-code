#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/10 10:58
# filename: subpress_test.py
import subprocess


def exec_cmd(cmd, **kwds):
    """
    Execute arbitrary commands as sub-processes.
    """
    stdin = kwds.get('stdin', None)
    stdin_flag = None
    if not stdin is None:
        stdin_flag = subprocess.PIPE
    proc = subprocess.Popen(
        cmd,
        stdin=stdin_flag,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate(stdin)
    return (proc.returncode, stdout, stderr)


p = exec_cmd(['python', 'te.py'])
print(p)
print(p[0])
print(p[1])
