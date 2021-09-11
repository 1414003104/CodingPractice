'''
输入正整数n,对1-n进行排列, 使得相
输出时从整数1开始,逆时针排列,同一个环应该恰好输出1次邻两个数之和均为质数
n<=16

如输入:6
输出:
1 4 3 2 5 6
1 6 5 2 3 4
'''
def is_pal(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def can_c_num(n,rec,cur,temp):#temp为当前要填的数
    #已经取过的数不能取
    for i in range(cur):
        if temp==rec[i]:
            return False
    #cur和左边以及右边的数的和必须为质数
    #先判断右边的数填没填，如果填了就不用计算右边的和
    if rec[(cur+1)%n]!=0:
        num_l_sum=rec[cur-1]+temp
        num_r_sum=temp+rec[(cur+1)%n]#这样写取巧的地方在于取到n-1的时候，右边就是0,解决了边界问题
        return is_pal(num_l_sum) and is_pal(num_r_sum)#两个都为素数的时候才成立
    else:
        num_l_sum1=rec[cur-1]+temp
        return is_pal(num_l_sum1)

def circle_zhishu(n,rec,cur):
    #出口
    if cur==n:
        print(rec)
        return
    #试探的数，状态转移,因为从1开始，所以这里从2开始考察
    for temp in range(2,n+1):
        if can_c_num(n,rec,cur,temp):
            rec[cur]=temp
            circle_zhishu(n,rec,cur+1)
    #如果都填不了，重置为0，返回上一层
    rec[cur]=0

N=int(input())
rec=[0 for i in range(N)]
rec[0]=1
circle_zhishu(N,rec,1)#下标为0的值固定为1，所以从下标1开始


