#坏处是不能随意变动堆栈本身的大小
#例：设计一个大小可以容纳100个元素的堆栈，其中必须包括压入（push)与弹出（pop)函数，并在最后输出堆栈内所有的元素
max_stack=100
global stack
stack=[None for i in range(max_stack)]
#print(stack)
top=-1#因为top取0的时候，代表列表里存在一个元素，并不为空

def is_Empty():
    if top==-1:
        return True
    else:
        return False

def push(data):
    global top
    global stack
    global max_stack
    if top>=max_stack-1:
        print("堆栈已满")
    else:
        top+=1
        stack[top]=data

def pop():
    global top
    global stack
    if is_Empty():
        print("堆栈为空")
    else:
        print("弹出的元素为%d"%stack[top])
        top-=1

push(100)
push(99)
print(stack)
pop()
push(88)
print(stack)