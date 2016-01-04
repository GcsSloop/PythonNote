#coding=utf-8
#author: sloop
'''
任务
请给Student 类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>：

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
'''

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

s = Student('Bob', 'male', 88)
print s

'''
__str__和__repr__
如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
现在，在交互式命令行下用 print 试试：

>>> p = Person('Bob', 'male')
>>> print p
(Person: Bob, male)
但是，如果直接敲变量 p：

>>> p
<main.Person object at 0x10c941890>
似乎__str__() 不会被调用。

因为 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。

有一个偷懒的定义__repr__的方法：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
'''