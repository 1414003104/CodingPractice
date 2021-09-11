#extend() append()
a=[1,2,3]
b=[4,5]
print(a+b)
a.extend(b)
print(a)
a.append(0)
print(a)
a.append(b)
print(a)
#区别在于+号生成了一个新的列表 而后面两个并没有生成列表，只是对列表a进行了操作


# in 和 not in 成员运算符
print('a' in "abcd")
print('a' not in "abcd")
print(1 in [0,1,2])
print('a' in {'a':"laowang"})
print("laowang" in {'a':"laowang"})#只能判断字典的key,不能判断字典的值



