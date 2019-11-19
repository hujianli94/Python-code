#线程锁定与解锁
import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print ("开启线程： " + self.name+"出发\n")
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_turbo(self.name, self.delay)
        # 释放锁，才能开启下一个线程
        threadLock.release()
        print(self.name+"冲过终点！！！")

def print_turbo(threadName, delay):
    counter=3
    while counter:
        time.sleep(delay)
        print ("%s发射: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread("小小", 2)
thread2 = myThread("牛牛", 1)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
