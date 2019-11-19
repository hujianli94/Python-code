#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/19 17:36
# filename: apgparse模块.py

# import argparse
#
#
# def _argparse():
#     parser = argparse.ArgumentParser(description="This is description")
#     parser.add_argument("--host", action="store",
#                         dest="server", default="localhost", help="connect to host")
#     parser.add_argument("-t", action="store_true",
#                         dest="boolean_switch", default=False, help="Set a switch to true")
#     return parser.parse_args()
#
#
# def main():
#     parser = _argparse()
#     print(parser)
#     print("host = ", parser.server)
#     print("boolean_switch=", parser.boolean_switch)
#
#
# if __name__ == '__main__':
#     main()


import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="A Python-MySQL client")
    parser.add_argument("--host", action="store",
                        dest="host", required=True, help="connect to host")

    parser.add_argument("-u", "--user", action="store",
                        dest="user", required=True, help="user for login")

    parser.add_argument("-p", "--password", action="store",
                        dest="password", required=True,
                        help="password to use when connecting to server")

    parser.add_argument("-P", "--port", action="store",
                        dest="port", default=3306, type=int,
                        help="port number to use for connection or 3306 for default")
    parser.add_argument("-v", "--version", action="version", version='%(prog)s 0.1')
    return parser.parse_args()

def main():
    parser = _argparse()
    conn_args = dict(host=parser.host, user=parser.user,
                     password=parser.password,port=parser.port)
    print(conn_args)

if __name__ == '__main__':
    main()