#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
TCPServer
UDPServer
ThreadingTCPServer
ThreadingUDPServer

socketserver模块中使用的处理器类主要有StreamRequestHandler(基于TCP协议的)和DatagramRequestHandler(基于UDP协议的)
三个方法：
setup()     #为请求准备请求处理器（请求处理的初始化工作）
handler()       #完成具体的请求处理工作（解析请求、处理数据、发出响应）
finish()        #清理请求处理器相关数据
一般，自定义一个简单的请求处理器，只需覆盖handler()方法即可
'''
import socketserver
HOST = "localhost"
PORT = 10888

class MyTcpHandler(socketserver.StreamRequestHandler):
    '''
    定义了一个继承自StreamRequestHandler的处理器类，覆盖了handler()方法
    然后实例化TCPServer类，调用serve_forever()方法启动服务器
    '''
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                Server.shutdown()
                break
            print("Receive Data:", data.decode())
            self.request.send(data)
        return
Server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
Server.serve_forever()