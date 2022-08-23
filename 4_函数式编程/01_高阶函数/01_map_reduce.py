# map/reduce
"""
# python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作为用到序列的每个元素，并把结果作为新的Iterator返回。
# 举例说明，有一个函数f(x)=x^2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9] 上，就可以用map()实现：
                                        f(x) = x * x

                                              │
                                              │
                              ┌───┬───┬───┬───┼───┬───┬───┬───┐
                              │   │   │   │   │   │   │   │   │
                              ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

                            [ 1   2   3   4   5   6   7   8   9 ]

                              │   │   │   │   │   │   │   │   │
                              │   │   │   │   │   │   │   │   │
                              ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

                            [ 1   4   9  16  25  36  49  64  81 ]

"""


# 用python代码实现：
import shlex


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# 可不可以，不需要map()函数，写一个循环，也可以计算出结果：
"""
L1 = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L1.append(f(n))
print(L1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
# 的确实现了，但从上面的循环代码，能一眼看明白"把f(x)作用在list的每一个元素并把结果生成一个新list"吗？
# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此我们不仅可以计算简单的f(x)=x^2，
# 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符：
"""
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------------------------------------------------------------
"""
# reduce用法：
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积运算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：
"""
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [2, 4, 6, 8, 10])  # 30

"""
# 求和运算可以直接用python内建sum()，没必要动用reduce。
# 但如果要把序列[2, 4, 6, 8, 10]变成整数246810，reduce就可以派上用场：
"""
def fn(x, y):
    return x * 10 + y

reduce(fn, [2, 4, 6, 8])  # 2468

"""
# 上例本身没啥用，但是，如果考虑到字符串str也是一个序列，对上面对例子稍加改动，配合map()，
# 我们就可以写出str转换为int的函数：
"""
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

# reduce(fn, map(char2num, '2468'))  # 2468

# 整理成一个str2int的函数就是
Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def char2num(s):
        return Digits[s]
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, s))

# print(str2int('13245'))  # 13245

# 还可以用lambda函数进一步简化：
def lam_char2num(s):
    return Digits[s]

def lam_str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(lam_char2num, s))

# print(lam_str2int('22413'))  # 22413

# so,假设python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！
# 上面提到的 lambda函数的用法后面介绍


# 练习1：
"""
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母答谢，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
"""

def normalize(name):
    return name[:1].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
map(normalize, L1)
L2 = list(map(normalize, L1))
print(L2)  # ['Adam', 'Lisa', 'Bart']

# 练习2：
"""
python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
def prod(L):
    def product(x, y):
        return x * y
    return reduce(product, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习3：
"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456:
"""
# map()对字符串中的每个元素进行操作，
# reduce()对map()处理完的每个元素进行操作。
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}
def str2float(s):
    newList1 = s.split('.')
    chu = len(newList1[1])
    print('小数点后:', chu)
    newStr = newList1[0] + newList1[1]
    print(newStr)
    def str2num(newStr):
        print(newStr)
        return DIGITS[newStr]
    def num2int(x, y):
        print('x:', x, 'y:', y)
        return x * 10 + y
    newInt = reduce(num2int, map(str2num, newStr))
    print(newInt)
    print(isinstance(newInt, int))
    # print(newInt / 3)
    return newInt / 10 ** chu

# print('str2float(\'5672.42256\') =', str2float('57672.42256'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# a = '123.456'.split('.')
# print(a)
#
# print(a[0] + a[1])
# # isinstance(a[0] + a[1], int)
# print(isinstance(a[0] + a[1], str))