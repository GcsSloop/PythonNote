#coding=utf-8
#author: sloop
'''
任务
新来的Paul同学成绩是 75 分，请编写一个dict，把Paul同学的成绩也加进去。

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
'''

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print u'大小=',len(d)
for k,v in d.iteritems():
    print k,':',v

'''
什么是dict
我们已经知道，list 和 tuple 可以用来表示顺序集合，例如，班里同学的名字：

['Adam', 'Lisa', 'Bart']
或者考试的成绩列表：

[95, 85, 59]
但是，要根据名字找到对应的成绩，用两个 list 表示就不方便。

如果把名字和分数关联起来，组成类似的查找表：

'Adam' ==> 95
'Lisa' ==> 85
'Bart' ==> 59
给定一个名字，就可以直接查到分数。

Python的 dict 就是专门干这件事的。用 dict 表示“名字”-“成绩”的查找表如下：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。

花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。

由于dict也是集合，len() 函数可以计算任意集合的大小：

>>> len(d)
3
注意: 一个 key-value 算一个，因此，dict大小为3。
'''