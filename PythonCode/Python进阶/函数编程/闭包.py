#coding=utf-8
#author: sloop
'''
任务
返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
'''

def count():
    fs = []
    for i in range(1, 4):
        def f(x = i):
            return x*x
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

'''
考察下面的函数 f:

def f(j):
    def g():
        return j*j
    return g
它可以正确地返回一个闭包g，g所引用的变量j不是循环变量，因此将正常执行。

在count函数的循环内部，如果借助f函数，就可以避免引用循环变量i。

参考代码:

def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

'''

'''
闭包
在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问：

def g():
    print 'g()...'

def f():
    print 'f()...'
    return g
将 g 的定义移入函数 f 内部，防止其他代码调用 g：

def f():
    print 'f()...'
    def g():
        print 'g()...'
    return g
但是，考察上一小节定义的 calc_sum 函数：

def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
注意: 发现没法把 lazy_sum 移到 calc_sum 的外部，因为它引用了 calc_sum 的参数 lst。

像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。

闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：

# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果全部都是 9（请自己动手验证）。

原因就是当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，当 f1 被调用时：

>>> f1()
9     # 因为f1现在才计算i*i，但现在i的值已经变为3
因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''