'''
给定一组股票价格序列
求出能获得最佳收益的买进、卖出点

·举例
-股票价格prices = [10,11,7,10,6]
-买进:prices[2]= 7
-卖出:prices[3]= 10
- max profit = 10-7
'''
#暴力实现
def Max_profit(Arry):
    Dif_profit=[]
    max_profit=0
    B_S = []
    for i in range(len(Arry)):
        for j in range(i+1,len(Arry)):
            Now_profit=Arry[j]-Arry[i]
            if Now_profit>=max_profit:
                max_profit=Now_profit
                B_S = [i,j]
    return max_profit,B_S

prices = [10,11,7,10,6]
A,B=Max_profit(prices)
print(A,B)

#用分治实现，时间复杂度并没有下降，而且更为复杂
# uMax
# ·找到左边序列最小值，论为min(买点)
# ·找到右边序列的最大值，记为max(卖点)
# ·它们之间的差值就是跨界情况下的解s_cross = max-min
def dc_profit(Arr):
    if len(Arr)<=1:
        return 0#因为只有一个数据的时候，代表价格不会变动，收益始终为0
    mid=len(Arr)//2
    Arr_L=Arr[:mid]
    Arr_R=Arr[mid:]
    S_Arr_L=dc_profit(Arr_L)
    S_Arr_R=dc_profit(Arr_R)
    #考虑跨界情况
    S_Arr_L_R=max(Arr_R)-min(Arr_L)
    return max(S_Arr_L,S_Arr_R,S_Arr_L_R)

print(dc_profit(prices))


