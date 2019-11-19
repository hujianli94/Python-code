#SELECT操作示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root",db="myshopdb",charset="utf8")

#创建游标对象
cursor = db.cursor()

#SQL查询表结构
sql4="""SELECT 
  COLUMN_NAME,  
  COLUMN_TYPE,  
  DATA_TYPE,  
  CHARACTER_MAXIMUM_LENGTH,  
  IS_NULLABLE,  
  COLUMN_DEFAULT,  
  COLUMN_COMMENT   
FROM 
 INFORMATION_SCHEMA.COLUMNS 
where 
table_name  = 'employee'"""
try:
    cursor.execute(sql4)
    # 获取所有记录列表
    data = cursor.fetchall()
    #print(data)
    for field in data:
        # 打印结果
        print ("字段：", field)
except:
    print("查询失败")
    raise

#关闭数据库连接
db.close()
