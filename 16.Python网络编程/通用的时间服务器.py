#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 16:54
# filename: 通用的时间服务器.py
import socket
import datetime
import sys

DEFAULT_PORT = 1234  # 指定默认端口


def timeServer(port):
    host = '0.0.0.0'  # 使用本机地址
    s = None

    # 在本机的所有地址监听
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socketype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socketype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.bind(sa)  # 绑定socket地址
            s.listen(10)  # 开始监听
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:  # 生成socket出错
        print("could not open socket")
        return 1

    while True:
        c, addr = s.accept()
        print("Get connection from", addr)
        date = datetime.datetime.now()
        date = str(date).encode('utf-8')
        c.send(date)  # 发送当前时间
        c.close()


if __name__ == '__main__':
    port = DEFAULT_PORT  # 设置端口为默认端口
    # 两种启动方式，直接python timeServer启动。或者指定端口 python timeServer 8888
    if len(sys.argv) > 1:  # 判断用户的输入
        try:
            port = int[sys.argv[1]]
            if port < 0 or port >= 65536:  # 端口范围判断
                port = DEFAULT_PORT
        except Exception as e:
            port = DEFAULT_PORT

    timeServer(port)
