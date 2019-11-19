import math
#特征抽取
aim_film=[2,1,3,2,5]
sample_films_name=['《坏人家族》','《非洲攻略》','《阿龙》']
sample_films=[[1,3,2,4,1],[3,1,2,1,3],[1,2,1,3,4]]

#计算距离
dist_list=[]
min_dist=float('inf')
for row in sample_films:   #遍历其余电影样本
    sum_temp=0      #每行清零
    for i in range(len(row)):   #遍历每一条特征分
        sum_temp+=(aim_film[i]-row[i])**2   #求各项差的平方之和

    dist_list.append(math.sqrt(sum_temp))    #各样本与目标的距离

min_dist=min(dist_list)          #求最小距离
nearest=dist_list.index(min_dist)    #最近邻的下标

print("所有距离：",dist_list)
print("最小距离为：",min_dist)
print("最接近的电影为：",sample_films_name[nearest])
