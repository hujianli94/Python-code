#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/13 13:03
# filename: tran_mysql.py
import re
import time
import subprocess
import os
import sys
import datetime, time
import shutil

# import pymysql

# AWS_RDS = '192.168.2.100'

All_Database = []  # All databases
All_Tables1 = []  # All Tables


def exec_cmd(cmd):
    """
    Execute arbitrary commands as sub-processes.
    """
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True)
    stdout, stderr = proc.communicate()
    return (proc.returncode, stdout, stderr)


def sql_export_cmd(sql_cmd):
    status_info = exec_cmd(sql_cmd)
    Sql_name = sql_cmd.split(">")[1]
    if status_info[0] == 0:
        print("Database {} backup succeeded....".format(Sql_name))
    else:
        print("Database {} backup failed.....".format(Sql_name))
        sys.exit(1)


def sql_import_cmd(sql_cmd):
    status_info = exec_cmd(sql_cmd)
    Sql_name = sql_cmd.split("<")[1]
    if status_info[0] == 0:
        print("Database import {} succeeded....".format(Sql_name))
    else:
        print("Database import {} failed....".format(Sql_name))
        sys.exit(1)


def show_databases(cmd='mysql -uroot -padmin#123! -e "show databases;" | grep -v Database|xargs'):
    # cmd = 'mysql -uroot -padmin#123! -e "show databases;" | grep -v Database|xargs'
    status_info = exec_cmd(cmd)
    status_info = str(status_info[1])
    All_Database.append(status_info)
    return All_Database[0].split()


