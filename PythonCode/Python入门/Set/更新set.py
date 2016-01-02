#coding=utf-8
#author: sloop
'''
任务
针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。

s = set(['Adam', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
'''

#代码
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for k in L:
    if k in s:
        s.remove(k)
    else:
        s.add(k)
print s

'''
更新set
由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：

一是把新的元素添加到set中，二是把已有元素从set中删除。

添加元素时，用set的add()方法：

>>> s = set([1, 2, 3])
>>> s.add(4)
>>> print s
set([1, 2, 3, 4])
如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：

>>> s = set([1, 2, 3])
>>> s.add(3)
>>> print s
set([1, 2, 3])
删除set中的元素时，用set的remove()方法：

>>> s = set([1, 2, 3, 4])
>>> s.remove(4)
>>> print s
set([1, 2, 3])
如果删除的元素不存在set中，remove()会报错：

>>> s = set([1, 2, 3])
>>> s.remove(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
所以用add()可以直接添加，而remove()前需要判断。
'''