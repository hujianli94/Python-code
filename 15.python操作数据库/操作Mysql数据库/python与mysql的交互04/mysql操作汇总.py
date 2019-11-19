#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 17:20
# filename: mysql操作汇总.py

'''
# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='admin#123', db='test001', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION();')
data = cursor.fetchone()
print("Database version:", data)
cursor.execute('create database test001 DEFAULT CHARACTER SET utf8')
cursor.close()
db.close()

'''

'''
db = pymysql.connect(host='localhost', user='root', password='admin#123', db='test001', port=3306)
cursor = db.cursor()
# 创建数据库表
sql = """
 CREATE TABLE `students` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`)
"""
cursor.execute(sql)
cursor.close()
db.close()

'''

'''
# 插入数据
db = pymysql.connect(host='localhost', user='root', password='admin#123', port=3306, db='test001')
cursor = db.cursor()
id = '19940722'
user = 'hujianli12'
age = 21
sql = 'insert into students(id, name, age) values (%s,%s,%s)'

try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
'''

'''
# 插入、更新、删除操作都是对数据库进行更改的操作，更改操作都必须为一个事务，所以这些操作的标准写法就是：
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

'''

'''
# 更新数据
db = pymysql.connect(host='localhost', user='root', password='admin#123', port=3306, db='test001')
cursor = db.cursor()

sql = 'update students set age=%s where name = %s '

try:
    cursor.execute(sql, (18, 'hujianli'))
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
'''

'''
# 删除数据
db = pymysql.connect(host='localhost', user='root', password='admin#123', port=3306, db='test001')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'
sql = 'delete from {} where {}'.format(table, condition)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
'''

'''
# 查询数据库
db = pymysql.connect(host='localhost', user='root', password='admin#123', port=3306, db='test001')
cursor = db.cursor()

sql = 'select * from students where age >=10;'

try:
    cursor.execute(sql)
    print("Count:", cursor.rowcount)
    row = cursor.fetchone()

    # 方式1
    # result = cursor.fetchall()
    # print("Result:", result)
    # print("Result Type:", type(result))
    # for row in result:
    #     print(row)

    # 方式2
    while row:
        print("Row: ", row)
        row = cursor.fetchone()

except:
    print("Error")

cursor.close()
db.close()


'''
