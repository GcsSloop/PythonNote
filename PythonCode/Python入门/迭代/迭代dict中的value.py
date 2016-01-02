#coding=utf-8
#author: sloop
'''
任务
给定一个dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

请计算所有同学的平均分。
'''

#代码
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for i in d.itervalues():
    sum += i
print sum/len(d)

'''
迭代dict的value
我们已经了解了dict对象本身就是可迭代对象，用 for 循环直接迭代 dict，可以每次拿到dict的一个key。

如果我们希望迭代 dict 对象的value，应该怎么做？

dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v
# 85
# 95
# 59
如果仔细阅读Python的文档，还可以发现，dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.itervalues()
# <dictionary-valueiterator object at 0x106adbb50>
for v in d.itervalues():
    print v
# 85
# 95
# 59
那这两个方法有何不同之处呢？

1. values() 方法实际上把一个 dict 转换成了包含 value 的list。

2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。

3. 打印 itervalues() 发现它返回一个 <dictionary-valueiterator> 对象，这说明在Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。

如果一个对象说自己可迭代，那我们就直接用 for 循环去迭代它，可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求。
'''