#删除数据库示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root")

#创建游标对象
cursor = db.cursor()

#SQL删除数据库
sql2="DROP DATABASE IF EXISTS `testdb`"
 
#使用execute()方法执行SQL
try:
    cursor.execute(sql2)
    print("数据库已不复存在")
except:
    print("数据库删除失败")
    raise

#关闭数据库连接
db.close()
