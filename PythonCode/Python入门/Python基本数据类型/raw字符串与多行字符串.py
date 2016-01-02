#coding=utf-8
"""
任务
请把下面的字符串用r'''...'''的形式改写，并用print打印出来：
'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
"""
# 代码
print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''


"""
raw字符串与多行字符串
如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了。例如：

r'\(~_~)/ \(~_~)/'
但是r'...'表示法不能表示多行字符串，也不能表示包含'和 "的字符串（为什么？）

如果要表示多行字符串，可以用'''...'''表示：

'''Line 1
Line 2
Line 3'''
上面这个字符串的表示方法和下面的是完全一样的：

'Line 1\nLine 2\nLine 3'
还可以在多行字符串前面添加 r ，把这个多行字符串也变成一个raw字符串：

r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
"""