#coding=utf-8
#author: sloop
'''
任务
sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
'''

#代码
L = [i*i for i in range(1,101)]
print sum(L)

'''
L = []
i=1
while i <= 100:
    L.append(i*i)
    i+=1
print sum(L)
'''

'''
调用函数
Python内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数 abs，它接收一个参数。

可以直接从Python的官方网站查看文档：
http://docs.python.org/2/library/functions.html#abs
也可以在交互式命令行通过 help(abs) 查看abs函数的帮助信息。

调用 abs 函数：

>>> abs(100)
100
>>> abs(-20)
20
>>> abs(12.34)
12.34
调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个：

>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：

>>> abs('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
而比较函数 cmp(x, y) 就需要两个参数，如果 x<y，返回 -1，如果 x==y，返回 0，如果 x>y，返回 1：

>>> cmp(1, 2)
-1
>>> cmp(2, 1)
1
>>> cmp(3, 3)
0
Python内置的常用函数还包括数据类型转换函数，比如   int()函数可以把其他数据类型转换为整数：

>>> int('123')
123
>>> int(12.34)
12
str()函数把其他类型转换成 str：

>>> str(123)
'123'
>>> str(1.23)
'1.23'
'''