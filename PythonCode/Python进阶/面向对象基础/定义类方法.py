#coding=utf-8
#author: sloop
'''
任务
如果将类属性 count 改为私有属性__count，则外部无法读取__score，但可以通过一个类方法获取，请编写类方法获得__count值。
'''

class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count
    
    def __init__(self, name):
        self.name = name
        Person.__count += 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()

'''
定义类方法
和属性类似，方法也分实例方法和类方法。

在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

要在class中定义类方法，需要这么写：

class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。

因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。
'''