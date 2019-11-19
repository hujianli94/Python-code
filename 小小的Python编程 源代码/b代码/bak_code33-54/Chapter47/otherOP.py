#SELECT操作示例

import pymysql
#创建数据库连接
db = pymysql.connect("localhost","root","root",db="myshopdb",charset="utf8")

#创建游标对象
cursor = db.cursor()

#SQL查询
def selectAll():
    sql6="SELECT * FROM employee"
    try:
        #执行SQL语句
        cursor.execute(sql6)
        #显示查询结果
        print("查询结果：")
        data=cursor.fetchall()
        for row in data:
            print(row)
    except:
        print("查询失败")
        raise

def selectOne(uid):
    sql7="SELECT * FROM employee WHERE id= "+uid
    try:
        #执行SQL语句
        cursor.execute(sql7)
        #显示查询结果
        data=cursor.fetchall()
        for row in data:
            print(row)
    except:
        print("查询失败")
        raise    

#修改
def modify():
    modiId=input("输入需要修改记录的id号：")
    selectOne(modiId)
    input("即将修改该条记录。")
    modiField=int(input("修改内容（【1】部门【2】备注）："))
    modiContent=input("修改为：")
    if modiField==1:
        field='department'
    elif modiField==2:
        field='others'
    sql8="UPDATE employee SET "+ field+" = '"+modiContent+"' WHERE id = "+modiId
    print(sql8)
    try:
        #执行SQL语句
        cursor.execute(sql8)
        db.commit()
        selectAll()
    except:
        db.rollback()
        raise

#删除
def delete():
    delId=input("输入需要删除记录的id号：")
    sql9="DELETE FROM employee WHERE id= "+delId
    selectOne(delId)
    confirm=input("即将删除该条记录（输入【Y】确定）：")
    if confirm=='Y':
        try:
            #执行SQL语句
            cursor.execute(sql9)
            db.commit()
            print("已删除，更新数据如下：")
            selectAll()
        except:
            db.rollback()
            raise

selectAll()
choose=int(input("选择操作（【1】修改；【2】删除）"))
if choose==1:
    modify()
elif choose==2:
    delete()
    
#关闭数据库连接
db.close()
print("数据库连接已关闭")
