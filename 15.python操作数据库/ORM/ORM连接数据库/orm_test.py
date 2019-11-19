#!/usr/bin/env python
#-*- coding:utf8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Boolean

engine = create_engine(
        "mysql+pymysql://root:123.com@127.0.0.1:3306/new_test?charset=utf8")
Base = declarative_base()

Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer,primary_key=True)
    title = Column(String(200),nullable=False)
    content = Column(String(200),nullable=False)
    types = Column(String(10),nullable=False)
    image = Column(String(300),)
    author = Column(String(20),)
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_valid = Column(Boolean)

def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123.com@127.0.0.1:3306/new_test?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)

class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        '''
        :return:新增记录
        '''
        new_obj = News(
            title = "标题",
            content = "内容",
            types = "百家",
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        """
        查询一条数据
        :return:
        """
        return self.session.query(News).get(1)

    def get_more(self):
        '''查询多条数据'''
        return self.session.query(News).all()

    def update_data(self,pk):
        """
        :param pk:  修改信息
        :return
        """
        new_obj = self.session.query(News).get(pk)
        #修改单条数据
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def delete_date(self,pk):
        '''
        :param pk:  删除信息
        :return:
        '''
        new_obj = self.session.query(News).get(1)
        self.session.delete(new_obj)
        self.session.commit()

def main():
    # init_db()
    obj = OrmTest()
    #-------------------------新增数据-----------------------
    # rest = obj.add_one()
    # print(rest.id)
    #------------------------查询数据------------------------
    # rest = obj.get_one()
    # if rest:
    #     print("ID:{0} --->{1}".format(rest.id, rest.title))
    # else:
    #     print("not exist....")

    #----------------------查询多条数据----------------------
    # rest = obj.get_more()
    # # print(rest)
    # for net_obj in rest:
    #     print("ID:{0} --->{1}".format(net_obj.id, net_obj.title))

    #---------------------修改数据----------------------------
    obj.update_data(1)

    #--------------------删除数据-----------------------------
    # obj.delete_date(1)

if __name__ == '__main__':
    main()


