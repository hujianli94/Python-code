#广度优先搜索
def BFS(start_point,end_point,graph):
    from collections import deque

    search_queue = deque()          #创建空队列，用于存放待搜索的节点
    visited=[]                      #记录访问过的节点
    search_queue+=[start_point]     #向搜索队列中添加起点
    layer=0                         #

    print("开始搜索：")
    while search_queue:  #只要没有搜索完全部节点，队列就不会空
        print("(当前搜索队列：",search_queue,")")
        current_node = search_queue.popleft()#取出队前节点
        if not current_node in visited:
            print(current_node,end=" | ")
            if current_node==end_point:
                break
            else:
                visited.append(current_node)
                search_queue+=graph[current_node]
    print("搜索完毕。")

#记录路径
