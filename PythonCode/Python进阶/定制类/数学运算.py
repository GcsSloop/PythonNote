#coding=utf-8
#author: sloop
# 分数运算
'''
任务
Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。

提示：
减法运算：__sub__
乘法运算：__mul__
除法运算：__div__
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p*r.q - r.p*self.q, self.q*r.q)

    def __mul__(self, r):
        return Rational(self.p*r.p, self.q*r.q)

    def __div__(self, r):
        return Rational(self.p*r.q, self.q*r.p)

    def __str__(self):
        g = gcd(self.p, self.q) 
        return '%s/%s' %(self.p/g, self.q/g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

'''
数学运算
Python 提供的基本数据类型 int、float 可以做整数和浮点的四则运算以及乘方等运算。

但是，四则运算不局限于int和float，还可以是有理数、矩阵等。

要表示有理数，可以用一个Rational类来表示：

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
p、q 都是整数，表示有理数 p/q。

如果要让Rational进行+运算，需要正确实现__add__：

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self):
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__
现在可以试试有理数加法：

>>> r1 = Rational(1, 3)
>>> r2 = Rational(1, 2)
>>> print r1 + r2
5/6
'''