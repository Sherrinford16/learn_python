# 迭代
"""
# 如果给定一个list或tuple，可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代。
# 在python代码中，迭代是通过for...in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如c代码：

for(i=0; i<length; i++){
    n = list[i];
}

# 可以看出，python的for循环抽象程度要高于C的for循环，因为python的for循环不仅可以用在list或tuple上，
# 还可以作用在其他可迭代对象上。

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标但，但是，只要是可迭代对象，无论有无下标，都可以迭代比如dict：

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# a
# c
# b

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()
# 如果要同时迭代key和value，可以用for k, v in d.items()

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABC':
    print(ch)
# A
# B
# C

# 所以当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

from collections.abc import Iterable
isinstance('abc', Iterable)  # str是否可迭代
# True
isinstance(['elementA', 'elementB', 'elementC'], Iterable)  # list是否可迭代
# True
isinstance(123, Iterable)  # 整数是否可迭代
# False

# 最后的小问题，如果要对list实现类似Java那样的下标循环怎么办？python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['elementA', 'elementB', 'elementC']):
    print(i, value)
# 0 elementA
# 1 elementB
# 2 elementC

# 上面的for循环里，同时引入了两个变量，这在python里是很常见的，比如下面的代码：

for x, y in [(1, 1), (2, 2), (3, 4)]:
    print(x, y)
# 1 1
# 2 2
# 3 4

"""


# 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# 复习知识：Python的函数返回多值其实就是返回一个tuple！
def findMinAndMax(l):
    if not l:
        return None, None
    else:
        return min(l), max(l)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
