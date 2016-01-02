#coding=utf-8
#author: sloop
'''
任务
月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。

月份可以用字符串'Jan', 'Feb', ...表示。
'''

#代码
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'

'''
set的特点
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

最后，set存储的元素也是没有顺序的。

set的这些特点，可以应用在哪些地方呢？

星期一到星期日可以用字符串'MON', 'TUE', ... 'SUN'表示。

假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？

可以用 if 语句判断，但这样做非常繁琐：

x = '???' # 用户输入的字符串
if x!= 'MON' and x!= 'TUE' and x!= 'WED' ... and x!= 'SUN':
    print 'input error'
else:
    print 'input ok'
注意：if 语句中的...表示没有列出的其它星期名称，测试时，请输入完整。

如果事先创建好一个set，包含'MON' ~ 'SUN'：

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
再判断输入是否有效，只需要判断该字符串是否在set中：

x = '???' # 用户输入的字符串
if x in weekdays:
    print 'input ok'
else:
    print 'input error'
这样一来，代码就简单多了。
'''