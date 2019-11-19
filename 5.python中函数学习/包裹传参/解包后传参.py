#!/usr/bin/env python
# -*- coding:utf8 -*-
def unpackage(mysql_user, mysql_passwd, port):
    print(mysql_user, mysql_passwd, port)


package = (1, 2, 3)
unpackage(*package)

key_vlaue = {"mysql_user": "root", "mysql_passwd": "admin#123", "port": 3306}
unpackage(**key_vlaue)

print("".center(100, "-"))


def foo(name, *nams):
    print("name参数:", name)
    print("nams参数:", nams)


my_tuple = (1, 2, 3, 4)

foo("hujianli", *my_tuple)
