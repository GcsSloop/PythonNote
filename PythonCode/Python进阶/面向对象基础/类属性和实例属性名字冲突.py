#coding=utf-8
#author: sloop
'''
任务
请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。
'''

class Person(object):
    __count = 0

    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

print Person.__count

'''
类属性和实例属性名字冲突怎么办
修改类属性会导致所有实例访问到的类属性全部都受影响，但是，如果在实例变量上修改类属性会发生什么问题呢？

class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address

p1.address = 'China'
print 'p1.address = ' + p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
结果如下：

Person.address = Earth
p1.address = China
Person.address = Earth
p2.address = Earth
我们发现，在设置了 p1.address = 'China' 后，p1访问 address 确实变成了 'China'，但是，Person.address和p2.address仍然是'Earch'，怎么回事？

原因是 p1.address = 'China'并没有改变 Person 的 address，而是给 p1这个实例绑定了实例属性address ，对p1来说，它有一个实例属性address（值是'China'），而它所属的类Person也有一个类属性address，所以:

访问 p1.address 时，优先查找实例属性，返回'China'。

访问 p2.address 时，p2没有实例属性address，但是有类属性address，因此返回'Earth'。

可见，当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。

当我们把 p1 的 address 实例属性删除后，访问 p1.address 就又返回类属性的值 'Earth'了：

del p1.address
print p1.address
# => Earth
可见，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。
'''