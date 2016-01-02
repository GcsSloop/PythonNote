#coding=utf-8
#author: sloop

'''
任务
请用 for 循环遍历如下的set，打印出 name: score 来。

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
'''

#代码
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0],':',x[1]


'''
遍历set
由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。

直接使用 for 循环可以遍历 set 的元素：

>>> s = set(['Adam', 'Lisa', 'Bart'])
>>> for name in s:
...     print name
... 
Lisa
Adam
Bart
注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。
'''