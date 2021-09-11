import paddle

#定义两个张量
x1 = paddle.ones([2,2], dtype='int64')
print(x1)
'''
二维数组其实就是一个二阶张量
这里的意思是创建一个数值全为1的2*2的二维数组
'''
x2 = paddle.ones([2,2], dtype='int64')

x3=paddle.zeros([2,3],dtype='int64')
x4=paddle.zeros([2,3],dtype='int64')

# 将两个张量求和
y1 = paddle.add(x1, x2)
y2=paddle.add(x3,x4)

# 查看结果
print(y1)
print(y2)