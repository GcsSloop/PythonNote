#coding=utf-8
#author: sloop
'''
任务
班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：

L = [75, 92, 59, 68]

请利用for循环计算出平均成绩。
'''

#代码
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum+=score
print sum / 4

'''
for循环
list或tuple可以表示一个有序集合。如果我们想依次访问一个list中的每一个元素呢？比如 list：

L = ['Adam', 'Lisa', 'Bart']
print L[0]
print L[1]
print L[2]
如果list只包含几个元素，这样写还行，如果list包含1万个元素，我们就不可能写1万行print。

这时，循环就派上用场了。

Python的 for 循环就可以依次把list或tuple的每个元素迭代出来：

L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name
注意:  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。

这样一来，遍历一个list或tuple就非常容易了。
'''