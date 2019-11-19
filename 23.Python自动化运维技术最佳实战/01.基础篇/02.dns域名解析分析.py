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