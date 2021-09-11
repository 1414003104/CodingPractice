'''
n 皇后问题

在n×n格的棋盘上放置彼此不受攻击的n个皇后。
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
即n后问题等价于再n×n的棋盘上放置n个皇后，任何2个皇后不妨在同一行或同一列或同一斜线上。

输入 n, 返回解法的个数
'''
#因为皇后没法同行，所以这里可以取巧用个一维数组存储坐标，下标代表行数，所存储的为列数
#row是行数，即下标

res=[]
def n_queue(n):
    one_res = [-100]*n#存放解, rec[i]表示第i行的皇后放在第rec[i]上
    dfs(one_res,0)#从第0行开始
    print(res)

def dfs(one_res,x):#x表示从哪行开始
    if x>=len(one_res):
        one_res_cp=one_res.copy()
        res.append(one_res_cp)
        return

    for y in range(len(one_res)):#对每一行的每一列进行试探
        if check(one_res,x,y):
            one_res[x]=y#如果可以，存储该位置
            dfs(one_res,x+1)#继续存下一行
    one_res[x]=-100#如果都不可以，则还原为-100

def check(one_res,x,y):#判断这个点能否放进去
    for i in range(len(one_res)):
        if i==x:#判断是否同行#感觉都不用判断，因为x一直在递增
            continue#continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
        if one_res[i]==y:#列
            return False
        if one_res[i]-i==y-x:#主对角线
            return False
        if i+one_res[i]==x+y:#副对角线
            return False
    return True

n_queue(4)








