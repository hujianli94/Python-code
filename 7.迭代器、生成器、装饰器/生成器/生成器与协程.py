#!/usr/bin/env python
# -*- coding:utf8 -*-

import time

cake = "🍰"


# 一个简单的生产者与消费者编程模型

def consumer():
    print("等待接收处理任务.......")
    while True:
        data = (yield)
        print("收到 {0}，开始品尝 【{1}】：".format(data, cake))
        time.sleep(0.5)
        print("蛋糕被吃完了........哈哈哈哈哈嗝")
        print()


def producer():
    c = consumer()
    c.__next__()
    print("模拟生产者模型")
    for i in range(1, 5):
        time.sleep(1)
        print("开始制作第{0}个蛋糕, 【{1}】【{2}】做好了.....".format(i, cake, i))
        c.send("蛋糕:【%s】" % i)


if __name__ == '__main__':
    producer()
