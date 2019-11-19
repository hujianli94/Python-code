#随机数应用示例3
import random
#蛋糕店的菜单
menu=('黑森林蛋糕','布朗尼蛋糕','舒芙里','提拉米苏','瑞士卷','海绵蛋糕','水果大理石蛋糕','咖啡酸奶核桃蛋糕','卡士达抹茶蛋糕');
print("全部",len(menu),"款蛋糕：",menu)
#元组转换成列表
menuList=list(menu)
#打乱菜单中蛋糕的顺序，再由顾客抽号
random.shuffle(menuList)
sel=int(input("请抽取免费蛋糕（0-9）"))
print("从【",menuList,"】中产生的第一款免费蛋糕是：【",menuList[sel],"】")
random.shuffle(menuList)
sel=int(input("请抽取免费蛋糕（0-9）"))
print("从【",menuList,"】中产生的第二款免费蛋糕是：【",menuList[sel],"】")
