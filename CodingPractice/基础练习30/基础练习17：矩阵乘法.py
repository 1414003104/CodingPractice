'''
问题描述
　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2
　　3 4
　　A的2次幂
　　7 10
　　15 22
输入格式
　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
输出格式
　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开
样例输入
2 2
1 2
3 4
样例输出
7 10
15 22
'''
# n = 阶数， m = 幂数
n, m = input().split()
# 将输入的矩阵写入
start = []
for i in range(int(n)):
    start.append(input().split())

# 生成“竖排列表”
def vertical(e):
    o = []
    for j in range(int(n)):
        l = []
        for k in e:
            l.append(k[j])
        o.append(l)
    return o

def matrix_multi(x, y):
    q = []
    for i in x:
        p = []
        for j in y:
            a = 0
            for u in range(int(n)):
                a = a + int(i[u]) * int(j[u])
            p.append(a)
        q.append(p)
    return q

# 自定义输出
def _print(end_list):
    for i in end_list:
        for j in i:
            print(int(j), end=' ')
        print()
# 幂运算，递归形式
def mi(xx, num):
    q2 = matrix_multi(xx, o2)
    if num == 2:
        _print(q2)
    else:
        mi(q2, num - 1)
# 程序的开始
#幂为0时，为单位矩阵E
if m == '0':
    EE = []
    for ii in range(int(n)):
        E = []
        for jj in range(int(n)):
            if not jj == ii:
                E.insert(jj, 0)
            else:
                E.insert(jj, 1)
        EE.append(E)
    _print(EE)
elif m == '1':
    _print(start)
else:
    o2 = vertical(start)
    mi(start, int(m))
