#!/usr/bin/env python
#-*- coding:utf8 -*-
#增加数据
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
import models

#1.创建连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

#2.从连接池中获取数据库连接
session = Session()
# session = scoped_session(Session)

# #3.执行ORM操作
# obj1 = models.Users(name="jack",email='jack@163.com')
# session.add(obj1)
# # 提交事务
# session.commit()

#批量增加,里面是列表
session.add_all([
    models.Users(name="jack1",email='jack1@163.com'),
    models.Users(name="jack2",email='jack2@163.com'),
])
session.commit()

# 4.关闭数据库连接
session.close()
