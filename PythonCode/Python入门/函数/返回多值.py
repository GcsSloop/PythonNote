#coding=utf-8
#author: sloop

'''
任务
一元二次方程的定义是：ax² + bx + c = 0

请编写一个函数，返回一元二次方程的两个解。

注意：Python的math包提供了sqrt()函数用于计算平方根。
请参考求根公式：x = (-b±√(b²-4ac)) / 2a
'''

import math

def quadratic_equation(a, b, c):
    t = b*b - 4*a*c
    if t < 0:
        return
    else:
        x1 = ( -b+math.sqrt(t) ) / (2*a)
        x2 = ( -b-math.sqrt(t) ) / (2*a)
        return x1, x2
        
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

'''
返回多值
函数可以返回多个值吗？答案是肯定的。

比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：

# math包提供了sin()和 cos()函数，我们先用import引用它：

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
这样我们就可以同时获得返回值：

>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print x, y
151.961524227 70.0
但其实这只是一种假象，Python函数返回的仍然是单一值：

>>> r = move(100, 100, 60, math.pi / 6)
>>> print r
(151.96152422706632, 70.0)
用print打印返回结果，原来返回值是一个tuple！

但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''