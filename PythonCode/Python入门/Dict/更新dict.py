#coding=utf-8
#author: sloop

'''
任务
请根据Paul的成绩 72 更新下面的dict：

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
'''

#代码
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72]='Paul'
print d

'''
更新dict
dict是可变的，也就是说，我们可以随时往dict中添加新的 key-value。比如已有dict：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
要把新同学'Paul'的成绩 72 加进去，用赋值语句：

>>> d['Paul'] = 72
再看看dict的内容：

>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}
如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：

>>> d['Bart'] = 60
>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60}
'''