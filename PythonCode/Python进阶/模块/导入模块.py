#coding=utf-8
#author: sloop
'''
任务
Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。

注意: 
1. 由于运行环境是平台服务器，所以测试的也是服务器中的文件夹和文件，该服务器上有/data/webroot/resource/python文件夹和/data/webroot/resource/python/test.txt文件，大家可以测试下。
2. 当然，大家可以在本机上测试是否存在相应的文件夹和文件。

import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')
'''

import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')

'''
注意到os.path模块可以以若干种方式导入：

import os
import os.path
from os import path
from os.path import isdir, isfile
每一种方式调用 isdir 和 isfile 都有所不同。

参考代码:

import os
print os.path.isdir(r'/data/webroot/resource/python')
print os.path.isfile(r'/data/webroot/resource/python/test.txt')
'''

'''
导入模块
要使用一个模块，我们必须首先导入该模块。Python使用import语句导入一个模块。例如，导入系统自带的模块 math：

import math
你可以认为math就是一个指向已导入模块的变量，通过该变量，我们可以访问math模块中所定义的所有公开的函数、变量和类：

>>> math.pow(2, 0.5) # pow是函数
1.4142135623730951

>>> math.pi # pi是变量
3.141592653589793
如果我们只希望导入用到的math模块的某几个函数，而不是所有函数，可以用下面的语句：

from math import pow, sin, log
这样，可以直接引用 pow, sin, log 这3个函数，但math的其他函数没有导入进来：

>>> pow(2, 10)
1024.0
>>> sin(3.14)
0.0015926529164868282
如果遇到名字冲突怎么办？比如math模块有一个log函数，logging模块也有一个log函数，如果同时使用，如何解决名字冲突？

如果使用import导入模块名，由于必须通过模块名引用函数名，因此不存在冲突：

import math, logging
print math.log(10)   # 调用的是math的log函数
logging.log(10, 'something')   # 调用的是logging的log函数
如果使用 from...import 导入 log 函数，势必引起冲突。这时，可以给函数起个“别名”来避免冲突：

from math import log
from logging import log as logger   # logging的log现在变成了logger
print log(10)   # 调用的是math的log
logger(10, 'import from logging')   # 调用的是logging的log
'''