from storage import *

if __name__ == '__main__':
    CONNECTION = 'localhost/27017/test/storage_db'
    # 实例化数据存储类DataStorage
    database = DataStorage(CONNECTION, databaseType='NoSQL')
    # 插入多条数据
    personInfo = [{'name': 'Lucy', 'age': '21', 'address': '北京市'},
                  {'name': 'Lily', 'age': '18', 'address': '上海市'}]
    database.insert(personInfo)
    # 插入单条数据
    value = {'name': 'Tom', 'age': '21', 'address': '北京市'}
    database.insert(value)
    # 更新数据
    condition = {'name': 'Lucy'}
    updateInfo = {'name': 'Lucy', 'age': '22', 'address': '广州市'}
    database.update(updateInfo, condition)

