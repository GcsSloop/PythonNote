#coding=utf-8
#author: sloop
'''
任务
请设计一个dict，可以根据分数来查找名字，已知成绩如下：

Adam: 95,

Lisa: 85,

Bart: 59.
'''

d = {
    95:'Adam',
    85:'Lisa',
    59:'Bart'
}
print d

'''
dict的特点
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，key不能重复。

dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
当我们试图打印这个dict时：

>>> print d
{'Lisa': 85, 'Adam': 95, 'Bart': 59}
打印的顺序不一定是我们创建时的顺序，而且，不同的机器打印的顺序都可能不同，这说明dict内部是无序的，不能用dict存储有序的集合。

dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

可以试试用list作为key时会报什么样的错误。

不可变这个限制仅作用于key，value是否可变无所谓：

{
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
最常用的key还是字符串，因为用起来最方便。
'''