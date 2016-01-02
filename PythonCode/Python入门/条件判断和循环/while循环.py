#coding=utf-8
#author: sloop
'''
任务
利用while循环计算100以内奇数的和。
'''

#代码
sum = 0
x = 1
while x<=100:
    sum+=x
    print x
    x+=2
print sum


'''
sum = 0
x = 1
while x<100:
    if x%2!=0:
        sum+=x
    x+=1
print sum
'''
'''
while循环
和 for 循环不同的另一种循环是 while 循环，while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。

比如要从 0 开始打印不大于 N 的整数：

N = 10
x = 0
while x < N:
    print x
    x = x + 1
while循环每次先判断 x < N，如果为True，则执行循环体的代码块，否则，退出循环。

在循环体内，x = x + 1 会让 x 不断增加，最终因为 x < N 不成立而退出循环。

如果没有这一个语句，while循环在判断 x < N 时总是为True，就会无限循环下去，变成死循环，所以要特别留意while循环的退出条件。
'''