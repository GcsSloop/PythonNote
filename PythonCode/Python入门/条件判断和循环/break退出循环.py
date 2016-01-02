#coding=utf-8
#author: sloop
'''
任务
利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
'''

#代码
sum = 0
x = 1
n = 1
while True:
    sum+=x
    x*=2
    n+=1
    if n>20:
        break
print sum

'''
break退出循环
用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。

比如计算1至100的整数和，我们用while来实现：

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
咋一看， while True 就是一个死循环，但是在循环体内，我们还判断了 x > 100 条件成立时，用break语句退出循环，这样也可以实现循环的结束。
'''