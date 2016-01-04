#coding=utf-8
#author: sloop
'''
任务
斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。

请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
'''

class Fib(object):

    def __init__(self, num):
        a,b,L = 0,1,[]
        for n in range(num):
            L.append(a)
            a,b = b, a+b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)
    
    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)

'''
__len__
如果一个类表现得像一个list，要获取有多少个元素，就得用 len() 函数。

要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数。

例如，我们写一个 Students 类，把名字传进去：

class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
只要正确实现了__len__()方法，就可以用len()函数返回Students实例的“长度”：

>>> ss = Students('Bob', 'Alice', 'Tim')
>>> print len(ss)
3
'''