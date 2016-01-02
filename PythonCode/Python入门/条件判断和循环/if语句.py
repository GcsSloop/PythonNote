#coding=utf-8
#author: sloop
'''
任务
如果成绩达到60分或以上，视为passed。

假设Bart同学的分数是75，请用if语句判断是否能打印出 passed:
'''

#代码
score = 75
if score>=60:
    print 'passed'

'''
if语句
计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，可以用if语句实现：

age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'
注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。

缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。

注意: if 语句后接表达式，然后用:表示代码块开始。

如果你在Python交互环境下敲代码，还要特别留意缩进，并且退出缩进需要多敲一行回车：

>>> age = 20
>>> if age >= 18:
...     print 'your age is', age
...     print 'adult'
...
your age is 20
adult
'''