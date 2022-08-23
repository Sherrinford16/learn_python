"""
# python内建的filter()用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素,
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
"""
# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(num):
    return num % 2 == 1

odd_list = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8]))
# print('odd_list:', odd_list)  # odd_list: [1, 3, 5, 7]

# 把一个序列中的空字符串删掉，可以这么写：
def del_empty(s):
    return s and s.strip()  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

not_empty_list = list(filter(del_empty, ['A', '', 'B', None, 'C', '  ']))
# print(not_empty_list)  # ['A', 'B', 'C']

"""
# 可见用filter()这个高阶函数，关键在于正确实现一个"筛选"函数。
# 注意到filter()函数返回一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。
"""

# 用filter求素数 素数一般指质数。质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
"""
# 计算素数的一个方法是埃式筛法，理解算法：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 5, 7, 9, 11, 13, 15, 17, 19, ...
# 取序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 7, 11, 13, 17, 19, ...
# 取序列的第一个数5，它一定是素数，然后用5把序列的5的倍数筛掉：
# 7, 11, 13, 17, 19, ...
# 不断筛下去，就可以得到所有的素数。
"""
# 用python来实现这个算法，可以先构造一个从3开始的奇数序列：
def odd_generator():
    n = 1
    while True:
        n = n + 2
        yield n
    # 这是一个生成器，并且是一个无限序列

# 然后定义一个筛选函数：
def not_divisible(n):
    return lambda x: x % n > 0

# 最后定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = odd_generator()  # 初始序列
    # print('地址:', id(it))  # 查询地址完全是因为之前有讲到每次generator就会构造新的地址，看看内存中是不是真这样
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(not_divisible(n), it)  # 构造新序列
        # ？？为什么filter(not_divisible, it)时就不能正常构造呢？？是不是和lambda有关呢？
        # print('地址:', id(it))  # 真的每调用一次generator就产生一个新的地址。。。有没有什么回收机制呢

"""
# 这个生成器先返回第一个素数2，然后，利用filter不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个循环退出的条件：
"""
# 打印1000以内的素数：
for n in primes():
    if n < 10:
        print(n)
    else:
        break

# 练习：回数是指从左向右读和从右向左读都是一样的数，例如090，12321。请利用filter()筛选出回数：
def is_palindrome(n):
    ps = str(n)
    io = ps[::-1]
    return n and ps == io
# 最简化 return str(n) = str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')