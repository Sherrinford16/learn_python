"""
有序集合list []
"""
detective = ['SH', 'BR', 'Queen']
print(detective)

# len()函数获取list元素个数
list_length = len(detective)
print(list_length)

# 索引访问list中每个位置的元素 索引从0开始
# 索引越界报错IndexError 最后一个元素的索引为len(detective)-1
print(detective[0], detective[1], detective[2])
# 倒序索引 -1直接获取最后一个元素
# 疑问 当list中只有一个元素时 -1和0的索引都是该元素
test_list = ['just one']
print(test_list[-1], test_list[0])

# 可变有序表list 添加删除元素
# append()向末尾追加元素
detective.append('AP')
print(detective)
# insert()将元素插入到指定位置
detective.insert(0, 'You?')
print(detective)
# pop()删除末尾元素 删除指定位置的元素用pop(i) i为索引位置
detective.pop()
print(detective)
detective.pop(0)
print(detective)
# 将某个元素替换成别的元素, 可以直接赋值给对应的索引位置
detective[1] = 'AC'
print(detective)
# list中的数据类型可以不同 list元素也可以是另一个list
s = ['python', 'js', ['c', 'c++'], 'java']
print(len(s))
# 注意s只有4个元素 可以将s看作是一个二维数组
p = ['c', 'c++']
s = ['python', 'js', p, 'java']
print(s[2][1])

"""
tuple 有序列表元组 () tuple一旦初始化就不能修改 代码更安全 没有append(), insert()这样的方法
其他获取元素的方法和list是一样的 正常使用name[0] name[-1]
"""
name = ('a', 'b', 'c')
# tuple的陷阱: 当定义一个tuple时, tuple的元素就必须被确定下来
t = (1, 2)
print('!!!!!!!!!!', t[1])
# 如果要定义一个空的tuple, 可以写成()
t = ()
print(t)
# ????????? 为什么这里的t正常声明啊 python的变量指针是咋指的捏 ???????
# 定义一个只有一个元素的tuple, t = (1) 会产生歧义, () 既能表示tuple, 又是数学公式中的小括号
# python规定在这种情况下, 按小括号计算, 计算结果为1
# 那么, 定义一个元素的tuple时必须加上一个","逗号, 来消除歧义
# python在现实只有一个元素的tuple的时候也会加上一个逗号,用来区分
t = (1,)
print(t)

# "可变"tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
"""
原因:
 ['A', 'B']是一个list 被改变的是list中的元素
 tuple一开始就指向了该list, 且没有改变指向别的list
 所以tuple所谓的不变是说, tuple的每个元素，指向永远不变
 要创建一个内容也不变的tuple必须要保证其中的每一个元素本身也不能变
"""

# 练习 用索引取出list中的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])