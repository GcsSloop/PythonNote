#coding=utf-8
#author: sloop
'''
任务
请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
'''

class Person(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

'''
创建类属性
类是模板，而实例则是根据类创建的对象。

绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

定义类属性可以直接在 class 中定义：

class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：

print Person.address
# => Earth
对一个实例调用类的属性也是可以访问的，所有实例都可以访问到它所属的类的属性：

p1 = Person('Bob')
p2 = Person('Alice')
print p1.address
# => Earth
print p2.address
# => Earth
由于Python是动态语言，类属性也是可以动态添加和修改的：

Person.address = 'China'
print p1.address
# => 'China'
print p2.address
# => 'China'
因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了。
'''