#coding=utf-8
#author: sloop
'''
任务
上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
'''

import time

def performance(unit):
    def performance_dec(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return performance_dec

@performance('ms')
def factorial(n):
    for i in range(1, 1000):
        print i
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

'''
编写带参数decorator
考察上一节的 @log 装饰器：

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
发现对于被装饰的函数，log打印的语句是不能变的（除了函数名）。

如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数，类似这样：

@log('DEBUG')
def my_func():
    pass
把上面的定义翻译成高阶函数的调用，就是：

my_func = log('DEBUG')(my_func)
上面的语句看上去还是比较绕，再展开一下：

log_decorator = log('DEBUG')
my_func = log_decorator(my_func)
上面的语句又相当于：

log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
所以，带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：

def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
执行结果：

[DEBUG] test()...
None
对于这种3层嵌套的decorator定义，你可以先把它拆开：

# 标准decorator:
def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator

# 返回decorator:
def log(prefix):
    return log_decorator(f)
拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，最内层的wrapper引用了最外层的参数prefix，所以，把一个闭包拆成普通的函数调用会比较困难。不支持闭包的编程语言要实现同样的功能就需要更多的代码。
'''