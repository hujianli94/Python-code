#蒙特卡罗法求π
from random import random
from time import perf_counter
from math import sqrt

Points=int(input("输入点数n（点越多结果越准确，计算时间也越长）："))
cnt = 0     #统计圆内的点数

#开始计时
start = perf_counter()  #perf_counter()返回计时器的精准时间
print("计算中，请稍候...")
for i in range(Points):
    x, y = random(), random()   #随机生成一个点，坐标均在[0,1)范围内
    #检查点是否落在1/4单位圆范围内
    dis = sqrt(x ** 2 +y ** 2)    #点到圆心的距离
    if dis <= 1.0:  #如果小于半径则点落在1/4圆内
        cnt += 1    #增加统计数

#计算π
pi = 4*cnt/Points   #点数比=pi:4
print("{:.6f}".format(pi))  #输出6位小数
print("运行时间是: {:.6f}秒".format(perf_counter() - start))  #计算运行时间
