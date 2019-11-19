#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 14:12
# filename: 01.连接mysql数据库.py
import os
import pymysql as db


def get_conn(**kwargs):
    return db.connect(host=kwargs.get('host', 'localhost'),
                      user=kwargs.get('user'),
                      passwd=kwargs.get('passwd'),
                      port=kwargs.get('port', 3306),
                      db=kwargs.get('db'))


def execute_sql(conn, sql):
    """
    执行sql语句函数
    :param conn: cur数据库连接对象
    :param sql: 要执行的SQL
    :return:
    """
    with conn as cur:
        cur.execute(sql)


def create_table(conn):
    sql_drop_table = "DROP TABLE IF EXISTS student;"
    sql_create_table = """create table 'student'('sno' int(11) not null ,
    'sname' varchar(20) DEFAULT null,'sage' int(11) default null,
    primary key ('sno')) ENGINE=InnoDB default charset=utf-8"""

    for sql in [sql_drop_table, sql_create_table]:
        execute_sql(conn, sql)


def insert_data(conn, sno, sname, sage):
    INSERT_FORMAT = "insert into student values({0},'{1}',{2})"
    sql = INSERT_FORMAT.format(sno, sname, sage)
    execute_sql(conn, sql)


def main():
    mysql_info = {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "admin#123",
        "port": "3306",
        "db": "test"
    }

    conn = get_conn(**mysql_info)

    try:
        create_table(conn)
        insert_data(conn, 1, "zhangsan", 20)
        insert_data(conn, 1, "lisi", 21)

        with conn as cur:
            cur.execute("select * from student")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