class Format_conversion(object):
    def __init__(self):
        self.User = "root"
        self.Password = "admin#123!"
        self.Exclude_database = ['information_schema', 'mysql', 'performance_schema', 'sys']
        self.backup_time = time.strftime('%Y-%m-%d_%H')

    def __backup_All_databases(self):
        sql_cmd = "mysqldump -u{0} -p{1} --all-databases > Full-backup-{2}.sql"
        sql_cmd = sql_cmd.format(self.User, self.Password, self.backup_time)
        # print(sql_cmd % (Mysql_User, Mysql_Passwd, backup_time))
        sql_export_cmd(sql_cmd)

    def __export_One_databases(self, onedb):
        """
        导出单个数据库的所有数据到本地
        :param table:
        :return:
        """
        sql_cmd = "mysqldump -u{0} -p{1} {2} > {3}-backup-{4}.sql"
        sql_cmd = sql_cmd.format(self.User, self.Password, onedb, onedb, self.backup_time)
        sql_export_cmd(sql_cmd)

    def __alter(self, file, old_str="ENGINE=MyISAM", new_str="ENGINE=InnoDB"):
        """

        :param file: 需要改变编码的文件
        :param old_str: 改变编码前的字段
        :param new_str: 改变后的字段
        :return:
        """
        backup_fname = "%s_bak.sql" % file.split('.')[0]

        flag = False  # 标志符
        index = 0  # 计数器

        # python2x中如下
        # with open(file, "r") as f1, open(backup_fname, "w") as f2:
        #     for line in f1:
        #         f2.write(re.sub(old_str, new_str, line, re.I))
        # with open(backup_fname, "r") as f_check:
        #     for line in f_check:
        #         if re.search(new_str, line, re.I):
        #             flag = True
        #             index += 1
        # if flag:
        #     print("Total conversion completed, converted {} second".format(index))
        # else:
        #     raise Exception("Conversion failed!!")
        #


        # python3x
        with open(file, "r", encoding='utf-8', errors='ignore') as f1, open(backup_fname, "w",
                                                                            encoding='utf-8',
                                                                            errors='ignore') as f2:
            for line in f1:
                f2.write(re.sub(old_str, new_str, line, re.I))
        with open(backup_fname, "r", encoding='utf-8', errors='ignore') as f_check:
            for line in f_check:
                if re.search(new_str, line, re.I):
                    flag = True
                    index += 1
        if flag:
            print("Total conversion completed, converted {} second".format(index))
        else:
            raise Exception("Conversion failed!!")
        old_path_dir = backup_fname.split('-')[0]

        if not os.path.exists(old_path_dir):
            os.mkdir(old_path_dir)
            shutil.move(file, old_path_dir)
        else:
            shutil.rmtree(old_path_dir)
            os.mkdir(old_path_dir)
            shutil.move(file, old_path_dir)

        os.rename(backup_fname, file)

    def __Conversion_database_engine(self, filename):
        """
        转换数据库引擎
        # filename = "Full_backuk-2019-08-13_09_28_42.sql"
        # ENGINE=MyISAM改为 ENGINE=innodb;
        :return:
        """
        self.__alter(filename, "ENGINE=MyISAM", "ENGINE=InnoDB")
        # self.__alter(filename,  "ENGINE=InnoDB", "ENGINE=MyISAM")

    def __delete_Database_db(self):
        """
        删除数据库，删除前，再次备份，删除前先确认。提示！
        :return:
        """
        pass

    def __create_Database_db(self):
        """
        根据数据库名称创建本地目录结构
        :return:
        """
        database_name = show_databases()
        for dbname in database_name:
            if not os.path.exists(dbname):
                os.mkdir(dbname)
                print("创建目录 {} 完毕.....".format(dbname))

    def __import_databases(self, Conversion_list=None):
        cmd = "reset master;"
        sql_cmd = 'mysql -u{0} -p{1} -e "{2}"'.format(self.User, self.Password, cmd)
        # print(sql_cmd)
        status_info = exec_cmd(sql_cmd)
        # print(status_info[0])
        if status_info[0] == 0:
            print("{} complete！".format(sql_cmd))
            print("Ready to start importing the database...")
        else:
            raise Exception("Database import failed！！！")

        Conversion_list = [] if Conversion_list is None else Conversion_list  # Conversion list
        list_sql_file = os.listdir('.')
        for sql_files in list_sql_file:
            if str(sql_files).endswith(".sql"):
                Conversion_list.append(sql_files)
        for sql_file in Conversion_list:
            if str(sql_file).startswith('Full-'):
                continue
            ql_cmd = "mysql -u{0} -p{1} {2} < {3}".format(self.User, self.Password, sql_file.split('-')[0], sql_file)
            # print(ql_cmd)
            sql_import_cmd(ql_cmd)
            time.sleep(0.5)

    def back_All_db(self):
        """
        备份全库
        :return:
        """
        self.__backup_All_databases()

    def Export_One_databasename(self):
        """
        导出排除'information_schema', 'mysql', 'performance_schema', 'sys'之外的数据库到当前目录
        :return:
        """
        cmd = 'mysql -u{0} -p{1} -e "show databases;" | grep -v Database|xargs'.format(self.User, self.Password)
        db_name_show = show_databases(cmd)
        for one_db_name in db_name_show:
            if one_db_name not in self.Exclude_database:
                self.__export_One_databases(one_db_name)

    def Conversion_db_engine(self, Conversion_list=None):
        Conversion_list = [] if Conversion_list is None else Conversion_list  # Conversion is None list
        list_sql_file = os.listdir('.')
        for sql_file in list_sql_file:
            if str(sql_file).endswith(".sql"):
                Conversion_list.append(sql_file)
        for C_Sql_File in Conversion_list:
            self.__Conversion_database_engine(C_Sql_File)

    def Create_Db_path(self):
        """
        创建目录结构
        :return:
        """
        self.__create_Database_db()

    def impotr_db(self):
        """
        导入数据库表数据
        :param table:
        :return:
        """
        self.__import_databases()


HELPER = """
        ## 创建目录结构
        python tran_mysql.py 0        

        ## 全量数据备份
        python tran_mysql.py 1

        ## 单个库备份
        python tran_mysql.py 2

        ## 转换格式
        python tran_mysql.py 3

        ## 数据库导入
        python tran_mysql.py 4
"""

if __name__ == '__main__':
    Mysql_back_dump = Format_conversion()  # 实例化
    print("params:"), sys.argv

    if len(sys.argv) < 2:
        print(HELPER)
    else:
        type = sys.argv[1]
        if type == "0":
            Mysql_back_dump.Create_Db_path()  # 创建目录结构
        elif type == "1":
            Mysql_back_dump.back_All_db()  # 全量备份
        elif type == "2":
            Mysql_back_dump.Export_One_databasename()  # 单个库备份
        elif type == "3":
            Mysql_back_dump.Conversion_db_engine()  # 转换格式
        elif type == "4":
            Mysql_back_dump.impotr_db()  # 数据库导入
        else:
            print(HELPER)
