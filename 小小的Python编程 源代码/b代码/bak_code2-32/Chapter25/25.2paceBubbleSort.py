#调用bubbleSort函数
import bubbleSort,time
arr1=bubbleSort.arrMaker(0,50000,5000)
print("排序前(开头和末尾5个元素)：",arr1[0:5],"...",arr1[-5:])
print("-------------------冒泡排序-------------------")
start=time.time()
arr=bubbleSort.bubbleSort(arr1)
print("-------------------排序结束-------------------")
print("排序后(开头和末尾5个元素)：",arr1[0:5],"...",arr1[-5:])
print("本次排序耗时：",time.time()-start,"秒")

