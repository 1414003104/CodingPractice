'''
1241783
无法取相邻的数
最大的和是多少
'''
arr=[1,2,4,1,7,8,3]

#递归实现
def rec_opt(arr,i):
    if i==0:
        return arr[0]
    elif i==1:
        return max(arr[0],arr[1])
    else:
        A=rec_opt(arr,i-2)+arr[i]#函数的意思是求到某个位置的最大和是
        B=rec_opt(arr,i-1)
        return max(A,B)

print(rec_opt(arr,6))

#动态规划
def dp_opt(arr):
    dp_arr=[0 for i in range(len(arr))]
    dp_arr[0]=arr[0]
    dp_arr[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A=dp_arr[i-2]+arr[i]#这样避免了重复计算
        B=dp_arr[i-1]
        dp_arr[i]=max(A,B)
    #print(dp_arr)
    return dp_arr[-1]

print(dp_opt(arr))

