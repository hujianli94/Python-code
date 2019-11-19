#2.2printLog2.py
while 1:
    i = int(input('输入购买总价:'))
    if i==0:
        break
    arr = [400,200,100,0]
    rat = [0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,4):      #此行中range(0,3)改为range(0,4)
        #在此处添加一些print语句，输出变量值
#        print('i>arr[idx]吗？i为',i,',arr[idx]为',arr[idx])
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            i=arr[idx]
    print('总优惠金额：',r)
