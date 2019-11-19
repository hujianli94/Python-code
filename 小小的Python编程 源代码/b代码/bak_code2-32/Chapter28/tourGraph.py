#图的表示
tourGraph={}
tourGraph['家']=['1','2']
tourGraph['1']=['4']
tourGraph['2']=['3','5']
tourGraph['3']=['4']
tourGraph['4']=['开心森林']
tourGraph['5']=['4']
tourGraph['开心森林']=[]

#图的示例
n_graph={}
n_graph[0]=[1,2]
n_graph[1]=[3,5]
n_graph[2]=[7,4]
n_graph[4]=[6,8]
n_graph[3]=[5,6,7]
n_graph[5]=[8,10,9]
n_graph[6]=[5]
n_graph[7]=[10]
n_graph[8]=[9]
n_graph[9]=[]
n_graph[10]=[9]

from BFS import BFS
BFS(0,9,n_graph)
