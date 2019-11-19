#多进程验证哥德巴赫猜想
import time
from  multiprocessing import cpu_count
from multiprocessing import Pool
from Goldbach import goldbach

#把数字空间N分段，分段数为内核数
def subRanges(N, CPU_COUNT):
    list = [[i + 1, i + N // CPU_COUNT] for i in range(4, N, N // CPU_COUNT)]
    list[0][0] = 4
    if list[CPU_COUNT - 1][1] > N:
        list[CPU_COUNT - 1][1] = N
    return list

def main():
    N = 10**6       #根据电脑性能调整
    CPU_COUNT = cpu_count()  #获取CPU内核数

    #单进程测试
    print("单进程")
    start = time.clock()
    results=goldbach([4, N])    #4-N区间内执行goldbach
    for sample in results:
        print('%d=%d+%d' % sample)
    print('单进程耗时:%d s' % (time.clock() - start))

    #多进程测试
    print("多进程")    
    pool = Pool(CPU_COUNT)   #建立进程池，进程数等于CPU内核数
    sepList = subRanges(N, CPU_COUNT)   #将数N按内核数分割
    start = time.clock()
    results=pool.map(goldbach, sepList)    #并行迭代goldbach函数
    pool.close()    #关闭进程池
    pool.join()     #等待所有进程结束

    for result in results:
        for sample in result:
            print('%d=%d+%d' % sample)
    print('多进程耗时:%d s' % (time.clock() - start))

if __name__ == '__main__':
    main()


