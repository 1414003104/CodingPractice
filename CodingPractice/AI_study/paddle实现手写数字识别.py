import paddle
from paddle.vision.transforms import Normalize

#准备数据
#使用normalize对图片进行归一化
#图像归一化处理，支持两种方式：
# 1. 用统一的均值和标准差值对图像的每个通道进行归一化处理；
# 2. 对每个通道指定不同的均值和标准差值进行归一化处理。
transform = Normalize(mean=[127.5],
                               std=[127.5],
                               data_format='CHW')
# 使用transform对数据集做归一化
#print('download training data and load training data')
train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)#模式设置为训练集
test_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)#模式设置为测试集
#print('load finished')

import numpy as np
import matplotlib.pyplot as plt
train_data0, train_label_0 = train_dataset[0][0],train_dataset[0][1]
#print(train_data0)
train_data0 = train_data0.reshape([28,28])#将数组变为28*28的二维数组
plt.figure(figsize=(2,2))
plt.imshow(train_data0, cmap=plt.cm.binary)
#plt.show()
print('train_data0 label is: ' + str(train_label_0))


#配置网络
#因为MNIST数据集是手写0到9的灰度图像，类别有10个，所以最后的输出大小是10
# 定义多层感知机
class MultilayerPerceptron(paddle.nn.Layer):#继承于paddle.nn.layer这个父类
    def __init__(self, in_features):
        super(MultilayerPerceptron, self).__init__()
        #在单类继承中，其意义就是不需要父类的名称来调用父类的函数，
        # 因此当子类改为继承其他父类的时候，不需要对子类内部的父类调用函数做任何修改就能调用新父类的方法。

        # 形状变换，将数据形状从 [] 变为 []
        self.flatten = paddle.nn.Flatten()
        # 第一个全连接层
        self.linear1 = paddle.nn.Linear(in_features=in_features, out_features=100)#线性变换层
        #in_features (int) – 线性变换层输入单元的数目。
        #out_features (int) – 线性变换层输出单元的数目。

        # 使用ReLU激活函数
        self.act1 = paddle.nn.ReLU()
        #ReLU(x)=max(0,x)

        # 第二个全连接层
        self.linear2 = paddle.nn.Linear(in_features=100, out_features=100)
        # 使用ReLU激活函数
        self.act2 = paddle.nn.ReLU()

        # 第三个全连接层
        self.linear3 = paddle.nn.Linear(in_features=100, out_features=10)#因为数字是从0到9，共10个数

    def forward(self, x):
        # x = x.reshape((-1, 1, 28, 28))
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.act1(x)
        x = self.linear2(x)
        x = self.act2(x)
        x = self.linear3(x)
        return x

# 使用 paddle.Model 封装 MultilayerPerceptron
model = paddle.Model(MultilayerPerceptron(in_features=784))
#Model 对象是一个具备训练、测试、推理的神经网络。该对象同时支持静态图和动态图模式
# 使用 summary 打印模型结构
model.summary((-1, 1, 28, 28))
'''
summary(input_size=None, batch_size=None, dtype=None)
input_size (tuple|InputSpec|list[tuple|InputSpec，可选) - 输入张量的大小。
如果网络只有一个输入，那么该值需要设定为tuple或InputSpec。如果模型有多个输入。
那么该值需要设定为list[tuple|InputSpec]，包含每个输入的shape。
如果该值没有设置，会将 self._inputs 作为输入。默认值：None。

batch_size (int，可选) - 输入张量的批大小。默认值：None。
dtypes (str，可选) - 输入张量的数据类型，如果没有给定，默认使用 float32 类型。默认值：None。
'''

# 配置模型
model.prepare(paddle.optimizer.Adam(parameters=model.parameters()),  # 使用Adam算法进行优化
              paddle.nn.CrossEntropyLoss(), # 使用CrossEntropyLoss 计算损失
              paddle.metric.Accuracy()) # 使用Accuracy 计算精度

# 开始模型训练
model.fit(train_dataset, # 设置训练数据集
          epochs=5,      # 设置训练轮数
          batch_size=64, # 设置 batch_size 批大小
          verbose=1)     # 设置日志打印格式

#调用 evaluate 接口并传入验证集即可。这里我们使用测试集作为验证集。
model.evaluate(test_dataset, verbose=1)

#完成模型预测也非常的简单，只需要调用 predict 接口并传入测试集即可。
results = model.predict(test_dataset)

# 获取概率最大的label
lab = np.argsort(results)                               #argsort函数返回的是result数组值从小到大的索引值
# print(lab)
print("该图片的预测结果的label为: %d" % lab[0][0][-1][0])  #-1代表读取数组中倒数第一列