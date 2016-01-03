#coding=utf-8
#author: sloop
'''
任务
请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

import math
def is_sqr(x):
    return math.sqrt(x)%1 == 0

print filter(is_sqr, range(1, 101))

'''
is_sqr其他实现方式
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x

def is_sqr(x):
    return math.sqrt(x)- int(math.sqrt(x)) == 0

 def is_sqr(x):
    math.modf( math.sqrt(x) )[0] != 0.0
 
def is_sqr(x):
    return x==int(math.sqrt(x))**2
'''

'''
filter()函数
filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

例如，要从一个list [1, 4, 6, 7, 9, 12, 17]中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：

def is_odd(x):
    return x % 2 == 1
然后，利用filter()过滤掉偶数：

filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
结果：[1, 7, 9, 17]

利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：

def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
结果：['test', 'str', 'END']

注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。

当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：

a = '     123'
a.strip()
结果： '123'

a='\t\t123\r\n'
a.strip()
结果：'123'
'''