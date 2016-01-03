#coding=utf-8
#author: sloop
'''
任务
利用匿名函数简化以下代码：

def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
'''

print filter(lambda s : s and s.strip(), ['test', None, '', 'str', '  ', 'END'])

'''
print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
'''

'''
匿名函数
高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算 f(x)=x2 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：

def f(x):
    return x * x
关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。

使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：

>>> sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
[9, 5, 3, 1, 0]
返回函数的时候，也可以返回匿名函数：

>>> myabs = lambda x: -x if x < 0 else x 
>>> myabs(-1)
1
>>> myabs(1)
1
'''