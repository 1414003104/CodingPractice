graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def BFS(graph,s):#s是第一个开始的节点
    queue=[]
    queue.append(s)#先放进去s
    #print(queue)
    seen=set()#用于判断已经访问过哪些节点,这里注意区分集合和字典的区别
    seen.add(s)#往集合里面添加一个元素
    #print(seen)
    parent={s:None}
    while(len(queue)>0):
        vertex=queue.pop(0)#弹出改元素，并返回该元素的值
        nodes=graph[vertex]#比如vertex是B,nodes里面就是A、C、D
        #print(nodes)
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w]=vertex
        print(vertex)
    return parent

parent=BFS(graph,"B")
print(parent)