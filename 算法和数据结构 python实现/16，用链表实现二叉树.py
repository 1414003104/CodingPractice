'''
用链表表示二叉树的好处在于便于删除、添加
但是很难找到父节点
除非在每一节点多增加一个父字段
'''
class tree:
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None

def create_tree(root,val):#建立二叉树的函数,val是要添加的值,root是根指针
    newnode=tree()
    newnode.data=val
    newnode.left=None
    newnode.right=None
    if root==None:#先判断是否有根节点，没有就指向这个节点作为根
        root=newnode
        return root
    else:
        current=root#如果有根节点了，current指针指向根节点
        while current!=None:
            backup=current
            if current.data>val:#如果current指针指向的位置的数据大于要填的数据，则current指向current.left比根小的数填他的左子树
                current=current.left
            else:
                current=current.right
        if backup.data>val:#backup存储的没有改变指向时候的current指针的指向
            backup.left=newnode
        else:
            backup.right=newnode
    return root

def traverse_front(ptr):#中序遍历，前序遍历和中序遍历差不多
    if ptr!=None:
        traverse_front(ptr.left)
        print(ptr.data,end=' ')
        traverse_front(ptr.right)

data=[5,6,24,8,12,3,17,1,9]
#print(data)
ptr=None
root=None
for i in range(9):
    ptr=create_tree(ptr,data[i])
#print(ptr.left.data)
traverse_front(ptr)