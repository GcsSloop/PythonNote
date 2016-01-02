#coding=utf-8
#input code
print 'hello, python.'
print 'hello,','python.'

'''
print语句
print语句可以向屏幕上输出指定的文字。比如输出'hello, world'，用代码实现如下：

>>> print 'hello, world'
注意：

1.当我们在Python交互式环境下编写代码时，>>>是Python解释器的提示符，不是代码的一部分。

2.当我们在文本编辑器中编写代码时，千万不要自己添加 >>>。

print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：

>>> print 'The quick brown fox', 'jumps over', 'the lazy dog'
The quick brown fox jumps over the lazy dog
print会依次打印每个字符串，遇到逗号“,”会输出一个空格.

print也可以打印整数，或者计算结果：

>>> print 300
300    #运行结果
>>> print 100 + 200
300    #运行结果
因此，我们可以把计算100 + 200的结果打印得更漂亮一点：

>>> print '100 + 200 =', 100 + 200
100 + 200 = 300     #运行结果
注意: 对于100 + 200，Python解释器自动计算出结果300，但是，'100 + 200 ='是字符串而非数学公式，Python把它视为字符串，请自行解释上述打印结果。

任务
请用两种方式打印出 hello, python.
'''
