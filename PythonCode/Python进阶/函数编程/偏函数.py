#coding=utf-8
#author: sloop
'''
任务
在第7节中，我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。请用functools.partial把这个复杂调用变成一个简单的函数：

sorted_ignore_case(iterable)

偏函数中的参数说明：第一个参数时被改变函数名，第二个参数是函数参数的默认值
'''

import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1,s2:cmp(s1.lower(),s2.lower()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

'''
偏函数
当一个函数有很多参数时，调用者就需要提供多个参数。如果减少参数个数，就可以简化调用者的负担。

比如，int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

>>> int('12345')
12345
但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做 N 进制的转换：

>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x, base=2):
    return int(x, base)
这样，我们转换二进制就非常方便了：

>>> int2('1000000')
64
>>> int2('1010101')
85
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
所以，functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
'''