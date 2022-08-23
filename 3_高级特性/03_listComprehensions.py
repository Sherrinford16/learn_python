# 列表生成式即List Comprehensions，是python内置的非常简单却强大的可以用来创建list的生成式。
# 举例：如果要生成一list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list([range(1, 11)])
list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
newList = []
for num in range(1, 11):
    newList.append(num * num)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面但list：
[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# 还可以使用两层循环，生成全排列
[m + n for m in 'ABC' for n in '123']
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# 三层和三层以上的循环就很少用到了。
# 运用列表生成式，可以写出非常简介的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os  # 导入os模块

[d for d in os.listdir('.')]
print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
# ['03_listComprehensions.py', '02_iteration.py', 'The-zen-of-python.py', '01_slice.py']

# for循环其实可以同时使用两个甚至多个变量，比如dict的item()可以同时迭代key和value：
d1 = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d1.items():
    print(k, '=', v)
# x = A
# y = B
# z = C

# 因此，列表生成式也可以使用两个变量来生成list：
[k + '=' + v for k, v in d1.items()]
# ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写：
newList1 = ['See', 'You', 'Space', 'Cowboy']
a = [s.lower() for s in newList1]
# ['see', 'you', 'space', 'cowboy']

# 使用列表生成式的时候，if...else的用法需要注意！！
[x for x in range(1, 11) if x % 2 == 0]  # 可以正常输出偶数

"""
# 但是，不能在最后的if加上else：
[x for x in range(1, 11) if x % 2 == 0 else 0]

# [x for x in range(1, 11) if x % 2 == 0 else 0]
#                                            ^
# SyntaxError: invalid syntax
"""
# 这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？（带上else总会得到一个结果，无法起到筛选的作用

"""
# 但，把if写在for前面必须加else，否则报错：
[x if x % 2 == 0 for x in range(1, 11)]

# [x if x % 2 == 0 for x in range(1, 11)]
#                      ^
# SyntaxError: invalid syntax
"""
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：
# x if x % == 0，它因为缺少else而无法根据x计算出结果，所以必须加上else：
[x if x % 2 == 0 else -x for x in range(1, 11)]
# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 上述for前面的表达式 x if x % 2 == 0 else -x 才能根据x计算出确定的结果。
"""# 可见，在一个列表生成式中，for前面的if...else是表达式，而for后面的if是过滤条件，不能带else"""

# 练习：如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
newList2 = ['See', 'You', 'Space', 'Cowboy', 16]
"""
[s.lower() for s in newList2]
AttributeError: 'int' object has no attribute 'lower
'"""

# 使用内建的isinstance函数可以判断一个变量是不是字符串：
x = 'abc'
y = 123
isinstance(x, str)
# True
isinstance(y, str)
# False
isinstance(y, int)
# True

# 修改列表生成表达式，通过添加if语句保证列表生成表达式能正确执行：
L2 = [s.lower() for s in newList2 if isinstance(s, str)]
print(L2)
if L2 == ['see', 'you', 'space', 'cowboy']:
    print('测试通过!')
else:
    print('测试失败!')