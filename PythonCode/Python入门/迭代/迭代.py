#coding=utf-8
#author: sloop
'''
任务
请用for循环迭代数列 1-100 并打印出7的倍数。
'''

#代码
for i in range(1,101)[6::7]:
    print i

'''
什么是迭代
在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。

在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：

for (i=0; i<list.length; i++) {
    n = list[i];
}
可以看出，Python的for循环抽象程度要高于Java的for循环。

因为 Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。

因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。

注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict
而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。

迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。
'''