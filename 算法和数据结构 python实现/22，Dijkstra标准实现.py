'''
这里用到了python自带的heapq模块，小顶堆
'''
import heapq
import math

graph={
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
}

def init_distance(graph,s):#除了第一个点的距离为0以外，其余所有的点的距离都被重置为正无穷
    distance={s:0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex]=math.inf
    return distance

# print(graph["A"])#查看与A相连的节点和距离
# print(list(graph["A"].keys()))
# print(graph["A"]["B"])
# print(graph["C"]["D"])#C到D的距离

def dijkstra(graph,s):#s是第一个开始的节点
    pqueue=[]
    heapq.heappush(pqueue,(0,s))#s距离s的距离为0
    seen=set()#用于判断已经访问过哪些节点,这里注意区分集合和字典的区别
    #seen.add(s)#往集合里面添加一个元素
    parent={s:None}
    distance=init_distance(graph,s)

    while(len(pqueue)>0):
        pair=heapq.heappop(pqueue)#这里拿到的是一对数据：点和距离
        dist=pair[0]
        vertex=pair[1]
        seen.add(vertex)#要拿出来之后才算这个点被看到

        nodes=graph[vertex].keys()#因为这里是字典内嵌字典，所以需要用keys()取到键值
        for w in nodes:
            if w not in seen:
                if dist+graph[vertex][w]<distance[w]:#vertex代表点S的点，w是与点S相连的点
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w]=vertex
                    distance[w]=dist+graph[vertex][w]
    return parent,distance

parent,distance=dijkstra(graph,"A")
print(parent)
print(distance)