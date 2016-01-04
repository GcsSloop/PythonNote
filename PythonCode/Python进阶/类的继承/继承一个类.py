#coding=utf-8
#author: sloop
'''
任务
请参考 Student 类，编写一个 Teacher类，也继承自 Person。
'''

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name,gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course

'''
继承一个类
如果已经定义了Person类，需要定义新的Student和Teacher类时，可以直接从Person类继承：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
定义Student类时，只需要把额外的属性加上，例如score：

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
一定要用 super(Student, self).__init__(name, gender) 去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。

函数super(Student, self)将返回当前类继承的父类，即 Person ，然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）。
'''