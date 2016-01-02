#coding=utf-8
#author: sloop

'''
任务
班里的同学按照分数排名是这样的：

L = ['Adam', 'Lisa', 'Bart']

但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。

请通过对list的索引赋值，生成新的排名。
'''

#代码
L = ['Adam', 'Lisa', 'Bart']
L[0],L[-1]=L[-1],L[0]		#交换第一名和最后一名
print L

'''
替换元素
假设现在班里仍然是3名同学：

>>> L = ['Adam', 'Lisa', 'Bart']
现在，Bart同学要转学走了，碰巧来了一个Paul同学，要更新班级成员名单，我们可以先把Bart删掉，再把Paul添加进来。

另一个办法是直接用Paul把Bart给替换掉：

>>> L[2] = 'Paul'
>>> print L
L = ['Adam', 'Lisa', 'Paul']
对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。

由于Bart还可以用 -1 做索引，因此，下面的代码也可以完成同样的替换工作：

>>> L[-1] = 'Paul'
'''