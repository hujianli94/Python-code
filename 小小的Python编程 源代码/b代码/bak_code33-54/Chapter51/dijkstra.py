#Dijkstra算法
#找到最低开销节点
def find_best_neighbor(costs):
    lowest_cost = float("inf")      #最低开销初始化为正无穷大
    best_neighbor = None                #最低开销节点初始化为None
    for neighbor in costs:              #遍历所有节点
        cost = costs[neighbor]          #取出到节点的开销
        if cost < lowest_cost and neighbor not in processed:#如果当前节点开销更低并且未处理过
            lowest_cost = cost      #就将当前节点开销视为最低开销
            best_neighbor = neighbor     #当前节点视为最低开销节点
    return best_neighbor

#引入加权图graph
from D_graph import graph

#用于记录已处理节点的列表
processed=[]

#起点
infinity=float("inf")
costs={}
costs["别针"]=0
costs["海洋世界门票"]=infinity
costs["限量版海报"]=infinity
costs["滑板车"]=infinity
costs["变形金刚玩具"]=infinity
costs["摩托"]=infinity

#父节点
parents={}

#求最优路径
#def find_best_path(graph,costs):
current_node=find_best_neighbor(costs)    #从开销表中找出最低开销的节点作为当前节点
while current_node is not None:         #如果找不出最低开销节点则结束循环
    cost = costs[current_node]          #到达当前节点的总开销
    neighbors = graph[current_node]     #取出图中最低开销节点的所有邻居（包含开销）
    print("当前节点：",current_node,"，总开销为：",cost)
    for neighbor in neighbors.keys():      #遍历当前节点的所有邻居      
        new_cost = cost + neighbors[neighbor]  #新的开销=当前总开销+此邻居的开销  
        if new_cost < costs[neighbor]:         #如果经当前节点前往邻居的开销更小
            costs[neighbor] = new_cost         #就更新该邻居的开销
            parents[neighbor] = current_node          #同时将当前节点设为该邻居的父节点
    processed.append(current_node)              #将当前节点标记为已处理
    current_node = find_best_neighbor(costs)      #继续处理后续节点
print("最低开销为：",cost)
print(parents)
