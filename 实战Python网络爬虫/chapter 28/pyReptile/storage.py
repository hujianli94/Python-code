from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pymongo import MongoClient
import csv
import os

Base = declarative_base()

# 定义数据存储类DataStorage
class DataStorage(object):
    def __init__(self, CONNECTION, **kwargs):
        self.databaseType = kwargs.get('databaseType', 'CSV')
        # 根据参数databaseType选择存储方式，默认CSV文件存储
        if self.databaseType == 'SQL':
            # 根据字段创建映射类和数据表
            self.field()
            tablename = kwargs.get('tablename', self.__class__.__name__)
            self.table = self.table(tablename)
            self.DBSession = self.connect(CONNECTION)
        elif self.databaseType == 'NoSQL':
            self.DBSession = self.connect(CONNECTION)
        else:
            self.path = CONNECTION

    # 定义数据表字段
    def field(self):
        # self.name = Column(String(50))
        pass

    # 连接数据库，生成DBSession对象
    def connect(self, CONNECTION):
        # 连接关系型数据库
        if self.databaseType == 'SQL':
            engine = create_engine(CONNECTION)
            DBSession = sessionmaker(bind=engine)()
            Base.metadata.create_all(engine)
        # 连接非关系型数据库
        else:
            info = CONNECTION.split('/')
            # 连接Mongo数据库
            connection = MongoClient(
                info[0],
                int(info[1])
            )
            db = connection[info[2]]
            DBSession = db[info[3]]
        return DBSession

    # 定义映射类
    def table(self, tablename):
        class TempTable(Base):
            __tablename__ = tablename
            id = Column(Integer, primary_key=True)
        # 将类属些进行判断，符合sqlalchemy的字段则定义到数据映射类
        for k, v in self.__dict__.items():
            if isinstance(v, Column):
                setattr(TempTable, k, v)
        return TempTable

    # 插入数据
    def insert(self, value):
        # 关系型数据库的数据插入
        if self.databaseType == 'SQL':
            self.DBSession.execute(self.table.__table__.insert(), value)
            self.DBSession.commit()
        # 非关系型数据库的数据插入
        elif self.databaseType == 'NoSQL':
            # 判断参数value的数据类型，选择单条数据还是多条数据插入
            if isinstance(value, list):
                self.DBSession.insert_many(value)
            else:
                self.DBSession.insert(value)

    # 更新数据
    def update(self, value, condition={}):
        # 关系型数据库的数据更新
        if self.databaseType == 'SQL':
            # 更新条件只设置了单个条件
            if condition:
                c = self.table.__dict__[list(condition.keys())[0]].in_(list(condition.values()))
                self.DBSession.execute(self.table.__table__.update().where(c).values(), value)
            # 全表更新
            else:
                self.DBSession.execute(self.table.__table__.update().values(), value)
            self.DBSession.commit()
        # 非关系型数据库的数据更新
        elif self.databaseType == 'NoSQL':
            self.DBSession.update_many(condition, {'$set': value})

    # 文件下载
    def getfile(self, content, filepath):
        with open(filepath, 'wb') as code:
            code.write(content)

    # 数据写入CSV文件
    def writeCSV(self, value, title=[]):
        # 参数title为空列表，则将字典的keys进行排序并作为CSV的标题
        if not title:
            title = sorted(value[0].keys())
        # 判断文件是否存在，
        pathExists = os.path.exists(self.path)
        with open(self.path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # 文件不存在，则写入标题
            if not pathExists:
                csv_writer.writerow(title)
            # 将数据写入CSV文件
            for v in value:
                valueList = []
                for t in title:
                    valueList.append(v[t])
                csv_writer.writerow(valueList)
