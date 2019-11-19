#多线程
import threading
import time

class myThread (threading.Thread):  #继承Thread类
    def __init__(self, name, test_arg):
        threading.Thread.__init__(self) #调用父类的初始函数
        self.name = name
        self.test_arg = test_arg
    def run(self):
        print (self.name+"出发啦！\n")
        print_race(self.name, self.test_arg)  #要在线程中执行的函数
        print (self.name+"冲过终点！！！\n")

def print_race(threadName, delay):
    counter=5   #观测5次经过主席台的时间
    while counter:
        time.sleep(delay)       #延迟delay秒
        print("%s经过主席台\n" % (threadName))
        counter -= 1

# 创建新线程
thread1 = myThread("小小",1)   #参数：threadID, name,测试参数(假设为时间延迟)
thread2 = myThread("牛牛",2)
thread3 = myThread("小花",3)

# 开启新线程
thread1.start() #开始线程后，即会调用run()方法
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("比赛结束")
