# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from scrapy.conf import settings

# 定义映射类
Base = declarative_base()
class scrapy_db(Base):
    __tablename__ = 'maoyan_db'
    id = Column(Integer(), primary_key=True)
    movieName = Column(String(100))
    performer = Column(String(100))
    releasetime = Column(String(200))
    score = Column(String(100))

class MaoyanPipeline(object):
    def __init__(self):
        # 初始化，连接数据库
        conntion = settings['MYSQL_CONNECTION']
        engine = create_engine(conntion, echo=False, pool_size=2000)
        DBSession = sessionmaker(bind=engine)
        self.SQLsession = DBSession()
        # 创建数据表
        Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        # 入库处理
        self.SQLsession.execute(scrapy_db.__table__.insert(),
                                {'movieName': item['movieName'],
                                 'performer': item['performer'],
                                 'releasetime': item['releasetime'],
                                 'score': item['score']})
        self.SQLsession.commit()
        return item
