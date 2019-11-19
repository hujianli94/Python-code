#选择和冒泡两种排序时间比较
import selectSort,bubbleSort,time
#产生一个大列表
arr1=bubbleSort.arrMaker(0,50000,10000)
arr2=arr1.copy()

#冒泡排序
print("-------------------冒泡排序-------------------")
print("排序前(开头和末尾5个元素)：",arr1[0:5],"...",arr1[-5:])
start=time.time()
arr=bubbleSort.bubbleSort(arr1)
print("-------------------排序结束-------------------")
print("排序后(开头和末尾5个元素)：",arr1[0:5],"...",arr1[-5:])
print("本次排序耗时：",time.time()-start,"秒")

print()
#选择排序
print("-------------------选择排序-------------------")
print("排序前(开头和末尾5个元素)：",arr2[0:5],"...",arr2[-5:])
start=time.time()
arr=selectSort.selectionSort(arr2)
print("-------------------排序结束-------------------")
print("排序后(开头和末尾5个元素)：",arr2[0:5],"...",arr2[-5:])
print("本次排序耗时：",time.time()-start,"秒")

