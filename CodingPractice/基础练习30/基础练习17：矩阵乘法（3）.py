#自己写的
def matrix_multiply(matrix_A,matrix_B,matrix_C,N):#这个函数是求矩阵相乘,求完后存到C里面
    for i in range(N):
        for j in range(N):#C的元素位置
            temp=0
            for k in range(N):
                temp+=int(matrix_A[i*N+k])*int(matrix_B[k*N+j])#行数列数个数相乘的和就是C的对应位置的元素
            matrix_C[i*N+j]=temp

N,M=map(int,input().split())
matrix_N=[]
matrix_NN=[]
for i in range(N):
    matrix_NN=map(int,input().split())
    matrix_N.extend(matrix_NN)
#print(matrix_N)

#需要判断是否为单位阵，以及M为1的情况
if M>1:
    matrix_temp=matrix_N
    for i in range(M-1):
        matrix_Final = [0 for i in range(N * N)]#切记一定要每次都初始化，不然会错误
        matrix_multiply(matrix_temp,matrix_N,matrix_Final,N)
        matrix_temp=matrix_Final
        #print(matrix_Final)
    for i in range(N):
        for j in range(N):
            print(matrix_Final[i * N + j], end=' ')
        print()
elif M==1:
    print(matrix_N)
elif M==0:
    for i in range(N):
        for j in range(N):
            if i==j:
                matrix_N[i*N+j]=1
            else:
                matrix_N[i*N+j]=0
    for i in range(N):
        for j in range(N):
            print(matrix_N[i * N + j], end=' ')
        print()



