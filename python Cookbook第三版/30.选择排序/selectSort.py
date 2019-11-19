#找出最大值
#调试标志
flag=input("是否打印调试信息【Y or N】：")
def findBiggest(arr):
    biggest = arr[0]                    #先假设最大值是第一个元素
    biggest_index = 0                   #相应的，最大值的索引是0
    if flag=='Y':
        print("调试信息：biggest=",biggest)
    for i in range(1, len(arr)):        #遍历列表
        if arr[i] > biggest:            #如果第i个元素比假设的最大值还要大
            biggest = arr[i]            #就让第i个元素当最大值
            biggest_index = i           #相应的，最大值的索引就是i
        #调试用：输出每次遍历的最大值对应的索引
        if flag=='Y':
            print("调试信息：第",i,"个元素=",arr[i],"，最大值biggest=",biggest,"，索引为",biggest_index)
    return biggest_index

#选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        biggest_index = findBiggest(arr)
        newArr.append(arr.pop(biggest_index))     #将从列表中弹出的元素添加到新列表末尾
    return newArr
