#coding=utf-8
#author: sloop
'''
任务
请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
'''

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)


'''
__cmp__
对 int、str 等内置数据类型排序时，Python的 sorted() 按照默认的比较函数 cmp 排序，但是，如果对一组 Student 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()：

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
上述 Student 类实现了__cmp__()方法，__cmp__用实例自身self和传入的实例 s 进行比较，如果 self 应该排在前面，就返回 -1，如果 s 应该排在前面，就返回1，如果两者相当，返回 0。

Student类实现了按name进行排序：

>>> L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
>>> print sorted(L)
[(Alice: 77), (Bob: 88), (Tim: 99)]
注意: 如果list不仅仅包含 Student 类，则 __cmp__ 可能会报错：

L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(L)
请思考如何解决。
'''