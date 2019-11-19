# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.files import FilesPipeline
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from scrapy.conf import settings

# SQLAlchemy映射数据表
Base = declarative_base()
class song(Base):
    # 表名
    __tablename__ = 'song'
    # 字段，属性
    song_id = Column(Integer, primary_key=True)
    song_name = Column(String(200))
    song_ablum = Column(String(200))
    song_interval = Column(String(200))
    song_songmid = Column(String(200))
    song_singer = Column(String(200))
    song_url = Column(String(2000))


# 数据入库
class MusicPipeline(object):
    def __init__(self):
        # 获取配置信息setting.py的数据库连接
        connection = settings['MYSQL_CONNECTION']
        # 连接数据库
        engine = create_engine(connection, echo=False)
        # 创建会话对象，用于数据表的操作
        DBSession = sessionmaker(bind=engine)
        self.SQLsession = DBSession()
        # 创建数据表
        Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        song_songmid = item['song_songmid']
        temp = self.SQLsession.query(song).filter_by(song_songmid=song_songmid).first()
        if temp:
            temp.song_name = item['song_name'],
            temp.song_ablum = item['song_ablum'],
            temp.song_interval = item['song_interval'],
            temp.song_singer = item['song_singer'],
            temp.song_url = item['song_url']
        elif 'vkey' in item['song_url']:
            data = song(
                song_name=item['song_name'],
                song_ablum=item['song_ablum'],
                song_interval=item['song_interval'],
                song_songmid=item['song_songmid'],
                song_singer=item['song_singer'],
                song_url=item['song_url']
            )
            self.SQLsession.add(data)
        self.SQLsession.commit()
        return item

# 下载文件
class DownloadMusicPipeline(FilesPipeline):
    # 重写get_media_requests
    def get_media_requests(self, item, info):
        # 设置文件名
        file_name = item['song_songmid'] + '.m4a'
        yield scrapy.Request(item['song_url'], meta={'name': file_name})

    # 重写file_path，命名文件名
    def file_path(self, request, response=None, info=None):
        file_name = settings['FILES_STORE'] + (request.meta['name'])
        return file_name