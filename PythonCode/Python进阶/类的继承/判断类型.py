#coding=utf-8
#author: sloop
'''
任务
请根据继承链的类型转换，依次思考 t 是否是 Person，Student，Teacher，object 类型，并使用isinstance()判断来验证您的答案。
'''

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)

'''
判断类型
函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型。

假设有如下的 Person、Student 和 Teacher 的定义及继承关系如下：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
当我们拿到变量 p、s、t 时，可以使用 isinstance 判断类型：

>>> isinstance(p, Person)
True    # p是Person类型
>>> isinstance(p, Student)
False   # p不是Student类型
>>> isinstance(p, Teacher)
False   # p不是Teacher类型
这说明在继承链上，一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法。

我们再考察 s ：

>>> isinstance(s, Person)
True    # s是Person类型
>>> isinstance(s, Student)
True    # s是Student类型
>>> isinstance(s, Teacher)
False   # s不是Teacher类型
s 是Student类型，不是Teacher类型，这很容易理解。但是，s 也是Person类型，因为Student继承自Person，虽然它比Person多了一些属性和方法，但是，把 s 看成Person的实例也是可以的。

这说明在一条继承链上，一个实例可以看成它本身的类型，也可以看成它父类的类型。
'''