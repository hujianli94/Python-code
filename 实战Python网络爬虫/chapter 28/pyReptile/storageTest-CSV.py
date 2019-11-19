from storage import *

if __name__ == '__main__':
    CONNECTION = 'data.csv'
    # 待存储数据personInfo
    personInfo = [{'name': 'Lucy', 'age': '21', 'address': '北京市'},
                  {'name': 'Lily', 'age': '18', 'address': '上海市'}]
    # 实例化数据存储类DataStorage
    database = DataStorage(CONNECTION)
    # 调用writeCSV()实现CSV文件存储
    # database.writeCSV(personInfo)
    database.writeCSV(personInfo, title=['name', 'age', 'address'])

