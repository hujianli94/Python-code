#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/17 9:13
# filename: 01.系统性能信息模块.py
import psutil

############################# 内存的使用
M = 1024 * 1024 * 1024
mem = psutil.virtual_memory()
Swap = psutil.swap_memory()
print("物理内存Total值为：【{}】,\n物理内存Used值为：【{}】\n空闲内存数为:【{}】".format(str(round(mem.total / M)) + "G",
                                                               str(mem.used / M) + "G", str(round(mem.free / M)) + "G"))
print("SWAP分区信息为：【{}】".format(Swap))

print()
############################ 获取CPU的完整信息
print(psutil.cpu_times())
# 获取单项数据，user的CPU时间比
print(psutil.cpu_times().user)
# 获取CPU的逻辑个数
print(psutil.cpu_count())
# 获取CPU的物理个数
print(psutil.cpu_count(logical=False))

############################ 获取磁盘信息
print()
# 获取磁盘的完整信息
print(psutil.disk_partitions())
# 获取分区的使用情况
print(psutil.disk_usage("C:\\"))
# 获取硬盘总的IO个数、读写信息
print(psutil.disk_io_counters())
print()
# 获取单个分区的IO个数、读写信息
print(psutil.disk_io_counters(perdisk=True))

print()
############################ 网络信息
# 获取网络总的IO信息，默认pernic=False
print(psutil.net_io_counters())
print()
# 输出每个网络接口的IO信息
print(psutil.net_io_counters(pernic=True))
all_Net = psutil.net_io_counters(pernic=True)
print()
for name, values in all_Net.items():
    print("网卡名称：【{}】，流量值：【{}】".format(name, values))

print()
############################ 其他系统信息
# 返回当前登录系统的用户信息
print(psutil.users())

# 获取开机时间转，以Linux的时间戳格式返回
print(psutil.boot_time())

# 转换格式为自然时间格式
import datetime

init_date = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print("系统开机时间为：【{}】".format(init_date))
print()


######################### 系统进程管理方法
# 列出所有进程PID
All_PID = psutil.pids()
print(All_PID)

# 实例化Process对象，参数为一进程PID
p = psutil.Process(13092)
# 进程名称
print(p.name())
# 进程bin路径
print(p.exe())
# 进程工作目录绝对路径
print(p.cwd())
# 进程状态
print(p.status())
# 进程创建时间，时间戳格式
print(p.create_time())
# 进程uid新的
# print(p.uids())
# 进程gid新的
# print(p.gids())
# 进程CPU时间信息，包括user、system两个CPU时间
print(p.cpu_times())

# 进程CPU亲和度
print(p.cpu_affinity())

# 进程内存利用率
print(p.memory_percent())

# 进程内存rss、vms信息
print(p.memory_info())

#进程IO信息，包括读写IO数及字节数
print(p.io_counters())

# 返回打开进程socket的namedutples列表
print(p.connections())

# 进程开启的线程数
print(p.num_threads())