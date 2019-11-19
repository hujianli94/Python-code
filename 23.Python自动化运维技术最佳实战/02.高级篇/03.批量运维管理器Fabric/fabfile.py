#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 21:42
# filename: fabfile.py
#!/usr/bin/env python
from fabric.api import run

def host_type():
    run('uname -s')