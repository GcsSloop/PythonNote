#coding=utf-8
#author: sloop

'''
任务
请用 for 循环遍历如下的dict，打印出 name: score 来。

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
'''

#代码
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

print u'方式1--------------'
for a in d:
    print a ,":",d[a]

print u'方式2--------------'

for key,value in zip(d.keys(),d.values()):
    print("%s:%s" %(key,value))

print u'方式3--------------'

for k,v in d.items():
     print k,':',v
 

'''
遍历dict
由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。

直接使用for循环可以遍历 dict 的 key：

>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> for key in d:
...     print key
... 
Lisa
Adam
Bart
由于通过 key 可以获取对应的 value，因此，在循环体内，可以获取到value的值。
'''