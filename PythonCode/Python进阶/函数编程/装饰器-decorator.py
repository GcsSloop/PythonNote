#coding=utf-8
#author: sloop
'''
装饰器模式
在不改变原函数的基础上利用高阶函数增加功能
使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。
'''
# 装饰器 log
def log(f):
    def fn(*args, **kw):    #使用可变参数
        print 'call '+f.__name__+'()...'
        return f(*args, **kw)
    return fn

# 阶乘
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

print factorial(10)

@log
def add(x,y):
    return x+y

print add(1,2)

'''
def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print 'call '+f.__name__+'()'
        return f(x)
    return fn

g = new_fn(f1)
print g(2)
'''