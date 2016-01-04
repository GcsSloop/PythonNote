#coding=utf-8
#author: sloop
'''
任务
对于Person类的定义：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，请修改 Person 的 __init__()定 义，完成该功能。
'''

class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self,k,v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

'''
获取对象信息
拿到一个变量，除了用 isinstance() 判断它是否是某种类型的实例外，还有没有别的方法获取到更多的信息呢？

例如，已有定义：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name
首先可以用 type() 函数获取变量的类型，它返回一个 Type 对象：

>>> type(123)
<type 'int'>
>>> s = Student('Bob', 'Male', 88)
>>> type(s)
<class '__main__.Student'>
其次，可以用 dir() 函数获取变量的所有属性：

>>> dir(123)   # 整数也有很多属性...
['__abs__', '__add__', '__and__', '__class__', '__cmp__', ...]

>>> dir(s)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'gender', 'name', 'score', 'whoAmI']
对于实例变量，dir()返回所有实例属性，包括`__class__`这类有特殊意义的属性。注意到方法`whoAmI`也是 s 的一个属性。

如何去掉`__xxx__`这类的特殊属性，只保留我们自己定义的属性？回顾一下filter()函数的用法。

dir()返回的属性是字符串列表，如果已知一个属性名称，要获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数了：

>>> getattr(s, 'name')  # 获取name属性
'Bob'

>>> setattr(s, 'name', 'Adam')  # 设置新的name属性

>>> s.name
'Adam'

>>> getattr(s, 'age')  # 获取age属性，但是属性不存在，报错：
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'

>>> getattr(s, 'age', 20)  # 获取age属性，如果属性不存在，就返回默认值20：
20
'''