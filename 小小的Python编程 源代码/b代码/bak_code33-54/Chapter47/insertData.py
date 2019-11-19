#SELECT操作示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root",db="myshopdb",charset="utf8")

#创建游标对象
cursor = db.cursor()

#用户输入
while 1:
    print("=========添加员工==========")
    uid=int(input("员工id号："))
    nam=input("姓名：")
    sex=input("性别：")
    ent=input("入职日期（例:2016.01.24）：")
    dep=input("部门：")
    oth=input("备注：")
    val=(uid,nam,sex,ent,dep,oth)
    print("即将添加员工：",val)
    while 1:
        k=input("按【Enter】继续，按【B】重新输入，按【Q】退出")
        if k in ('','b','B','q','Q'):
            break
    if k=='':
        break
    elif k=='b' or k=='B':
        continue
    else:
        import sys
        sys.exit()
        

#SQL添加数据
sql5="""INSERT INTO employee
(id,
name,
sex,
enterdate,
department,
others)
VALUES"""+str(val)
print(sql5)
try:
    #执行SQL语句
    cursor.execute(sql5)
    #写数据的操作需要提交才会执行
    db.commit()
    print("添加成功")
except:
    db.rollback()
    print("添加失败")
    raise

#关闭数据库连接
db.close()
