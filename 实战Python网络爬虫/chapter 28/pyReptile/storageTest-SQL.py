from storage import *

# 定义数据表personinfo
class PersonInfo(DataStorage):
    def field(self):
        # 定义数据表字段
        # self.name = Column(String(50))
        self.name = Column(String(50), comment='姓名')
        self.age = Column(String(50), comment='年龄')
        self.address = Column(String(50), comment='地址')

# 定义数据表schoolinfo
class SchoolInfo(DataStorage):
    def field(self):
        # 定义数据表字段
        # self.name = Column(String(50))
        self.school = Column(String(50), comment='学校')
        self.name = Column(String(50), comment='姓名')

if __name__=='__main__':
    CONNECTION = 'mysql+pymysql://root:1234@localhost/storage_db?charset=utf8mb4'
    person = PersonInfo(CONNECTION, databaseType='SQL')
    school = SchoolInfo(CONNECTION, databaseType='SQL')
    # 对personInfo表插入多条数据
    personInfo = [{'name': 'Lucy', 'age': '21', 'address': '北京市'},
                  {'name': 'Lily', 'age': '18', 'address': '上海市'}]
    person.insert(personInfo)
    # 对schoolInfo表插入单条数据
    schoolInfo = {'name': 'Lucy', 'school': '清华大学'}
    school.insert(schoolInfo)

    # 对personInfo表更新数据
    condition = {'id': 1}
    personInfo = {'name': 'Lucy', 'age': '22', 'address': '广州市'}
    person.update(personInfo, condition)
    # 对schoolInfo表更新数据
    schoolInfo = {'name': 'Lucy', 'school': '北京大学'}
    school.update(schoolInfo, condition)
