'''
资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
给定带权无向图，求出一颗最小的生成树。

输入格式
输入多组测试数据。第一行为N,M，依次是点数和边数。接下来M行，每行三个整数U,V,W，代表连接U,V的边，和权值W。保证图连通。n=m=0标志着测试文件的结束。

输出格式
对于每组数据，输出方差，四舍五入到0.01。输出格式按照样例。

样例输入
4 5
1 2 1
2 3 2
3 4 2
4 1 1
2 4 3
4 6
1 2 1
2 3 2
3 4 3
4 1 1
2 4 3
1 3 3
0 0

样例输出
Case 1: 0.22
Case 2: 0.67

数据规模与约定
1<=U,V<=N<=50,N-1<=M<=1000,0<=W<=50。数据不超过5组。
'''
_=float( 'inf ')#正无穷
#负无穷的表示方法:float( '_inf ')

def prim(graph,n):
    dis=[0]*n
    pre=[0]*n
    flag=[False]*n
    flag[0]=True
    k=0
    for i in range(n):
        dis[i]=graph[k][i]
    for j in range(n-1):
        mini=_
        for i in range(n):
            if mini>dis[i] and not flag[i]:
                mini=dis[i]
                k=i
            if k==0:#并不连通
                return
            flag[k] = True
            for i in range(n):
                if dis[i] > graph[k][i] and not flag[i]:
                    dis[i] = graph[k][i]
                    pre[i] = k
        return dis

zu = 0
outpu = [0, 0, 0, 0, 0]  # 存放每个组的结果
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        for i in range(5):# 不超过五组
            if outpu[i] != 0:
                print(outpu[i])
        break
    zu+=1
    #这一段用于初始化graph
    graph = [[_ for i in range(n)] for j in range(n)]
    for j in range(n):
        graph[j][i] = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a - 1][b - 1] = c

    # 由于graph只有一组，所以把结果计算出来存好再接收下一组
    quanzhi= prim(graph,n)#积累当前组的结果
    # print( 'Case %d:%.2f'%(ZU,outp))
    num = str(zu)
    # print(quanzhi)

    #求方差
    junzhi=0
    fangcha=0
    for i in quanzhi:
        junzhi+=i
    junzhi=junzhi/(n-1)
    #print(junzhi)
    for i in quanzhi:
        if i!=0:
            fangcha+=(i-junzhi)**2
            #print(fangcha)
    fangcha=fangcha/(n-1)
    #print(fangcha)
    outpu[zu-1]='Case'+num+':'+'%.2f'% fangcha




