#coding=utf-8
#author: sloop

'''
任务
创建一个tuple，顺序包含0 - 9这10个数。
'''

#代码
t = (0,1,2,3,4,5,6,7,8,9)
print t

'''
创建tuple
tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

同样是表示班里同学的名称，用tuple表示如下：

>>> t = ('Adam', 'Lisa', 'Bart')
创建tuple和创建list唯一不同之处是用( )替代了[ ]。

现在，这个 t 就不能改变了，tuple没有 append()方法，也没有insert()和pop()方法。所以，新同学没法直接往 tuple 中添加，老同学想退出 tuple 也不行。

获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素，不信可以试试：

>>> t[0] = 'Paul'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''