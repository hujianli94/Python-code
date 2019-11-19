#break、continue、pass示例
for n in range(100):
    print("第",n+1,"次：")
    
    if (n+1)%5==0:
        print("你问了",n+1,"遍了，老狼该休息了！")
        y=input("姑奶奶，您还玩吗？（选Y继续，选N发呆，选其他退出）")
        if y=='Y' or y=='y':
            continue
        elif y=='N' or y=='n':
            print("开始发呆，按Ctrl+C退出")
            while 1:
                pass
        else:
            break
        
    x=int(input("老狼老狼几点了？"))
    if x==12:
        print("老狼来抓你啦！！！快跑吧！！！")
    
print("游戏结束。")
        
