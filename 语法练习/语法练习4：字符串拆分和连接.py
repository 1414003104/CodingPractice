#string.split(str=""，num)以str为分隔符拆分string，如果num有指定值，则仅分割num+1个子字符串

poem_str="登黄雀楼\t 王之涣\t 白日依山尽\t \n 黄河入海流\t\t 欲穷千里目\t\t更上一层楼"

print(poem_str)

#拆分字符串成列表
poem_list = poem_str.split()
print(poem_list)

#合并列表为字符串
poem_result = " ".join(poem_list)
print(poem_result)