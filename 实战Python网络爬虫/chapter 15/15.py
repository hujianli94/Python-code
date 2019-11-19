# 连接数据库
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://root:1990@localhost:3306/test?charset=utf8",
    echo=True)

# 创建数据表方法一
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class mytable(Base):
    # 表名
    __tablename__ = 'mytable'
    # 字段，属性
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    birth = Column(DateTime)
    class_name = Column(String(50))

Base.metadata.create_all(engine)

# 创建数据表方法二
from sqlalchemy import Column, MetaData, ForeignKey, Table
from sqlalchemy.dialects.mysql import (INTEGER, CHAR)
meta = MetaData()
myclass = Table('myclass', meta,
                Column('id', INTEGER, primary_key=True),
                Column('name', CHAR(50), ForeignKey(mytable.name)),
                Column('class_name', CHAR(50))
                )
myclass.create(bind=engine)

# 删除数据表
#myclass.drop(bind=engine)
#Base.metadata.drop_all(engine)

# 第10.5章节
new_data = mytable(name='Li Lei',age=10,birth='2017-10-01',class_name='一年级一班')
session.add(new_data)
session.commit()
session.close()

# 第10.6章节
session.query(mytable).filter_by(id=1).update({ mytable.age : 12})
session.commit()
session.close()
###########
get_data = session.query(mytable).filter_by(id=1).first()
get_data.class_name = '三年级三班'
session.commit()
session.close()

# 第10.7章节
# 查询myclass全部数据
get_data = session.query(myclass).all()
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
session.close()
#################################

get_data = session.query(myclass.name, myclass.class_name).all()
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
session.close()
#################################

# 根据条件查询某条数据
# 筛选方法一：
# get_data = session.query(myclass).filter(myclass.id==1).all()
# 筛选方法二：
get_data = session.query(myclass).filter_by(id=1).all()
print('数据类型是：' + str(type(get_data)))
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
#################################

get_data = session.query(myclass).filter_by(id=1).first()
print('数据类型是：' + str(type(get_data)))
print('我的名字是：' + get_data.name)
print('我的班级是：' + get_data.class_name)
#################################

get_data = session.query(mytable).filter(mytable.id >= 2, 
             mytable.class_name == '三年级二班').first()
print('数据类型是：' + str(type(get_data)))
print('我的名字是：' + get_data.name)
print('我的班级是：' + get_data.class_name)
#################################

# 内连接
get_data = session.query(mytable).join(myclass).filter(mytable.class_name == '三年级二班').all()
print('数据类型是：' + str(type(get_data)))
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
# 外连接
get_data = session.query(mytable).outerjoin(
             myclass).filter(mytable.class_name == '三年级二班').all()
#################################

sql = 'select * from mytable '
session.execute(sql)
# 如果涉及更新，添加数据，需要session.commit()
session.commit()
