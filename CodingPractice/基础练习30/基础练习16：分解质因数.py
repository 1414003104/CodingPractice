'''
问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)(具体可看样例)
样例输入
3 10
样例输出
3=3
4=2*2
5=5
6=2*3
7=7
8=2*2*2
9=3*3
10=2*5
提示
　　先筛出所有素数，然后再分解。
数据规模和约定
　　2<=a<=b<=10000
'''

'''
判断是否是质数：只能被自己和1整除的数
def is_pri(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
'''
#Python break语句，就像在C语言中，打破了最小封闭for或while循环。
#break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
#break语句用在while和for循环中。
#如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
def pri_de(n):
    print("%d="%n,end='')
    while n!=1:
        for i in range(1,n+1):
            if n%i==0 and i!=1:
                n = n // i
                if n!=1:
                    print("%d*"%i,end='')
                else:
                    print("%d"%i)
                break

a,b=map(int,input().split())
#map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
for i in range(a,b+1):
    pri_de(i)



