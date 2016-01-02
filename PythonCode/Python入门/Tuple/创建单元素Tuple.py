#coding=utf-8
#author: sloop

'''
任务
请指出右边编辑器中代码为什么没有创建出包含一个学生的 tuple：

t = ('Adam')

print t

请修改代码，确保 t 是一个tuple。
'''

#代码
t = ('Adam',)
print t

'''
创建单元素tuple
tuple和list一样，可以包含 0 个、1个和任意多个元素。

包含多个元素的 tuple，前面我们已经创建过了。

包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示：

>>> t = ()
>>> print t
()
创建包含1个元素的 tuple 呢？来试试：

>>> t = (1)
>>> print t
1
好像哪里不对！t 不是 tuple ，而是整数1。为什么呢？

因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1。

正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义：

>>> t = (1,)
>>> print t
(1,)
Python在打印单元素tuple时，也自动添加了一个“,”，为了更明确地告诉你这是一个tuple。

多元素 tuple 加不加这个额外的“,”效果是一样的：

>>> t = (1, 2, 3,)
>>> print t
(1, 2, 3)
'''