#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 21:48
# filename: simple01.py
from fabric.api import *

env.user='root'
env.hosts=['192.168.0.100','192.168.0.103']
env.password='admin#123'

@runs_once
def local_task():
    local("uname -a")

def remote_task():
    with cd("/data/logs"):
        run("ls -l")
