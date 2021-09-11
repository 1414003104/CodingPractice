'''
有一个大小为N×M的园子，雨后积起了水。

其中: 1代表有水, 0代表没水

八连通的积水被认为是连通在一起的。请求出园子里总共有多少水洼？（八连通指的是下图中相对w的*部分）

***
*W*
***

例如某园子如图:

100000000110
011100000111
000011000110
000000000110
000000000100
001000000100
010100000110
101010000010
010100000010
001000000010

输出3
'''
#把1变0，直到整个列表里面的数全部为0
#边界的时候会报错
def water_num(arr):
    count=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==1:
                tra_water(arr,i,j)#每遍历完一个水坑就加1
                count+=1
    print(count)

def tra_water(arr,i,j):#判断每个位置的四周是否有1，这里千万别用else-if 而是每个位置都判断8次不同位置
    arr[i][j]=0
    if arr[i-1][j]==1:
        tra_water(arr,i-1,j)
    if arr[i+1][j]==1:
        tra_water(arr,i+1,j)
    if arr[i][j-1]==1:
        tra_water(arr,i,j-1)
    if arr[i][j+1]==1:
        tra_water(arr,i,j+1)
    if arr[i-1][j-1]==1:
        tra_water(arr,i-1,j-1)
    if arr[i+1][j-1]==1:
        tra_water(arr,i+1,j-1)
    if arr[i+1][j+1]==1:
        tra_water(arr,i+1,j+1)
    if arr[i-1][j+1]==1:
        tra_water(arr,i-1,j+1)
    return

def add_num(arr):#在原矩阵外增加一圈0，消除边界问题
    a=len(arr)#行数
    b=len(arr[0])#列数
    New_L=[[0 for i in range(b+2)] for j in range(a+2)]
    for i in range(0,a):
        for j in range(0,b):
            New_L[i+1][j+1]=arr[i][j]
    return New_L


New_List=[
    [1,0,0,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,0,0,0,0,0,1,1,1],
    [0,0,0,0,1,1,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,1,0,0],
    [0,1,0,1,0,0,1,0,0,1,1,0],
    [1,0,1,0,1,0,0,1,0,0,1,0],
    [0,1,0,1,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,1,0]
]
New_List1=[
    [1,0,1,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,1,1]
]
water_num(add_num(New_List))



