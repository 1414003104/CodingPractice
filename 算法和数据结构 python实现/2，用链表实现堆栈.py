# 类中的方法和属性。
# 方法：也就是各类中定义的函数，比如我们定义一个车的类，描述车的函数就是一个方法。
# 属性：车的品牌、型号、生产日期等信息就是它的属性
'''
init”的全称是“initialize”，也就是初始化的意思，所以__init__又称构造方法。
在定义类的时候__init__()方法是必不可少的。
init()这种初始化方法，用来初始化新创建对象的属性，在一个对象被创建以后会立即调用，比如像实例化一个类：
class Car():
    def __init__(self,make,model,year):    ###
        self.make = make
        self.model = model
        self.year = year
my_car = Car('aodi','A4','2010')
print(my_car.model)
————————————————
'''
class Node:
    def __init__(self):
        self.data=0#堆栈数据的声明
        self.next=None#堆栈中

top=None

def isEmpty():
    global top
    if(top==None):
        return 1
    else:
        return 0

#将指定的数据压入堆栈
def push(data):
    global top
    new_add_node=Node()
    new_add_node.data=data#将传入的值指定为节点的内容
    new_add_node.next=top#将新节点指向堆栈的顶端
    top=new_add_node#新节点成为堆栈的顶端
#从堆栈中弹出数据
def pop():
    global top
    if isEmpty():
        print("当前为空栈")
        return -1
    else:
        ptr=top#指向堆栈的顶端
        top=top.next#将堆栈顶端的指针指向下一个节点
        temp=ptr.data#弹出堆栈的数据
        return temp

push(10)
push(20)
pop()
push(30)
print(top.data)
print(top.next)
print(top.next.data)