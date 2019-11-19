import math
# 判断数字是否为素数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#验证大于2的偶数可以分解为两个质数之和
def goldbach(T):
# T为列表，第一个元素为区间起点，第二个元素为区间终点
    S = T[0]
    E = T[1]
    sample=[]   #用于返回样例
    if S < 4:   #若不是大于2的偶数
        S = 4   #设为大于2的最小偶数
    if S % 2 == 1:      #除2余数为1的是奇数
        S += 1          #奇数+1为偶数
    for i in range(S, E + 1, 2):    #遍历区间内所有偶数
        isGoldbach = False
        for j in range(i // 2 + 1): # 表示成两个素数的和,其中一个不大于1/2
            if isPrime(j):
                k = i - j
                if isPrime(k):
                    isGoldbach = True
                    if i % 100000 == 0:  # 每隔10万输出样例
                        sample.append((i,j,k))
                    break
        if not isGoldbach:
            #如果打印这句话表示算法失败或欧拉错了
            sample.append('哥德巴赫猜想失败！')
            break
    return sample



