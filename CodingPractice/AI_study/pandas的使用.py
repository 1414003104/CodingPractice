'''
1.Series
Series是一种类似于一维数组的对象，它由一维数组（各种numpy数据类型）以及一组与之相关的数据标签（即索引）组成.

可理解为带标签的一维数组，可存储整数、浮点数、字符串、Python 对象等类型的数据。
'''
import pandas as pd
import numpy as np

s=pd.Series(['a','b','c','d','e'])
print(s)
#Series允许重复索引
s=pd.Series(['a','b','c','d','e'],index=[100,200,100,400,500])
print(s)

#Series 可以用字典实例化
d = {'b': 1, 'a': 0, 'c': 2}
print(pd.Series(d))

#可以通过Series的values和index属性获取其数组表示形式和索引对象
print(s.values)
print(s.index)

#与普通numpy数组相比，可以通过索引的方式选取Series中的单个或一组值
print(s[100])
print(s[[400,500]])

s1=pd.Series(np.array([1,2,3,4,5],dtype=np.int64),index=['a','b','c','d','e'])
print(s1)
print(s1+s1)
print(s1*3)
print(s1**2)

'''
Series中最重要的一个功能是：它会在算术运算中自动对齐不同索引的数据.
Series 和多维数组的主要区别在于， Series 之间的操作会自动基于标签对齐数据。因此，不用顾及执行计算操作的 Series 是否有相同的标签。
'''
'''
np.nan是一个float类型的数据 None是一个NoneType类型
'''
obj1 = pd.Series({"Ohio": 35000, "Oregon": 16000, "Texas": 71000, "Utah": 5000})
print(obj1)
obj2 = pd.Series({"California": np.nan, "Ohio": 35000, "Oregon": 16000, "Texas": 71000})
print(obj2)
print(obj1 + obj2)

#Series取索引和切片
s = pd.Series(np.array([1,2,3,4,5]), index=['a', 'b', 'c', 'd', 'e'])
print(s[1:])
print(s[:-1])
print(s[1:] + s[:-1])




'''
2,DataFrame:
DataFrame是一个表格型的数据结构，类似于Excel或sql表

它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）

DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（共用同一个索引）
'''
#用多维数组字典、列表字典生成 DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)

#如果指定了列顺序，则DataFrame的列就会按照指定顺序进行排列
frame1 = pd.DataFrame(data, columns=['year', 'state', 'pop'])#columns是返回引用中的列数
print(frame1)

#跟原Series一样，如果传入的列在数据中找不到，就会产生NAN值
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)

#用 Series 字典或字典生成 DataFrame
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(d))

#通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series,返回的Series拥有原DataFrame相同的索引
print(frame2['state'])
print(frame2['pop'])

#列可以通过赋值的方式进行修改,例如，给那个空的“delt”列赋上一个标量值或一组值
frame2['debt']=16.5
print(frame2)

frame2['debt']=frame2['debt']*frame2['pop']
print(frame2)

frame2['debt'] = np.arange(5.)
print(frame2)


