import pymongo
# 创建对象，连接本地数据库。
# 方法一：
client = pymongo.MongoClient()
# 方法二：
client = pymongo.MongoClient('localhost', 27017)
# 方法三：
client = MongoClient('mongodb://localhost:27017/')
# 连接DB数据库
db = client['DB']
# 连接集合user，集合类似关系数据库的数据表
# 如果集合不存在，会新建集合user
user_collection = db.user
# 设置文档格式（文档即我们常说的数据）
