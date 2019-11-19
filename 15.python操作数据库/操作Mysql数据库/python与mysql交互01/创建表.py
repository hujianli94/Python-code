#!/usr/bin/env python
#-*- coding:utf8 -*-

#导入PyMySQL模块
import pymysql

#调用connect()函数生成connection连接对象
db = pymysql.connect(host="39.96.10.11", user="hujianli",
                     password="admin#123", database="test_hu",
                     charset="utf8")

#调用cursor()方法，创建Cursor对象
cursor = db.cursor()
cursor.execute("drop table if EXISTS students2")
#执行SQL语句

sql = '''
create table students2(id int auto_increment primary key,name varchar(20) not null,
age int not null ,gender bit default 1,address varchar(20),isDelete bit default 0);
'''
"""
sql2 = '''
CREATE TABLE users (
  'name' varchar(32) NOT NULL,
  'age' int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY ('name')
) Full_backuk-2019-08-13_09_28_42.sql DEFAULT CHARSET=utf8
'''
"""
cursor.execute(sql)



#关闭连接
cursor.close()
db.close()