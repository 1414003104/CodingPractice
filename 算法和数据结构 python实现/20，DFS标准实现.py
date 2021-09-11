graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def DFS(graph,s):#s是第一个开始的节点
    queue=[]
    queue.append(s)#先放进去s
    seen=set()#用于判断已经访问过哪些节点,这里注意区分集合和字典的区别
    seen.add(s)#往字典里面添加一个元素
    while(len(queue)>0):
        vertex=queue.pop()#弹出改元素，并返回该元素的值
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

DFS(graph,"E")