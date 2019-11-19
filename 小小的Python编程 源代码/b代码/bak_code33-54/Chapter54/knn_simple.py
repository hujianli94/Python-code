import math

#找出最小值
def findSmallest(arr):
    smallest = arr[0]                    #先假设最小值是第一个元素
    smallest_index = 0                   #相应的，最小值的索引是0
    for i in range(1, len(arr)):        #遍历列表，从第2个元素开始
        if arr[i] < smallest:            #如果第i个元素比假设的最小值还要小
            smallest = arr[i]            #就让第i个元素当最小值
            smallest_index = i           #相应的，最小值的索引就是i
    return smallest_index

#计算距离
def knn(sample,aim,k):
    """返回k个aim的最近邻sample"""
    dist_list=[]                #距离列表
    sample_value_list=[]         #距离对应的样本值
    min_dist=float('inf')       #最小距离初始化
    for row in sample:   #遍历样本
        #print(row)
        #求样本与目标的距离
        sum_temp=0      #每行距离初始化
        for i in range(len(aim)-1):               #遍历样本每一条特征值
            sum_temp+=(aim[i]-row[i])**2   #求各项差的平方之和
            dist=math.sqrt(sum_temp)    #样本与目标的距离
        dist_list.append(dist)          #每个样本的距离添加到列表
        sample_value_list.append(row[len(aim)-1])    #每个距离对应的样本值

    #求k个最近邻
    knn_value_list=[]   #用于存放k个最近邻对应的样本值
    knn_dist_list=[]
    for j in range(len(dist_list)):
        smallest_index=findSmallest(dist_list)
        if k>0:
            #将从sample_value_list中弹出的对应元素添加到knn_value_list中
            knn_value_list.append(sample_value_list.pop(smallest_index))
            knn_dist_list.append(dist_list.pop(smallest_index))
            k-=1
    return [knn_dist_list,knn_value_list]        #返回k个最近邻的距离和样本值

