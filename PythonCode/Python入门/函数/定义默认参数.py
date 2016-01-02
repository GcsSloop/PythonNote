#coding=utf-8
#author: sloop

'''
任务
请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
'''

#代码
def greet(str1='world'):
    print 'Hello,',str1+'.'

greet()
greet('Bart')

'''
定义默认参数
定义函数的时候，还可以有默认参数。

例如Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：

>>> int('123')
123
>>> int('123', 8)
83
int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。

可见，函数的默认参数的作用是简化调用，你只需要把必须的参数传进去。但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。

我们来定义一个计算 x 的N次方的函数:

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
假设计算平方的次数最多，我们就可以把 n 的默认值设定为 2：

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
这样一来，计算平方就不需要传入两个参数了：

>>> power(5)
25
由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：

# OK:
def fn1(a, b=1, c=2):
    pass
# Error:
def fn2(a=1, b):
    pass
'''