"""
# 排序算法
# 排序也是程序中经常用到的算法，无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上但大小是没有意义的，
# 因此，比较的过程必须通过函数抽象出来。
"""

# python内置的sorted()函数就可以对list进行排序：
test0 = sorted([36, 5, -12, 9, -21])  # [-21, -12, 5, 9, 36]
print(test0)

# sorted()函数也是一个高阶函数，它还可以接受一个key函数来实现自定义的排序，例如按绝对值大小排序：
test1 = sorted([36, 5, -12, 9, -21], key=abs)  # [5, 9, -12, -21, 36]
print(test1)
# key指定的函数将作用于list的每个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过处理的list。

"""
list = [36, 5, -12, 9, -21]
key = [36, 5, 12, 9, 21]
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：
# keys排序结果 => [5, 9,  12,  21, 36]
#                 |  |    |    |   |
# 最终结果     => [5, 9, -12, -21, 36]
"""

# 一个字符串排序的例子：
test2 = sorted(['bob', 'about', 'Zoo', 'Credit'])  # ['Credit', 'Zoo', 'about', 'bob']
print(test2)

"""
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 现在，提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（小写），再比较。
"""

# 给sorted()函数传入key函数，实现忽略大小写的排序：
test3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # ['about', 'bob', 'Credit', 'Zoo']
print(test3)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:
test4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)  # ['Zoo', 'Credit', 'bob', 'about']
print(test4)

"""
# 从上述列子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持的非常简洁。
# 小结：sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
"""

# 练习：假设我们用一组tuple表示学生的名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]
test5 = sorted(L, key=by_name)
print(test5)

# 再按成绩从高到低排序：
def by_score(t):
    return t[1]  # -t[1]也可以实现倒序
test6 = sorted(L, key=by_score, reverse=True)
print(test6)
