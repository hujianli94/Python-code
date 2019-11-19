#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 22:00
# filename: simple02.py

from fabric.api import *

env.user='root'
env.hosts=['192.168.0.100','192.168.0.103']
env.password="admin#123"

@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l "+dirname)

@task
def go():
    getdirname = input_raw()
    worktask(getdirname)