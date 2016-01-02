#coding=utf-8
#author: sloop

'''
任务
三名同学的成绩可以用一个list表示：

L = [95.5, 85, 59]

请按照倒序索引分别打印出倒数第一、倒数第二、倒数第三、倒数第四的分数。
'''

#代码
L = [95.5, 85, 59]
print L[-1]
print L[-2]
print L[-3]
#print L[-4]	#越界异常

'''
倒序访问list
我们还是用一个list按分数从高到低表示出班里的3个同学：

>>> L = ['Adam', 'Lisa', 'Bart']
这时，老师说，请分数最低的同学站出来。

要写代码完成这个任务，我们可以先数一数这个 list，发现它包含3个元素，因此，最后一个元素的索引是2：

>>> print L[2]
Bart
有没有更简单的方法？

有！

Bart同学是最后一名，俗称倒数第一，所以，我们可以用 -1 这个索引来表示最后一个元素：

>>> print L[-1]
Bart
Bart同学表示躺枪。

类似的，倒数第二用 -2 表示，倒数第三用 -3 表示，倒数第四用 -4 表示：

>>> print L[-2]
Lisa
>>> print L[-3]
Adam
>>> print L[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
L[-4] 报错了，因为倒数第四不存在，一共只有3个元素。

使用倒序索引时，也要注意不要越界。
'''