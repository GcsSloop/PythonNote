#coding=utf-8
#author: sloop
'''
任务
Python提供了open()函数来打开一个磁盘文件，并返回 File 对象。File对象有一个read()方法可以读取文件内容：

例如，从文件读取内容并解析为JSON结果：

import json
f = open('/path/to/file.json', 'r')
print json.load(f)
由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。

请尝试编写一个File-like Object，把一个字符串 r'["Tim", "Bob", "Alice"]'包装成 File-like Object 并由 json.load() 解析。
'''

import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)

'''
多态
类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Person 派生出 Student和Teacher ，并都写了一个 whoAmI() 方法：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
在一个函数中，如果我们接收一个变量 x，则无论该 x 是 Person、Student还是 Teacher，都可以正确打印出结果：

def who_am_i(x):
    print x.whoAmI()

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)
运行结果：

I am a Person, my name is Tim
I am a Student, my name is Bob
I am a Teacher, my name is Alice
这种行为称为多态。也就是说，方法调用将作用在 x 的实际类型上。s 是Student类型，它实际上拥有自己的 whoAmI()方法以及从 Person继承的 whoAmI方法，但调用 s.whoAmI()总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。

由于Python是动态语言，所以，传递给函数 who_am_i(x)的参数 x 不一定是 Person 或 Person 的子类型。任何数据类型的实例都可以，只要它有一个whoAmI()的方法即可：

class Book(object):
    def whoAmI(self):
        return 'I am a book'
这是动态语言和静态语言（例如Java）最大的差别之一。动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。
'''