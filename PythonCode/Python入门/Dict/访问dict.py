#coding=utf-8
#author: sloop
'''
任务
根据如下dict：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
请打印出：

Adam: 95
Lisa: 85
Bart: 59
'''

#代码
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:',d.get('Adam')
print 'Lisa:',d.get('Lisa')
print 'Bart:',d.get('Bart')

'''
访问dict
我们已经能创建一个dict，用于表示名字和成绩的对应关系：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
那么，如何根据名字来查找对应的成绩呢？

可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：

>>> print d['Adam']
95
>>> print d['Paul']
Traceback (most recent call last):
  File "index.py", line 11, in <module>
    print d['Paul']
KeyError: 'Paul'
注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。

要避免 KeyError 发生，有两个办法：

一是先判断一下 key 是否存在，用 in 操作符：

if 'Paul' in d:
    print d['Paul']
如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。

二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：

>>> print d.get('Bart')
59
>>> print d.get('Paul')
None
'''