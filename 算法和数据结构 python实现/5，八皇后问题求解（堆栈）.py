'''
皇后可以对角斜吃，直吃，横吃
放入多个皇后到棋盘，相互之间还不能互相吃到对方
N*N就是N皇后问题

堆栈+回溯解决
'''
global queen
global number
EIGHT=8#定义堆栈的最大容量
queen=[None]*8#堆栈存放8个皇后的行位置

number=0#计算总共有几组解
#决定皇后存放的位置
#输出所需要的结果
def print_table():
    global number
    x=y=0
    number+=1
    print('')
    print('8皇后问题的第%d组解\t'%number)
    for x in range(EIGHT):
        for y in range(EIGHT):
            if x==queen[y]:
                print('<q>',end='')#所存储的行位置是否对应，是就输出这个位置的皇后
            else:
                print('<->',end='')
        print('\t')
    input('\n..按下任意键继续..\n')

#测试在(row,col)上的皇后是否遭受攻击
#若遭受攻击则返回值为1，否则返回0
def attack(row,col):#行、列
    global queen
    i=0#列循环参数
    atk=0#标志位
    offset_row=offset_col=0
    while (atk!=1) and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)
        #判断两皇后是否在同一行或在同一对角线上
        if queen[i]==row or offset_row==offset_col:#这两个如果相等则说明斜率相等
            atk=1
        i=i+1
    return atk

def decide_position(value):
    global queen
    i=0
    while i<EIGHT:
        if attack(i,value)!=1:
            queen[value]=i
            if value==7:
                print_table()
            else:
                decide_position(value+1)
        i=i+1

#主程序
decide_position(0)
