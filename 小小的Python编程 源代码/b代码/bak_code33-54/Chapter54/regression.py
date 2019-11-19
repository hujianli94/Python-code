#引入knn算法
from knn_simple import knn

#回归计算
def regression(knn_value):
    """knn回归计算，knn_value为k最近邻对应的样本值"""
    return sum(knn_value)/len(knn_value)    

#目标特征值
aim=[1,4,5,'r']     #'r'表示待求的值
#样本特征值及样本值
sample=[[1,5,2,280],
        [1,1,1,20],
        [1,3,2,210],
        [0,4,4,360],
        [1,5,3,320],
        [0,3,0,50],
        [1,2,1,170],
        [0,3,2,150],
        [0,1,1,60],
        [1,0,0,10],
        [1,3,5,310],
        [0,5,3,205]]

nn=knn(sample,aim,5)
print('最近的5个距离：',nn[0])
print('最近的5个距离对应的样本值：',nn[1])
print('回归值：',regression(nn[1]))
