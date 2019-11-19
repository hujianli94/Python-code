#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 15:46
# filename: DB_info.py
import sqlite3

class Question_bank:
    '''
    设计题库
    '''

    def __init__(self):
        self.conn = sqlite3.connect('test2.db')
        self.curror = self.conn.cursor()  # 创建一个Cursor

    def create_db(self):
        '''
        生成试题库
        :return:
        '''
        # 执行一条SQL语句，创建exam表
        self.curror.execute(
            'create table [exam] ([question] varchar(80) null ,[Answer_A] varchar(1) null ,[Answer_B] varchar(1) null ,'
            '[Answer_C] varchar(1) null ,[Answer_D] varchar(1) null,[right_Answer] varchar(1) null )')

        # 继续执行一条SQL语句，插入一条数据
        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('哈雷彗星的平均周期为','54年','55年','73年','83年','C')")

        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('您的选择是，没有问题，碰运气','1','2','3','4','C')")

        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('中国历史上谁发明了麻药?','孙思邈','华佗','张仲景','扁鹊','B')")

        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('京剧中的花旦指的是?','年轻男子','年轻女子','年长男子','年长女子','B')")

        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('篮球比赛每队几人?','4','5','6','7','B')")

        self.curror.execute(
            "insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('在天愿做比翼鸟，在地愿做连理枝，讲述的是谁的爱情故事?','梁山伯和祝英台','胡健力和吴明','崔莺莺和张生','杨贵妃和唐明皇','B')")
        print(self.curror.rowcount)  # 通过rowcount获得插入的行数
        # self.curror.close()  # 关闭Cursor
        self.conn.commit()  # 提交事务
        # self.conn.close()  # 关闭Connection

    def read_info(self):
        '''
        读取试题信息
        :return:
        '''
        # 执行查询语句
        self.curror.execute('select * from exam')
        # 获得查询结果集
        values = self.curror.fetchall()
        return values

    def __del__(self):
        """
        析构函数，自动关闭游标连接和数据库连接
        :return:
        """
        self.curror.close()  # 关闭Cursor
        self.conn.close()  # 关闭Connection

# if __name__ == '__main__':
# a = Question_bank()
# print(a.read_info())
