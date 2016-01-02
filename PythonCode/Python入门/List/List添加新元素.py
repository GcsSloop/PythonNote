#coding=utf-8
#author: sloop

'''
任务
假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
'''

#代码
L = ['Adam', 'Lisa', 'Bart']
L.insert(2,'Paul')
print L

'''
添加新元素
现在，班里有3名同学：

>>> L = ['Adam', 'Lisa', 'Bart']
今天，班里转来一名新同学 Paul，如何把新同学添加到现有的 list 中呢？

第一个办法是用 list 的 append() 方法，把新同学追加到 list 的末尾：

>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.append('Paul')
>>> print L
['Adam', 'Lisa', 'Bart', 'Paul']
append()总是把新的元素添加到 list 的尾部。

如果 Paul 同学表示自己总是考满分，要求添加到第一的位置，怎么办？

方法是用list的 insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素：

>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.insert(0, 'Paul')
>>> print L
['Paul', 'Adam', 'Lisa', 'Bart']
L.insert(0, 'Paul') 的意思是，'Paul'将被添加到索引为 0 的位置上（也就是第一个），而原来索引为 0 的Adam同学，以及后面的所有同学，都自动向后移动一位。
'''
