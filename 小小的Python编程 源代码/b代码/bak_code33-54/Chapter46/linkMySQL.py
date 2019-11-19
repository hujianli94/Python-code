#连接MySQL数据库示例

#引入必要模块 
import pymysql
 
#创建数据库连接
db = pymysql.connect("localhost","root","root")
 
#创建一个游标对象 cursor
cursor = db.cursor()
 
#执行SQL语句
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("数据库版本: %s " %data )
 
# 关闭数据库连接
db.close()
