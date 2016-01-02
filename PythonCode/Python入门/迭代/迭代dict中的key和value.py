#coding=utf-8
#author: sloop
'''
任务
请根据dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

打印出 name : score，最后再打印出平均分 average : score。
'''

#代码
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,':',v
print 'average', ':', sum/len(d)

'''
迭代dict的key和value
我们了解了如何迭代 dict 的key和value，那么，在一个 for 循环中，能否同时迭代 key和value？答案是肯定的。

首先，我们看看 dict 对象的 items() 方法返回的值：

>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> print d.items()
[('Lisa', 85), ('Adam', 95), ('Bart', 59)]
可以看到，items() 方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value：

>>> for key, value in d.items():
...     print key, ':', value
... 
Lisa : 85
Adam : 95
Bart : 59
和 values() 有一个 itervalues() 类似， items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() 不占用额外的内存。
'''