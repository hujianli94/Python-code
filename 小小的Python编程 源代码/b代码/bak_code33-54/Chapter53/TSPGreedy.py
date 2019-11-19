#城市
cities={0:'莫斯科',1:'巴黎',2:'柏林',3:'华盛顿',4:'温哥华'}

#距离表
LONG=100    #用于表达很长的时间
#各城市之间的距离，用飞行时间表示：D[i][j]表示从i到j的飞行时间，本地距离设为LONG
D=[[LONG,4,3,4,15],
   [3.5,LONG,3.5,8.5,10],
   [2.5,2,LONG,12,14],
   [9.5,7.5,13,LONG,8.5],
   [19,12,13.5,8,LONG]]

#选择出发城市
for k in cities.keys():
    print(k,cities[k])
start=int(input("请选择出发城市："))
print('从',cities[start],'出发')

#初始化
currentMinDistance=LONG     #当前行内最小值
currentBestCityId=start     #当前最优城市id
sumDistance=0       #当前累计距离
bestCityId=[start,] #当前入选城市id

#从起点开始遍历所有城市
for i in range(len(cities)-1):       #遍历行
    #print('------------------------------------------------------当前行',currentBestCityId)
    currentMinDistance=LONG
    for col in cities.keys():   #每行内遍历列
        if col not in bestCityId:     #如果城市col还未入选，则
            #print("当前列",col,D[currentBestCityId][col])
            if D[currentBestCityId][col]<currentMinDistance:    #比较：如果某距离比当前最小距离更小
                currentMinDistance=D[currentBestCityId][col]    #则更新当前最小距离
                nextBestCityId=col
                #print('currentMinDistance',currentMinDistance)
    currentBestCityId=nextBestCityId               #更新当前最优城市
    sumDistance+=currentMinDistance     #累计时间
        
    bestCityId.append(currentBestCityId)        #一行比较完后添加最优城市

#输出路径
for i in bestCityId:
    print(cities[i],end='->')
print('共需',sumDistance,'小时')

input()         #屏幕暂停，用于cmd界面运行时
            
    

