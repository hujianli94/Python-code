while 1:
    i = int(input('输入购买总价:'))
    if i==0:
        break
    arr = [400,200,100,0]
    rat = [0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,3):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print((i-arr[idx])*rat[idx])    #print变量值进行调试
            i=arr[idx]
    print('总优惠金额：',r)
