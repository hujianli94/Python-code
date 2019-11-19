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
import redis

# 定义映射类
Base = declarative_base()
class scrapy_db(Base):
    __tablename__ = 'douban_db'
    id = Column(Integer(), primary_key=True)
    movieId = Column(String(100))
    comment = Column(String(2000))

class DoubanPipeline(object):
    def __init__(self):
        # 连接Redis数据库
        self.redis_db = redis.Redis(host='127.0.0.1', port=6379, db=1)
        self.redis_data_dict = 'keys'
        # 初始化，连接数据库
        conntion = settings['MYSQL_CONNECTION']
        engine = create_engine(conntion, echo=False, pool_size=2000)
        DBSession = sessionmaker(bind=engine)
        self.SQLsession = DBSession()
        # 创建数据表
        Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        # 判断数据库Redis是否存在URL
        for i, v in enumerate(item['movieInfo']):
            if self.redis_db.hexists(self.redis_data_dict, v):
                # 若存在，输出数据库已存在数据
                print('数据库已经存在该条数据')
            else:
                # 不存在，写入数据库Redis
                self.redis_db.hset(self.redis_data_dict, v, 0)
                # 入库处理
                self.SQLsession.execute(scrapy_db.__table__.insert(),
                                    {'comment': v['comment'].replace("\n", ""),
                                     'movieId': v['movieId']})
                self.SQLsession.commit()
        return item