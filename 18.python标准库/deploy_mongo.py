#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/19 22:08
# filename: deploy_mongo.py
import os
import shutil
import tarfile
import subprocess


def execute_cmd(cmd):
    """ 将执行shell命令封装成execute_cmd函数，使用时直接调用即可 """
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def unpackage_mongo(package, package_dir):
    # 分割路径和文件名组成元祖，获取mongodb安装包解压以后的目录，如果目录存在，则删除该目录。
    unpackage_dir = os.path.splitext(package)[0]
    if os.path.exists(unpackage_dir):
        shutil.rmtree(unpackage_dir)
    # 解压目录后，重命名为mongo目录
    t = tarfile.open(package, 'r:gz')
    t.extractall(".")

    shutil.move(unpackage_dir, package_dir)


def create_datadir(data_dir):
    ''' 检测MongoDB目录是否存在,存在删除，不存在直接创建 '''
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.mkdir(data_dir)


def format_mongod_command(package_dir, data_dir, logfile):
    mongod = os.path.join(package_dir, "bin", "mongod")
    mongod_format = """{0} --fork --dbpath {1} --logpath {2}"""
    return mongod_format.format(mongod, data_dir, logfile)


def start_mongod(cmd):
    # 获取shell命令执行状态码和输出信息。
    returncode, out = execute_cmd(cmd)
    if returncode != 0:
        raise SystemExit("execute {0} error:{1}".format(cmd, out))
    else:
        print("execute command ({0}) successful".format(cmd))


def main():
    package = "mongodb-linux-x86_64-debian71-3.4.0.tgz"
    cur_dir = os.path.abspath(".")
    package_dir = os.path.join(cur_dir, "mongo")
    data_dir = os.path.join(cur_dir, "mongodata")
    logfile = os.path.join(cur_dir, "mongod.log")

    if not os.path.exists(package):
        raise SystemExit("{0} not found".format(package))

    # 解压安装包，并移动目录
    unpackage_mongo(package, package_dir)
    # 创建目标目录
    create_datadir(data_dir)
    # 启动服务
    start_mongod(format_mongod_command(package_dir, data_dir, logfile))


if __name__ == '__main__':
    main()
