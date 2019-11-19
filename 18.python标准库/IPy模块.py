#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 10:45
# filename: IPy模块.py
from IPy import IP

ip_s = input("Please input an IP or net-range: ")   #接收输入
ips = IP(ip_s)

if len(ips)>1:
    print("net:{}".format(ips.net()))       #输出网络地址
    print("netmask:{}".format(ips.netmask()))   #输出网络掩码地址
    print("broadcast:{}".format(ips.broadcast()))   #输出广播地址
    print("reverse address:{}".format(ips.reverseNames()[0]))   #输出地址反向解析
    print("subnet:{}".format(len(ips)))     #输出子网数
else:               #为单个地址
    print("reverse address:{}".format(ips.reverseNames()[0]))       #输出IP反向解析

print("hexadecimal:【{}】".format(ips.strHex()))        #输出十六进制地址
print("binary ip:【{}】".format(ips.strBin()))       #输出二进制地址
print("iptype:【{}】".format(ips.iptype()))           #输出地址类型，