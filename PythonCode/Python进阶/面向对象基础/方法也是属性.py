#coding=utf-8
#author: sloop
'''
任务
由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，大家看看下面代码的运行结果，请想一想 p1.get_grade 为什么是函数而不是方法：
'''

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()


'''
方法也是属性
我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# => <bound method Person.get_grade of <__main__.Person object at 0x109e58510>>
print p1.get_grade()
# => A
也就是说，p1.get_grade 返回的是一个函数对象，但这个函数是一个绑定到实例的函数，p1.get_grade() 才是方法调用。

因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数变为一个方法：

import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade
给一个实例动态添加方法并不常见，直接在class中定义要更直观。
'''