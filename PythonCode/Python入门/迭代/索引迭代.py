#coding=utf-8
#author: sloop
'''
任务
zip()函数可以把两个 list 变成一个 list：

>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。

提示：考虑使用zip()函数和range()函数
'''

#代码
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1,len(L)+1),L):
    print index, '-', name

'''
索引迭代
Python中，迭代永远是取出元素本身，而非元素的索引。

对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？

方法是使用 enumerate() 函数：

>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> for index, name in enumerate(L):
...     print index, '-', name
... 
0 - Adam
1 - Lisa
2 - Bart
3 - Paul
使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：

['Adam', 'Lisa', 'Bart', 'Paul']
变成了类似：

[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
因此，迭代的每一个元素实际上是一个tuple：

for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name
如果我们知道每个tuple元素都包含两个元素，for循环又可以进一步简写为：

for index, name in enumerate(L):
    print index, '-', name
这样不但代码更简单，而且还少了两条赋值语句。

可见，索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身。
'''