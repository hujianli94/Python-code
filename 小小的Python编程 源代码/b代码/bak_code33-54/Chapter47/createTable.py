#创建数据表示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root",db="myshopdb",charset="utf8")

#创建游标对象
cursor = db.cursor()

#SQL创建数据表
sql3="""DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `enterdate` datetime DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  `others` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

 
#使用execute()方法执行SQL
try:
    cursor.execute(sql3)
    print("数据表创建成功")
except:
    print("数据表创建失败")
    raise

sql4="""SELECT * FROM employee"""
try:
    cursor.execute(sql4)
    print("查询成功")
except:
    print("查询失败")
    raise

#查询结果
data=cursor.fetchone()
print("表employee的字段：%s" %data)

#关闭数据库连接
db.close()
