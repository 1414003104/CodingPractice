'''
有一个 X*Y 的方格, 一个机器人只能走格点且只能向下或者向右走, 要从左上角走到右下角
请设计一个算法, 计算机器人有多少种走法
给定两个个正整数X , Y, 返回机器人走法的数目.
'''
#找出口X=1 or Y=1的时候，都只有一种走法，因为是一条直线
#通过找规律可以发现，走到（m,n）的方法数的和等于走到（m-1,n）和（m,n-1）的方法的和
def robot_go_check(X,Y):
    if X==1 or Y==1:
        return 1
    return robot_go_check(X-1,Y)+robot_go_check(X,Y-1)
x,y=map(int,input().split())
print(robot_go_check(x,y))
