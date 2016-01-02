#coding=utf-8
#author: sloop
'''
任务
字符串有个方法 upper() 可以把字符变成大写字母：

>>> 'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。

提示：利用切片操作简化字符串操作。
'''

#代码
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

'''
对字符串切片
字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[-3:]
'EFG'
>>> 'ABCDEFG'[::2]
'ACEG'
在很多编程语言中，针对字符串提供了很多各种截取函数，其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
'''