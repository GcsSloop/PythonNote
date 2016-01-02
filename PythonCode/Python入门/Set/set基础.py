#coding=utf-8
#author: sloop

'''
任务
请用set表示班里的4位同学：

Adam, Lisa, Bart, Paul
'''

#代码
s = set(['Adam','Lisa','Bart','Paul'])
print s

'''
什么是set
dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。

有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。

set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：

>>> s = set(['A', 'B', 'C'])
可以查看 set 的内容：

>>> print s
set(['A', 'C', 'B'])
请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list 会怎么样呢？

>>> s = set(['A', 'B', 'C', 'C'])
>>> print s
set(['A', 'C', 'B'])
>>> len(s)
3
结果显示，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。
'''