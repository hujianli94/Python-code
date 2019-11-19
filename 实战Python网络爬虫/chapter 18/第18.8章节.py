# 导入concurrent.futures模块
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import datetime

# 线程的执行方法
def print_value(value):
    print('Thread' + str(value))

# 每个进程里面的线程
def myThread(value):
    Thread = ThreadPoolExecutor(max_workers=2)
    Thread.submit(print_value, datetime.datetime.now())
    Thread.submit(print_value, datetime.datetime.now())

# 创建两个进程，每个进程执行myThread方法，myThread主要将每个进程通过线程执行
# 如果不填写max_workers=2，会根据计算机的每一个CPU创建一个Python进程，如果四核就创建四个进程
def myProcess():
    pool = ProcessPoolExecutor(max_workers=2)
    pool.submit(myThread, datetime.datetime.now())
    pool.submit(myThread, datetime.datetime.now())

if __name__ == '__main__':
    myProcess()