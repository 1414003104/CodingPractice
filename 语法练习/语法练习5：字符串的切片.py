#切片方法适用于字符串、列表、元组
#字符串[开始索引：结束索引：步长]
#步长是指的中间的跳跃间隔

poem_str="白日依山尽黄河入海流"
#截取2到5位置的字符串
print(poem_str[2:6])
#截取从2到末尾的字符串
print(poem_str[2:])
#截取从 开始到5的字符串
print(poem_str[0:6])
#截取全部字符串
print(poem_str[:])
#从开始位置，每隔1个字符截取字符串
print(poem_str[::2])
#从索引1开始，每隔1个字符截取字符串
print(poem_str[1::2])
#截取从2到末尾-1的字符串
print(poem_str[2:-1])
#截取字符串末尾两个字符
print(poem_str[-2:])

#字符串的逆序
print(poem_str[-1::-1])