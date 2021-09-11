'''
给定整数序列a1,a2,...,an,判断是否可以从中选出m个数,使它们的和恰好为k
1<= n <= 20
-10^8 < ai < 10^8
-10^8 < k < 10^8
输入:    n = 4
        a=[1,4,2,7]
         k = 13
输出:   [[4,2,7]]

定义状态 : 当前考察的数字: arr[cur] , 已选择的数字集合
状态转移: 当前已选数字和小于k 时 , 顺次cur +1, 若大于了k, 则为死路, 考虑回退
选择路径顺序 : 对每一个状态时, 先考虑 选 , 其回溯后考虑 不选
和上面数独题类似, 也要考虑递归设计三要素:
找出口: 要么sum=k, 表示找到一个解, 此时退出, 若要寻找所有解, 则应当返回; 要么sum > k , 则说明此路径错误, 返回
找重复: 对于每一个状态的选择方法一致, 要么选要么不选, 属于同问题不同规模
找变化: sum变化, cur变化, 若需要保留每一组解, 则需引入的最终结果集res, 以及每个结果item 均在变化 (回忆找变化的作用: 往往用来定参数)
下面依然以 arr = [1, 2, 4,7 ] , k =13 为例, 其中cur为当前考虑的arr下标, sum为当前选了的数字和, item用于存放当前选了的数字
'''
#res存放满足条件的结果
#item存放当前选了的数字
#cur为当前考虑是否挑选的arr的下标
#k是剩余数据要加起来得到的数
def part_sum(arr,res,item,cur,k):
    if k==0:
        res.append(item)
        return#你正在运行第n次的递归函数函数出口
    if k<0 or cur==len(arr):
        return

    #不选择当前位置的数
    item_temp = item.copy()
    part_sum(arr, res, item_temp, cur + 1, k)#遇到return之后这个递归调用结束，继续执行下面的函数

    #选择当前位置的数
    item.append(arr[cur])
    item_temp=item.copy()
    part_sum(arr,res,item_temp,cur+1,k-arr[cur])

    #玉哥备注：比如，第0个数不选，先循环完一轮，没有添加任何数，

Arry=[1,2,3,4,5]
res=[]
item=[]
k=int(input())
part_sum(Arry,res,item,0,k)
print(res)

