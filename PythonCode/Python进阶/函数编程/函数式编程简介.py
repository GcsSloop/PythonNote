#coding=utf-8
#author: sloop

'''
函数式编程
python不是纯函数式编程，允许有变量，
支持高阶函数，
支持闭包
'''

f = abs             #将绝对值函数赋值给f 则f的功能就和abs相同了
print f(-12)        #调用函数

abs = len           #将求长度函数赋值给abs函数, 则abs不再具有求绝对值的功能，变成了求长度函数
#abs(-2)            #由于改变了函数功能，这样调用会出错
print abs([1,2,3])  #计算list的长度