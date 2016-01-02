#coding=utf-8
#author: sloop
'''
任务
三名同学的成绩可以用一个list表示：

L = [95.5, 85, 59]

请按照索引分别打印出第一名、第二名、第三名、第四名的分数。
'''

#代码
L = [95.5,85,59]
print L[0]
print L[1]
print L[2]
print L

'''
按照索引访问list
由于list是一个有序集合，所以，我们可以用一个list按分数从高到低表示出班里的3个同学：

>>> L = ['Adam', 'Lisa', 'Bart']
那我们如何从list中获取指定第 N 名的同学呢？方法是通过索引来获取list中的指定元素。

需要特别注意的是，索引从 0 开始，也就是说，第一个元素的索引是0，第二个元素的索引是1，以此类推。

因此，要打印第一名同学的名字，用 L[0]:

>>> print L[0]
Adam
要打印第二名同学的名字，用 L[1]:

>>> print L[1]
Lisa
要打印第三名同学的名字，用 L[2]:

>>> print L[2]
Bart
要打印第四名同学的名字，用 L[3]:

>>> print L[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
报错了！IndexError意思就是索引超出了范围，因为上面的list只有3个元素，有效的索引是 0，1，2。

所以，使用索引时，千万注意不要越界。
'''