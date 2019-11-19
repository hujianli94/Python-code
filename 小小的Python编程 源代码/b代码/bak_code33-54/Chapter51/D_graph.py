#物品交换图
graph={} 	  #有向加权图是一个字典
#起点“别针”
graph["别针"]={}  #节点“别针”也是一个字典
graph["别针"]["限量版海报"]=5       #“别针”的一个邻居，开销为5
graph["别针"]["海洋世界门票"]=0     #别针的另一个邻居，开销为0

#其余节点
graph["限量版海报"]={}
graph["限量版海报"]["滑板车"]=15
graph["限量版海报"]["变形金刚玩具"]=20

graph["海洋世界门票"]={}
graph["海洋世界门票"]["滑板车"]=30
graph["海洋世界门票"]["变形金刚玩具"]=35

graph["变形金刚玩具"]={}
graph["变形金刚玩具"]["摩托"]=275

graph["滑板车"]={}
graph["滑板车"]["摩托"]=200

graph["摩托"]={}      #终点节点，没有任何邻居
