import pymongo
# 用户验证方法一
client = pymongo.MongoClient()
db_auth = client.admin
db_auth.authenticate(username, password)
# 连接DB数据库
db = client['DB']
# 用户验证方法二
client = MongoClient('mongodb://username:password@localhost:27017/')
# 连接DB数据库
db = client['DB']
