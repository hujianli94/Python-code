#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 18:32
# filename: 02.实现文件上传、下载、创建、删除.py
import paramiko

username = 'root'
password = 'admin#123'
hostname = '192.168.0.103'
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 上传文件
    sftp.put('/home/python-scripts/02.高级篇/02.系统批量运维管理器paramiko/syslogin.log',
             '/home/syslogin.log')
    # 下载文件
    sftp.get('/home/vagrant_2.2.4_x86_64.rpm',
             '/home/python-scripts/02.高级篇/02.系统批量运维管理器paramiko/vagrant_2.2.4_x86_64.rpm')

    # 创建目录
    sftp.mkdir("/home/python-scrpts", 0775)  # 创建目录
    # 删除目录
    sftp.rmdir('/home/test1')

    # 文件重命名
    sftp.rename('/home/aaaa', '/home/aaaa_bak')

    # 打印文件信息
    print(sftp.stat('/home/apache-tomcat-8.5.37.tar.gz'))
    # 打印目录列表
    print(sftp.listdir('/home'))
    t.close()
except Exception as e:
    print(str(e))
