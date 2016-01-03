#coding=utf-8
#author: sloop
'''
任务
请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。
'''

class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score > 80:
            return 'A'
        if self.__score >= 60:
            return 'B'
        return 'C'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

'''
定义实例方法
一个实例的私有属性就是以__开头的属性，无法被外部访问，那这些属性定义有什么用？

虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。

实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：

class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
get_name(self) 就是一个实例方法，它的第一个参数是self。__init__(self, name)其实也可看做是一个特殊的实例方法。

调用实例方法必须在实例上调用：

p1 = Person('Bob')
print p1.get_name()  # self不需要显式传入
# => Bob
在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度
'''