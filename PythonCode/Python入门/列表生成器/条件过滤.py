#coding=utf-8
#author: sloop
'''
任务
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。

提示：

1. isinstance(x, str) 可以判断变量 x 是否是字符串；

2. 字符串的 upper() 方法可以返回大写的字母。
'''

#代码
def toUppers(L):
    return [i.upper() for i in L if isinstance(i, str) ]

print toUppers(['Hello', 'world', 101])

'''
条件过滤
列表生成式的 for 循环后面还可以加上 if 判断。例如：

>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。
'''