'''
Matplotlib库由各种可视化类构成，内部结构复杂。

matplotlib.pylot是绘制各类可视化图形的命令字库

更多学习，可参考Matplotlib中文网：https://www.matplotlib.org.cn
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,5,50)
#linspace（x, y, n）产生x和y之间等间隔的n个数，如果n = 1，返回结果为y。
y = 2*x + 1
#传入x,y,通过plot()绘制出折线图
plt.plot(x,y)
#显示图形
plt.show()


x1 = np.linspace(-1,1,50) #等差数列
y1 = 2*x1 + 1
y2 = x1**2
plt.figure()
#plt.figure?
plt.plot(x1,y1)
plt.figure(figsize=(7,5))#设置图表尺寸为7*5
plt.plot(x1,y2)
plt.show()

# dots1 = np.array([2,3,4,5,6])
# dots2 = np.array([2,3,4,5,6])
dots1 =np.random.rand(50)
#通过本函数可以返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。
'''
应用：在深度学习的Dropout正则化方法中，可以用于生成dropout随机向量（dl），
例如（keep_prob表示保留神经元的比例）：
dl = np.random.rand(al.shape[0],al.shape[1]) < keep_prob
'''
dots2 =np.random.rand(50)
plt.scatter(dots1,dots2,c='red',alpha=0.5) #c表示颜色，alpha表示透明度
plt.show()

#画柱状图
x = np.arange(10)
y = 2**x+10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')#绘制柱状图
plt.show()

#在柱状图顶端标上信息
x = np.arange(10)
y = 2**x+10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')
for ax,ay in zip(x,y):
    plt.text(ax,ay,'%.1f' % ay,ha='center',va='bottom')
plt.show()



