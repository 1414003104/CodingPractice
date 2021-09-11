'''
问题描述
　　给定一个以秒为单位的时间t，要求用“<H>:<M>:<S>”的格式来表示这个时间。<H>表示时间，<M>表示分钟，而<S>表示秒，它们都是整数且没有前导的“0”。
   例如，若t=0，则应输出是“0:0:0”；若t=3661，则输出“1:1:1”。
输入格式
　　输入只有一行，是一个整数t（0<=t<=86399）。
输出格式
　　输出只有一行，是以“<H>:<M>:<S>”的格式所表示的时间，不包括引号。
样例输入
0
样例输出
0:0:0
样例输入
5436
样例输出
1:30:36
'''
t=int(input())
h=t//3600
m=(t-h*3600)//60
s=t-h*3600-m*60
print(h,':',m,':',s,sep='')
#同时打印多个字符串的时候，每个字符串都会自动默认以空格作为每个字符串之间的间隔。
#sep是间隔的意思，这里是没有间隔