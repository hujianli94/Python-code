#物品列表
crystal=['紫水晶','红宝石']
soul=['传说灵魂','普通灵魂','高级灵魂']
legend=['牛牛的水果刀','小花的指甲钳']
item=[legend,crystal,soul]
print("晶体：",crystal)
print("灵魂：",soul)
print("传奇：",legend)
print("所有物品：",item)

#输入新的物品
newcrystal=input('新的晶体：')
#添加新的物品到相应列表中
crystal.append(newcrystal)
newlegend=input('新的传奇：')
legend.append(newlegend)
print("所有物品：",item)

