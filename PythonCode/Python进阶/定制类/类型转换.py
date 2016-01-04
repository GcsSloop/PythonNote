#coding=utf-8
#author: sloop
'''
任务
请继续完善Rational，使之可以转型为float。
'''

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q

print float(Rational(7, 2))
print float(Rational(1, 3))

'''
类型转换
Rational类实现了有理数运算，但是，如果要把结果转为 int 或 float 怎么办？

考察整数和浮点数的转换：

>>> int(12.34)
12
>>> float(12)
12.0
如果要把 Rational 转为 int，应该使用：

r = Rational(12, 5)
n = int(r)
要让int()函数正常工作，只需要实现特殊方法__int__():

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
结果如下：

>>> print int(Rational(7, 2))
3
>>> print int(Rational(1, 3))
0
同理，要让float()函数正常工作，只需要实现特殊方法__float__()。
'''