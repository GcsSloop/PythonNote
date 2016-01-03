#coding=utf-8
#author: sloop

import functools
'''
打印log函数
允许参数: 字符串
'''
def log(perfix):
    def log_decorator(f):
        @functools.wraps(f) #完成函数自动复制功能，防止改变函数原有的内容
        def wrapper(*args, **kw):
            print '[%s] %s...' %(perfix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
print test.__name__