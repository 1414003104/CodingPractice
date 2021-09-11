#创建一个长度为100的队列
Max_size=100
queue=[0 for i in range(Max_size)]
front=-1#队头，初值为-1
rear=-1#队尾，同-1，这样队列里面就没有任何值

#队列包含插入、删除两种操作
def insert_queue(temp):
    global Max_size#函数内操控函数外的变量
    global rear
    global queue
    if rear==Max_size-1:
        print("队列已满")
    else:
        rear+=1
        queue[rear]=temp#队尾+1,存入数据

def out_queue():
    global Max_size
    global front
    global queue
    if front==rear:
        print("队列为空")
    else:
        front+=1
        #temp = queue[front]#temp是有数据出队之后的队头
        print(queue[front])

insert_queue(5)
insert_queue(7)
out_queue()
out_queue()
#out_queue()
print(queue)
