#coding=utf-8
#author: sloop
'''
任务
请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
'''

#代码
def square_of_sum(L):
    return sum(i*i for i in L)

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])


'''
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum
'''

'''
编写函数
在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

我们以自定义一个求绝对值的 my_abs 函数为例：

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。

return None可以简写为return。
'''