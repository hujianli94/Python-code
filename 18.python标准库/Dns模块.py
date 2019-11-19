#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 11:03
# filename: Dns模块.py

# import dns.resolver
#
# domain = "www.baidu.com"
# A_domain_list = []
# A = dns.resolver.query(domain, 'A')
# for i in A.response.answer:
#     for j in i:
#         if j.rdtype == 1:
#             A_domain_list.append(j)
# for index, A_jilu in enumerate(A_domain_list):
#     print(domain + "的第{}条A记录为：{}".format(index, A_jilu))

# ## MX记录
# # （2）MX记录，邮件交换记录，定义邮件服务器的域名
# import dns.resolver
#
# mx = dns.resolver.query('163.com', 'MX')
# for i in mx.response.answer:
#     for j in i:
#         print(j)

# 检测ip域名是否正常
# 1)实现对域名解析，然后将A记录追加到list
# 2)对IP列表中的ip实现HTTP级别的探测

import os
import dns.resolver
import socket

list_ip = []
appdomain = "www.baidu.com"  # 定义域名


def get_ip_list(domain=""):
    try:
        A = dns.resolver.query(domain, "A")
    except Exception as e:
        print("dns resolver error: " + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                list_ip.append(j)
    return True


def checkip(address, port=80):
    s = socket.socket()
    print('Attempting to connect to %s on port %s' % (address, port))
    try:
        s.connect((address, port))
        print('Connected to %s on port %s status                  【OK】' % (address, port))
        print()
        return True
    except socket.error as e:
        print('Connection to %s on port %s 【failed】: %s' % (address, port, e))
        return False
    finally:
        s.close()


if __name__ == '__main__':
    if get_ip_list(appdomain) and len(list_ip) > 0:
        for i in list_ip:
            checkip(str(i))
    else:
        print("DNS resolver error........")

