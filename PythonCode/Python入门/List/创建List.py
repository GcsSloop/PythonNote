#coding=utf-8
'''
任务
假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
'''

#代码；
L = ['adam', 95.5, 'lisa', 85, 'bart', 59]
print L

'''
创建list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个list表示：

>>> ['Michael', 'Bob', 'Tracy']
['Michael', 'Bob', 'Tracy']
list是数学意义上的有序集合，也就是说，list中的元素是按照顺序排列的。

构造list非常简单，按照上面的代码，直接用 [ ] 把list的所有元素都括起来，就是一个list对象。通常，我们会把list赋值给一个变量，这样，就可以通过变量来引用list：

>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates # 打印classmates变量的内容
['Michael', 'Bob', 'Tracy']
由于Python是动态语言，所以list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据：

>>> L = ['Michael', 100, True]
一个元素也没有的list，就是空list：

>>> empty_list = []
'''