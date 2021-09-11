'''
问题描述
　　回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，
请你计算最少的交换次数使得该串变成一个完美的回文串。
　　交换的定义是：交换两个相邻的字符
　　例如mamad
　　第一次交换 ad : mamda
　　第二次交换 md : madma
　　第三次交换 ma : madam (回文！完美！)
输入格式
　　第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
　　第二行是一个字符串，长度为N.只包含小写字母
输出格式
　　如果可能，输出最少的交换次数。
　　否则输出Impossible
样例输入
5
mamad
样例输出
3
'''
#①判断:
#若字符串长度为偶数，则每个字符出现的次数都必须是偶数次，否则不对称
#若字符串长度为奇数，则只能有一个字符出现奇数次（在字符串最中间出现一次）
n=int(input())
List_N=list(input())
#print(List)

def can_swap(List):
    a=len(List)
    if a%2==0:
        for ch in List:
            if List.count(ch)%2!=0:
                print("Impossible")
                return False
    else:
        flag=0
        for ch in List:
            if List.count(ch)==1:
                flag+=1
        if flag>1:
            print("Impossible")
            return False
    return True

def swap_count(List):
    count = 0  # 统计交换次数
    while len(List)>0:
        for i in range(len(List)-1,0,-1):
            if List[i]==List[0]:
                count+=len(List)-1-i#从位置k交换到列表末尾需要的次数
                List.pop(0)#把当前找到的数出队列
                List.pop(i-1)#因为索引为0的数已经出对，之前的索引1变成了0，后续的数的索引-1
            elif i==1:#如果列表里面只剩下最后一个数，取本身会行不通
                count += len(List)//2  # 把这个数交换到中间需要的次数
                List.pop(0)
        return count

if can_swap(List_N):
    print(swap_count(List_N))

