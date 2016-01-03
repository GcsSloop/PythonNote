#coding=utf-8
#author: sloop
'''
任务
请练习定义Person类，并创建出两个实例，打印实例，再比较两个实例是否相等。
'''

class Person(object):
    pass

xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong
print xiaoming == xiaohong

'''
定义类并创建实例
在Python中，类通过 class 关键字定义。以 Person 为例，定义一个Person类如下：

class Person(object):
    pass
按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。

有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用 类名+()，类似函数调用的形式创建：

xiaoming = Person()
xiaohong = Person()
'''