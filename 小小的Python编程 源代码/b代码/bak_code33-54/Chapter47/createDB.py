#创建数据库示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root")

#创建游标对象
cursor = db.cursor()

#SQL创建数据库
sql1="CREATE DATABASE IF NOT EXISTS `myshopdb`"

#使用execute()方法执行SQL
try:
    cursor.execute(sql1)
    print("数据库创建成功")
except:
    print("数据库创建失败")
    raise

#关闭数据库连接
db.close()
