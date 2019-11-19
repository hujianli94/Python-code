#随机数应用示例2
import random
#蛋糕店的菜单
menu=('黑森林蛋糕','布朗尼蛋糕','舒芙里','提拉米苏','瑞士卷','海绵蛋糕','水果大理石蛋糕','咖啡酸奶核桃蛋糕','卡士达抹茶蛋糕');
print("全部蛋糕：",menu)
#要免费的两种蛋糕
freeCake=random.sample(menu,2)
print("今天的免费品种是：",freeCake)
