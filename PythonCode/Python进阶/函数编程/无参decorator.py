#coding=utf-8
#author: sloop
'''
任务
请编写一个@performance，它可以打印出函数调用的时间。
'''

import time

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' %(f.__name__,(t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    for i in range(0,1000):
        x = i
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

'''
编写无参数decorator
Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。

使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。

考察一个@log的定义：

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
对于阶乘函数，@log工作得很好：

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
结果：

call factorial()...
3628800
但是，对于参数不是一个的函数，调用将报错：

@log
def add(x, y):
    return x + y
print add(1, 2)
结果：

Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print add(1,2)
TypeError: fn() takes exactly 1 argument (2 given)
因为 add() 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。

要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：

def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
现在，对于任意函数，@log 都能正常工作。
'''