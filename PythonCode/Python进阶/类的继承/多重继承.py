#coding=utf-8
#author: sloop
'''
任务
+-Person
  +- Student
  +- Teacher

是一类继承树；

+- SkillMixin
   +- BasketballMixin
   +- FootballMixin

是一类继承树。

通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。
'''

class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin):
    pass

class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()

'''
多重继承
除了从一个父类继承外，Python允许从多个父类继承，称为多重继承。

多重继承的继承链就不是一棵树了，它像这样：

class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
看下图:



像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过 super()调用__init__()方法时，A 虽然被继承了两次，但__init__()只调用一次：

>>> d = D('d')
init A...
init C...
init B...
init D...
多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。

举个例子，Python的网络服务器有TCPServer、UDPServer、UnixStreamServer、UnixDatagramServer，而服务器运行模式有 多进程ForkingMixin 和 多线程ThreadingMixin两种。

要创建多进程模式的 TCPServer：

class MyTCPServer(TCPServer, ForkingMixin)
    pass
要创建多线程模式的 UDPServer：

class MyUDPServer(UDPServer, ThreadingMixin):
    pass
如果没有多重继承，要实现上述所有可能的组合需要 4x2=8 个子类。
'''