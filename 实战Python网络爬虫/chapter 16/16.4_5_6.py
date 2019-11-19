import pymongo
import datetime
import re
# 创建对象
client = pymongo.MongoClient()
# 连接DB数据库
db = client['DB']
# 连接集合user，集合类似关系数据库的数据表
# 如果集合不存在，会新建集合user
user_collection = db.user
# 设置文档格式（文档即我们常说的数据）
user_info = {
	    "_id": 100,
	    "author": "小黄",
         "text": "Python爬虫开发",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

# 使用insert_one单条添加文档，inserted_id获取写入后id
# 添加文档时，如果文档尚未包含"_id"键，则会自动添加"_id"。 "_id"的值在集合中必须是唯一。
# inserted_id是获取添加后的id，若不需要可去掉。
user_id = user_collection.insert_one(user_info).inserted_id
print ("user id is ", user_id)

#批量添加
user_infos = [{
	    "_id": 101,
	    "author": "小黄",
         "text": "Python爬虫开发",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()},
	 {
	    "_id": 102,
	    "author": "小黄_A",
         "text": "Python爬虫开发_A",
         "tags": {"db":"Mongodb", "lan":"Python", "modle":"Pymongo"},
         "date": datetime.datetime.utcnow()},
		 ]
# inserted_ids是获取添加后的id，若不需要可直接去掉。
user_id = user_collection.insert_many(user_infos).inserted_ids
print ("user id is ", user_id)

# 第16.5章节
# 更新单条文档
# update( 筛选条件 , 更新内容 )。筛选条件为空，默认更新第一条文档
user_collection.update(
{},
{"$set":{"author":" 小黄 ","text":"Python 爬虫 "}}
)
# 批量更新文档，只要将方法 update 改为 update_many 即可

# 第16.6章节
# 查询文档 ,find({"_id":101}), 其中 {"_id":101} 为查询条件，若查询条件为空，则默认查询全部
find_value = user_collection.find({"_id":101})
print(list(find_value))

# AND 条件查询
find_value = user_collection.find({
"$and":[{"_id":101},{"author":" 小黄 "}]
})
print(list(find_value))
# OR 条件查询
find_value = user_collection.find({
"$or":[{"author":" 小黄 _A"},{"author":" 小黄 "}]
})
print(list(find_value))

# 如查找 id>100 而 <102，即 _id=101 的文档
find_value = user_collection.find({
"_id":{"$gt":100,"$lt":102}
})
print(list(find_value))
# 查找 id 在 [100,101]
find_value = user_collection.find({
"_id":{"$in":[100,101]}
})
print(list(find_value))

find_value = user_collection.find({
"$and": [{"_id": {"$gt":100,"$lt":102}, {"_id": {"$in": [100,101]}]
})
print(list(find_value))

# 模糊查询实际上是加入正则表达式实现
# 方法一：
find_value = user_collection.find({
"author": {"$regex": ".* 小 .*"}
})
print(list(find_value))
# 方法二：
regex = re.compile(".* 小 .*")
find_value = user_collection.find({
"author": regex
})
print(list(find_value))

# 查询嵌入 / 嵌套文档
# 查询字段 "tags": {"db":"Mongodb", "lan":"Python", "modle":"Pymongo"}
# 查询嵌套字段 , 只需要查询嵌套里的某个值即可
find_value = user_collection.find({
"tags.db": "Mongodb"
})
print(list(find_value))

# 查询字段 "tags": {"db": {"Mongodb":"NoSql","MySql":"Sql"},"lan":"Python", "modle":"Pymongo"}
find_value = user_collection.find({
"tags.db.Mongodb": "NoSql"
})
print(list(find_value))