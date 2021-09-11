#numpy
import numpy as np
arr=np.array([[1,2],[3,4]])
print(arr)

#生成不同类型的数组
zeroarr=np.zeros((2,3),dtype='float')
onearr=np.ones((2,3),dtype='int')
emptyarr=np.empty((3,4),dtype='int')
array_1=np.arange(2,13,2)
print(zeroarr)
print(onearr)
print(emptyarr)
print(array_1)

#获取数组的不同属性
array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(array)
#数组维度
print(array.ndim)
#数组形状
print(array.shape)
#数组元素个数
print(array.size)
#数组元素类型
print(array.dtype)

#对数组形状进行转换
array_2=np.arange(6).reshape(2,3)
print(array_2)
array_3=np.array([[1,2,3],[4,5,6]],dtype=np.int64).reshape((3,2))
print(array_3)

#数组的基本运算
array_a=np.array([[1,2,3],[4,5,6]],dtype='int')
array_b=np.ones((2,3),dtype='int')
print(array_a+array_b)
print(array_a-array_b)
print(array_a*array_b)
print(array_a/array_b)
print(array_a**3)

#矩阵乘法
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.ones([3,2],dtype=np.int64)
print(arr3)
print(arr4)
print(np.dot(arr3,arr4))#dot是获取两个元素的乘积

#矩阵的其他运算
print(np.sum(arr3,axis=0)) #axis=1,每一行求和 axie=0,每一列求和
print(np.sum(arr3,axis=1))
print(np.max(arr3))
print(np.min(arr3))
print(np.argmax(arr3))
print(np.argmin(arr3))#最大最小值的下标
print(np.mean(arr3))#平均值

arr3_tran = arr3.transpose()#类似于矩阵的转置
print(arr3_tran)
print(arr3.flatten())
print(arr3.flatten('F'))
print(arr3_tran.flatten())
'''
a.flatten() #默认按行的方向降维
a.flatten('F') #按列降维
a.flatten('A') #按行降维

常用在从卷积层到全连接层的过渡
'''

#数组的索引和切片
arr5 = np.arange(0,6).reshape([2,3])
print(arr5)
print(arr5[0])
print(arr5[1])
print(arr5[0][2])
print(arr5[0,2])

print(arr5[1,2:])
print(arr5[:,1])
print(arr5[1,1:3])