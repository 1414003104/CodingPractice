b=[4,1,3,2]
a=[3,5,7,8]
d=["奥特曼","龙傲天","叶良辰"]
b.sort()
b.pop()
c=a+b
c[2]="马保国"
c.append("王小二")
c.insert(2,"王二麻子")
del c[2]
c.extend(d)
print(c)
print(c[8])
e=("OldSheep",25,25,"男")
print(e)
print(type(e))
#取索引
print(e.index("OldSheep"))
#count是统计一个数据在元组中出现的次数
print(e.count(25))
#统计元组中包含的元素个数
print(len(e))

for info in e:
    print(info)

print("%s的年龄是%d"%(e[0],e[1]))

f=("我","猪","肉")
print("%s喜欢吃%s的%s"%f)

#list能把元组转列表
e1=list(e)
print(type(e1))
#tuple能把列表转元组
e2=tuple(e1)
print(type(e2))

#字典是无序的对象集合
#键是索引，值是数据
yuge={"姓名":"杨明玉","职业":"学生","年龄":25}
print(yuge)
print(yuge["年龄"])
#增加键值对
yuge["战斗力"]=10000000
print(yuge)
#删除键值对
yuge.pop("年龄")
print(yuge)

#字典主要有三个操作
#统计键值对的数目
print(len(yuge))
#合并字典
#如果合并的字典里面有原本有的键值对，则覆盖键值对。
zhuangbei={"装备":"神装","年龄":8888}
yuge.update(zhuangbei)
print(yuge)
#清空字典
#yuge.clear()
#print(yuge)

#遍历字典
for k in yuge:
    print("%s:%s" % (k,yuge[k]))

#将多个字典放在一个列表里面，再进行遍历
card_list=[
    {"name":"OldSheep","phone":584264},
    {"name":"laoyang","phone":547897},
    {"name":"laosepi","Phone":123456}
]

for card_info in card_list:
    print(card_info)


#字符串
#字符串的索引是从0开始的
shabi="我是是大大傻逼"
#单引号的用法
shabi2='我是"大傻逼"'
print(shabi)
print(shabi2)
print(shabi2[1])
for SB in shabi2:
    print(SB)

#注意index是指出字符第一次出现时的索引
#字符串的长度
print(len(shabi))
#统计一个小字符串出现的次数
print(shabi.count("是"))
print(shabi.count("是大"))
#某一个子字符串出现的位置
print(shabi.index("大"))

#字符串的常用操作
#1，判断空白字符
space_str=" "
space_str0="\t"
space_str1="\n"
space_str2="\n22222"
print(space_str.isspace())
print(space_str0.isspace())
print(space_str1.isspace())
print(space_str2.isspace())

#判断字符串中是否只包含数字
#下面这三个方法都不能判断小数

'''
string.isdecimal0
如果string 只包含数字则返回True，全角数字
string.isdigito
如果string 只包含数字则返回True，全角数字、(1)、\u00b2
string.isnumeric0
如果string 只包含数字则返回True，全角数字，汉字数字
'''
num_str="1.1"
#转义字符 unicode编码
num_str0="\u00b2"
print(num_str0)
print(num_str0.isdecimal())
print(num_str0.isdigit())
print(num_str0.isnumeric())

#字符串的查找和替换
hello_str="hello python"
print(hello_str)
#判断是否以指定字符串开始
print(hello_str.startswith("hello"))
print(hello_str.startswith("Hello"))
#判断是否以指定字符串结束
print(hello_str.endswith("thon"))
#查找指定字符串
#index如果找不到指定字符串会报错
#find找不到指定字符串会返回-1
print(hello_str.find("llo"))
print(hello_str.index("llo"))
print(hello_str.find("ll0"))
#替换字符串
#replace执行完毕后会返回一个新的字符串
#注意：不会修改原有字符串的内容
print(hello_str.replace("python","dashabi"))
print(hello_str)