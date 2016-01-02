#coding=utf-8
'''
任务
请将下面两行内容用Python的字符串表示并打印出来：
　　Python was started in 1989 by "Guido".
　　Python is free and easy to learn.
'''
s = 'Python was started in 1989 by "Guido".\nPython is free and easy to learn.'
print s

'''
定义字符串
前面我们讲解了什么是字符串。字符串可以用''或者""括起来表示。

如果字符串本身包含'怎么办？比如我们要表示字符串 I'm OK ，这时，可以用" "括起来表示：

"I'm OK"
类似的，如果字符串包含"，我们就可以用' '括起来表示：

'Learn "Python" in imooc'
如果字符串既包含'又包含"怎么办？

这个时候，就需要对字符串的某些特殊字符进行“转义”，Python字符串用\进行转义。

要表示字符串 Bob said "I'm OK".
由于 ' 和 " 会引起歧义，因此，我们在它前面插入一个\表示这是一个普通字符，不代表字符串的起始，因此，这个字符串又可以表示为

'Bob said \"I\'m OK\".'
注意：转义字符 \ 不计入字符串的内容中。

常用的转义字符还有：

\n 表示换行
\t 表示一个制表符
\\ 表示 \ 字符本身
'''