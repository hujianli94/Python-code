#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 18:18
# filename: 01.使用密码登录ssh方式1.py

import paramiko

hostname='192.168.0.103'
username='root'
password='admin#123'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=22,username=username,password=password,compress=True)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
stdin,stdout,stderr=ssh.exec_command('ifconfig| grep inet|head -1|awk -F\' \' \'{print $2}\'')
print stdout.read()
ssh.close()
