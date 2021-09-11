#for 变量 in 集合：
#     循环体代码
#else:
#      没有通过break退出循环，循环结束后执行else后的代码
for num in [1,2,3]:
    print(num)
    if num==2:
        break
else:
    #如果循环体内部使用break退出了循环
    #else下方的代码就不会被执行
    print("会执行嘛？")
print("循环结束")

#应用
#在迭代遍历嵌套的数据类型时，假如一个列表包含了多个字典
#需求：判断某一个字典是否存在指定的值
students=[
    {"name":"阿土"},
    {"name":"小美"}
]
find_name="张三"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"]==find_name:
        print("找到了 %s"%find_name)
        #如果已经找到，应该直接推出循环，而不需要再遍历后续的元素
        break
else:
    #如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    #还希望得到一个统一的提示！
    print("抱歉，没有找到%s"%find_name)
print("循环结束")
