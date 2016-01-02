#coding=utf-8
#author: sloop
'''
任务
在生成的表格中，对于没有及格的同学，请把分数标记为红色。

提示：红色可以用 <td style="color:red"> 实现。
'''

#代码
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>'% (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>'% (name, score) if score >=60 else '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
'''

'''
复杂表达式
使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。

假设有如下的dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格：

tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。

把打印出来的结果保存为一个html文件，就可以在浏览器中看到效果了：

<table border="1">
<tr><th>Name</th><th>Score</th><tr>
<tr><td>Lisa</td><td>85</td></tr>
<tr><td>Adam</td><td>95</td></tr>
<tr><td>Bart</td><td>59</td></tr>
</table>
'''