#冒泡排序
showDebug=int(input("打印调试信息吗？【1】是；【0】否："))
def bubbleSort(arr):
    """冒泡排序"""
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j] < arr[j + 1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if showDebug==1:print("(调试信息)第",i+1,"轮：",arr)
    return arr

#列表构造器
def arrMaker(a,b,qty):
    """产生qty个[a,b)之间的整数"""
    import random
    arr=[]
    for i in range(qty):
        arr.append(random.randint(a,b))
    return arr

#改良的冒泡排序
def bubbleSortPlus(arr):
    s=1                                         #设置状态标志s
    for i in range(len(arr)-1):
        if s==1:                            #s==1时执行后续排序操作
            s = 0       #如果一轮循环中s没有改变，s=0状态持续到下一轮
            for j in range(len(arr)-1-i):
                if(arr[j] < arr[j + 1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    s = 1       #只要还存在一次交换，s就重被置为1 
            if showDebug==1:print("(调试信息)第",i+1,"轮：",arr)
        else:
            break       #s=0时结束排序
    return arr 




