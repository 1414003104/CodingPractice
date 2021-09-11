def binary_find(Arry,N):
    first=0
    end=len(Arry)-1
    find_it=False
    while first<=end and find_it==False:
        mid=(first+end)//2
        if N==Arry[mid]:
            find_it=True
        else:
            if N>Arry[mid]:
                first=mid+1
            else:
                end=mid-1
    return find_it

A=[1,3,4,5,6,7,9]
N=int(input())
print(binary_find(A,N))

