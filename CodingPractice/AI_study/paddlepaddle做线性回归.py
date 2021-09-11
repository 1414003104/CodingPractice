import paddle
import numpy as np

# 定义训练和测试数据
x_data = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   [2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   [3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   [4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   [5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]).astype('float32')

y_data = np.array([[3.0], [5.0], [7.0], [9.0], [11.0]]).astype('float32')
#print(y_data)
test_data = np.array([[6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]).astype('float32')

# 定义一个简单的线性网络
net = paddle.nn.Sequential(
    paddle.nn.Linear(13, 100),
    paddle.nn.ReLU(),
    paddle.nn.Linear(100, 1)
)
#这里定义输入层的形状为13，这是因为波士顿房价数据集的每条数据有13个属性，我们之后自定义的数据集也是为了符合这一个维度。

# 定义优化方法
optimizer = paddle.optimizer.SGD(learning_rate=0.01, parameters=net.parameters())#随机梯度下降优化方法

# 将numpy类型数据转换成tensor之后才能用于模型训练
inputs = paddle.to_tensor(x_data)
labels = paddle.to_tensor(y_data)

# 开始训练100个pass
for pass_id in range(10):
    out = net(inputs)
    loss = paddle.mean(paddle.nn.functional.square_error_cost(out, labels))

    loss.backward()
    optimizer.step()
    optimizer.clear_grad()

    print("Pass:%d, Cost:%0.5f" % (pass_id, loss))

# 开始预测
predict_inputs = paddle.to_tensor(test_data)
result = net(predict_inputs)

print("当x为6.0时，y为：%0.5f" % result)

