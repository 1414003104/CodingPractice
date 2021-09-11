'''
编写一个方法,打印n对括号的全部有效组合(即左右括号正确匹配)
示例
输入:3
输出:()()(),((())),(())(),()(()),(()())
'''
def print_bracket(n):
    res=[]
    if n==1:
        res.append("()")
    print_bracket(n-1)