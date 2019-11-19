from pyReptile.storage import *


# 定义电影信息表的字段
class MovieComment(DataStorage):
    def field(self):
        # 定义数据表字段
        self.movieId = Column(String(50), comment='电影ID')
        self.user = Column(String(50), comment='用户名')
        self.comment = Column(String(3000), comment='评论内容')


# 定义电影评论表的字段
class MovieInfo(DataStorage):
    def field(self):
        # 定义数据表字段
        self.movieId = Column(String(50), comment='电影ID')
        self.name = Column(String(50), comment='电影名称')
        self.summary = Column(String(3000), comment='剧情简介')
