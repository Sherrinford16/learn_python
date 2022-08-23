"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
95
就像字典里使用偏旁部首的查找方式一样
"""

# 把数据放入dict的方法, 除了初始化时指定外, 还可以通过key放入
newDic = {'A': 15, 'B': 16, 'C': 17}
# newDic['C'] = 18
# print(newDic['C'])

# 若key不存在, dict就会报错
# newDic['D']
# print(newDic['D'])
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/05_dict_set.py", line 20, in <module>
#     newDic['D']
# KeyError: 'D'

# 要避免key不存在的错误, 有两种办法, 一是通过in判断key是否存在
# print('D' in newDic)
# 二是通过dict提供的get()方法, 如果key不存在, 可以反悔None, 或者自己指定的value
# 注意 返回None的时候python的交互环境不显示结果
# print(newDic.get('D'))
# print(newDic.get('a', 'oh no'))

# 要删除一个key， 用pop(key)方法, 对应的value也会从dict中删除
# newDic.pop('C')
# print(newDic)
"""
注意! dict内部存放的顺序和key放入的顺序是没有关系的
和list比较，dict有以下几个特点:
查找和插入的速度极快, 不会随着key的增加而变慢;
需要占用大量的内存, 内存浪费多
而list相反:
查找和插入的时间随着元素的增加而增加;
占用空间小, 浪费内存很少
所以, dict是用空间来换取时间的一种方法
dict可以用在需要高速查找的很多地方, 在Python代码中几乎无处不在,正确使用dict非常重要
需要牢记的第一条就是dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了
这个通过key计算位置的算法称为哈希算法(Hash)
"""
# 要保证hash的正确性, 作为key的对象就不能变. 在Python中, 字符串/整数等都是不可变的, 可以放心地作为key
# 而list是可变的, 就不能作为key
# key = [1, 2, 3]
# newDic[key] = 'test value'
# print(newDic[key])
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/05_dict_set.py", line 52, in <module>
#     newDic[key] = 'test value'
# TypeError: unhashable type: 'list'

# set
"""
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
"""
newSet = set([1, 2, 3])
# 函数调用可被替换为集合文字 newSet = {1, 2, 3}
# print(newSet)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这三个元素，显示的顺序也不表示set是有序的

# 重复元素在set中自动被过滤
newSet1 = set([2, 2, 3, 5, 6])
# 函数调用可被替换为集合文字 newSet1 = {2, 2, 3, 5, 6}
print('newSet1:', newSet1)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
newSet.add(4)
newSet.add(4)
print('newSet_add:', newSet)

# remove(key)方法可以删除元素
newSet.remove(4)
print('newSet_remove:', newSet)

# add(key)方法,remove(key)方法只能接收一个变量，传入多个会报错
# newSet.add(4, 5)
# print(newSet)
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/05_dict_set.py", line 77, in <module>
#     newSet.add(4, 5)
# TypeError: set.add() takes exactly one argument (2 given)

# set可以看成数学意义上的无序无重复元素的集合，因此两个set可以做数学意义上的交集、并集等操作
print('交集:', newSet & newSet1)
print('并集:', newSet | newSet1)

"""
set和dict的唯一区别仅在于没有存储对应的value，但是set的原理和dict一样，所以，同样不可以放入可变对象
因为无法判断两个可变对象是否相等，也就无法保证set内部"不会有重复元素" 尝试: 将list放入set，看看是否会报错
"""


# 不可变对象 上面讲到，str是不可变对象，list是可变对象
# 对于可变对象，如list，对list进行操作，list内部的内容是会变化的
listTest = ['c', 'a', 'b']
listTest.sort()
print(listTest)
# 而对于不可变对象，如str，对str进行操作
strTest = 'aabc'
strReplace = strTest.replace('aa', 'Ax')
print('strReplace: ', strReplace)
print('strTest: ', strTest)

"""
注意！！！！！
需要牢记，strTest是变量，而'aabc'才是字符串对象！有这种说法：对象strTest的内容是'aabc'，但其实是指：
strTest本身是一个变量，它指向的对象的内容才是'aabc'
当我们调用strTest.replace('aa', 'Ax')时，实际上调用方法replace是作用在字符串对象'aabc'上的，
而这个方法名字虽然是replace，但却没有改变字符串'aabc'的内容。相反，replace方法创建了一个新字符串'Axbc'并返回，
我们用变量strReplace指向该新字符串，变量strTest仍然指向原有的字符串'aabc'，但strReplace却指向了新字符串'Axbc'了
所以，对于不变对象来说，调用自身的任意方法，也不会改变该对象自身的内容。相反，
这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
"""

# 练习：tuple虽然是不变对象，但试着吧(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果
practiceT1 = (1, 2, 3)
practiceT2 = (1, [2, 3])
practiceD = {}
practiceD['d1'] = practiceT1
# practiceD['d2'] = practiceT2
practiceD.update({'d2': practiceT2, 'd3': 16})
# practiceD = {'d1': practiceT1, 'd2': practiceT2}
print(practiceD)
print(practiceD['d1'])


practiceS_empty1 = {}
print('practiceS_empty1: ', practiceS_empty1)
practiceS_empty2 = set()
print('practiceS_empty2: ', practiceS_empty2)
practiceS_empty2.add(9)
print('practiceS_empty2_add: ', practiceS_empty2)
# 如果要创建一个空的set，只能使用set()关键字，因为如果使用set1={}这种方式，那么set1会被声明为一个空的字典

practiceS = {1}
practiceS.add(practiceT1)
print(practiceS)
# practiceS.add(practiceT2)
# print(practiceS)
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/05_dict_set.py", line 139, in <module>
#     practiceS.add(practiceT2)
# TypeError: unhashable type: 'list'

# 结论1 set中可以存放tuple，并且tuple中的元素不能有list，只能是单纯的元素
# 也可以说：含有list的tuple可以作为value值，但不能作为key值
# 结论2 dict中可以存放上面的两种的tuple

# 评论区中的小知识：
""" https://www.jb51.net/article/251922.htm 对set详细点的解答 """
# 在3.7之前的版本中，使用popitem将从dict中随机取出一对(key, value)，在之后的版本中结果遵照LIFO(后进现出)
# 即先进后出。必要时可以将dict作为有序对象进行操作（有点怪）。
d = {1:2,2:4,4:8}
pop1 = d.popitem()
print(pop1)
# (4, 8)
pop2 = d.popitem()
# (2, 4)
pop3 = d.popitem()
# (1, 2)

