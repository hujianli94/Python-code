#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
from Mysql_base_class import Mysql_SQL

hu = Mysql_SQL("192.168.2.122","root","123456","ttmgrportal")

res = hu.get_all("select * from student4 where money>100")
for row in res:
    print("%d -- %d" % (row[0], row[1]))