#coding=utf-8
#author: sloop
'''
任务
注意右边编辑器代码中 list 如下：

L = ['Adam', 'Lisa', 'Paul', 'Bart']

Paul的索引是2，Bart的索引是3，如果我们要把Paul和Bart都删掉，请解释下面的代码为什么不能正确运行：

L.pop(2)
L.pop(3)

怎样调整代码可以把Paul和Bart都正确删除掉？
'''

#代码
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L

'''
从list删除元素
Paul同学刚来几天又要转走了，那么我们怎么把Paul 从现有的list中删除呢？

如果Paul同学排在最后一个，我们可以用list的pop()方法删除：

>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L.pop()
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
pop()方法总是删掉list的最后一个元素，并且它还返回这个元素，所以我们执行 L.pop() 后，会打印出 'Paul'。

如果Paul同学不是排在最后一个怎么办？比如Paul同学排在第三：

>>> L = ['Adam', 'Lisa', 'Paul', 'Bart']
要把Paul踢出list，我们就必须先定位Paul的位置。由于Paul的索引是2，因此，用 pop(2)把Paul删掉：

>>> L.pop(2)
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
'''