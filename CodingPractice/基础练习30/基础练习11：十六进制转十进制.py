'''
问题描述
　　从键盘输入一个不超过8位的正的十六进制数字符串，将它转换为正的十进制数后输出。
　　注：十六进制数中的10~15分别用大写的英文字母A、B、C、D、E、F表示。
样例输入
FFFF
样例输出
65535
'''
num=input()
print(int(num,16))
#int() 函数用于将一个字符串或数字转换为整型。
#int('12',16)        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制