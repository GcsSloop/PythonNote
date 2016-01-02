#coding=utf-8
#author: sloop
'''
任务
对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
'''

#代码
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2==0:
        continue
    sum+=x
print sum

'''
continue继续循环
在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。

假设我们已经写好了利用for循环计算平均分的代码：

L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    sum = sum + x
    n = n + 1
print sum / n
现在老师只想统计及格分数的平均分，就要把 x < 60 的分数剔除掉，这时，利用 continue，可以做到当 x < 60的时候，不继续执行循环体的后续代码，直接进入下一次循环：

for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
'''