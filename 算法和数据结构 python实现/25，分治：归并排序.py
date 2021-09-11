def merge(sort_LA,sort_RA):#最后的合并
    i,j=0,0
    M_Arry=[]
    while i<len(sort_LA) and j<len(sort_RA):
        if sort_LA[i]<sort_RA[j]:
            M_Arry.append(sort_LA[i])
            i+=1
        else:
            M_Arry.append(sort_RA[j])
            j+=1
    #上面的遍历过程，可能会有一边先走完，所以还要把没走完的继续走完
    while i<len(sort_LA):
        M_Arry.append(sort_LA[i])
        i+=1
    while j<len(sort_RA):
        M_Arry.append(sort_RA[j])
        j+=1
    return M_Arry

def merge_sort(Arry):
    #你特么居然忘记写递归出口，吐了
    if len(Arry)<=1:
        return Arry
    mid=len(Arry)//2
    LArry=Arry[:mid]
    RArry=Arry[mid:]
    sort_LA=merge_sort(LArry)
    sort_RA=merge_sort(RArry)
    sort_Arry=merge(sort_LA,sort_RA)
    return sort_Arry



#test
# A=[1,4,5,6]
# B=[3,7,9,10]
# print(merge(A,B))
C=[1,4,5,6,3,7,9,10]
D=[77,59,88,14,23,7,9]
print(merge_sort(C))
print(merge_sort(D))

