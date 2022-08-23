# 函数的参数
"""
定义函数的时候，我们把函数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，
只要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

python的函数定义非常简单，却及其灵活。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
"""''


# 位置参数
# 先写一个计算x^2的函数
def power(x):
    return x * x


# 对于power(x)函数，参数x就是一个位置参数。
# 当我们调用power函数时，必须传入有且仅有的一个参数x：
print(power(13))


# 当我们想计算x^3怎么办呢。可以再定义一个power3函数，但如果要计算x^4, x^5....呢？
# 解决方法，可以把power(x)修改为power(x, n), 用来计算x^n
def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(2, 3))


# 改进后的函数power(x, n)有两个参数：x 和 n，这两个参数都是位置参数，
# 调用函数时，传入的两个值按照位置顺序依次赋给参数 x 和 n


# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，
# 导致旧的代码因为缺少一个参数而无法正常调用
# power(5)
# TypeError: power() missing 1 required positional argument: 'n'
# 明显的错误提示：调用函数power()缺少了一个位置参数 n 。
# 此时，默认参数就派上用场了。x^2是经常计算的，可以将第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


# 这样我们在调用power(5)的时候，相当于调用power(5, 2):
print(power(5))
print(power(5, 2))
# 对于n =！2 的其他情况，就需要明确的传入n的值，如power(5, 3)

"""
默认参数可以简化函数的调用。设置默认参数的时候，有几点需要注意
一是必选参数在前，默认参数在后，否则python的解释器会报错
二是如何设置默认参数。
当函数有多个参数时，把变化大当参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数最大的好处是能降低调用函数的难度。
"""


# 例子 写一个学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


# 这样，调用enroll()函数只需要传入两个参数：
enroll('Sher', 'M')


# name: Sher
# gender: M
# 如果要继续传入年龄，城市等信息怎么办？这样会使调用函数的复杂度大大增加。
# 可以把年龄和城市设为默认参数
def enroll(name, gender, age=6, city='Zhuhai'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
enroll('Sher', 'M')
# 只有与默认参数不符的学生才需要提供额外的信息：
enroll('Adam', 'F', 'Liao')
enroll('Adam', 'F', 7)
enroll('Adam', 'F', city='Liao')
enroll('Adam', 'F', 7, 'Liao')
# 输出的结果是不同的
"""
默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
无论是简单调用还是复杂调用，函数只需要定义一个。

有多个参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Adam', 'F', 7)，
意思是，除了name，gender这两个参数外，最后一个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

也可以不按顺序提供部分默认参数。当不按顺序提供部分参数时，需要把参数名写上。比如调用enroll('Adam', 'F', city='Liao')，
意思是，city参数用传进去的值，其他默认参数继续使用默认值。
"""


# 默认参数使用不当的坑：
# 先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L


# 当正常调用时，结果似乎不错：
add_end([1, 2, 3])
# [1, 2, 3, 'END']
add_end(['a', 'b', 'c'])
# ['a', 'b', 'c', 'END']
# 当使用默认参数调用时，一开始结果也是对的
print(add_end())
# ['END']
# 但再次调用add_end()时，结果就不对了
print(add_end())
# ['END', 'END']

# 原因解释如下：
"""
python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了
"""


# ！！！定义默认参数要牢记一点：默认参数必须指向不变对象。

# 对上面的例子进行修改，可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end(['a', 'b', 'c']))
print(add_end())
print(add_end())
# ['a', 'b', 'c', 'END']
# ['END']
# ['END']

"""
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
如果可以设计一个不变对象，那就尽量设计成不变对象。
"""

# 可变参数
"""
在python中还可以定义可变参数。可变参数传入的参数个数是可变的，可以是一个、两个到任意个，还可以是0个。
一个数学例子：给定一组数字a,b,c...，请计算a²+b²+c²+...

要定义出这个函数，我们必须确定输入函数的参数。由于参数个数不确定，
我们首先想到可以把a,b,c...作为一个list或tuple传进来，这样，函数可以定义如下：
"""


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 但是在调用时，需要先组装出一个list或tuple
resultA = calc([1, 2, 3, 4, 5])
print(resultA)
resultB = calc((1, 2, 3, 4, 5))
print(resultB)
# 如果利用可变参数，调用函数的方式可以简化成这样：
resultC = calc((1, 2, 3, 4, 5))
print(resultC)
"""疑问？？ 为什么在没定义可变参数的时候，就已经可以向函数传递可变参数了呢。如上例所示"""


# 所以，我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不同。
# 但是在调用该函数时，可以传入任意个参数，包括0个参数：
calc(1, 2)
# 5
calc()
# 0

# 如果已经有一个list或tuple，要调用一个可变参数怎么办？可以这样做：
nums = [3, 4, 5]
calc(nums[0], nums[1], nums[2])
# 14
# 虽然这种写法可行，但过于繁琐，所以python允许在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去：
nums = [3, 4, 5]
calc(*nums)
# 14
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# 关键字参数
"""
可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成为一个dict
"""


# 示例
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Somebody', 99)
# name: Somebody age: 99 other: {}

# 也可以传入任意个数的关键字参数：
person('personA', 11, city='Zhuhai')
# name: personA age: 11 other: {'city': 'Zhuhai'}
person('personB', 12, gender='Female', job='Nurse')
# name: personB age: 12 other: {'gender': 'Female', 'job': 'Nurse'}
"""
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数中，我们保证能接收到name和age两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。
情景：正在做一个用户注册的功能，除了用户名和年龄时必填项外，其他都是可选项，利用关键字参数来定义这个函数就可以满足注册的需求。
"""

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Zhuhai', 'job': 'Engineer'}
person('Sher', 24, city=extra['city'], job=extra['job'])
# name: Sher age: 24 other: {'city': 'Zhuhai', 'job': 'Engineer'}

# 简化写法
person('Sher', 24, **extra)
# name: Sher age: 24 other: {'city': 'Zhuhai', 'job': 'Engineer'}
"""
# **表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict时extra的一份拷贝，对kw的改动不会影响到函数外的extra。
"""


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 例：对于person()函数，我们希望检查是否有city和job参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 但是调用者仍可以传入不受限制的关键字参数：
person('Sher', 24, city='Zhuhai', addr='Xiangzhou', zipcode=114514)


# name: Sher age: 24 other: {'city': 'Zhuhai', 'addr': 'Xiangzhou', 'zipcode': 114514}

# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 调用方式：
person('Sher', 24, city='Zhuhai', job='Engineer')


# Sher 24 Zhuhai Engineer

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person('Sher', 24, 'Zhuhai', 'Engineer')
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
# 由于调用时缺少参数名city和job，python解释器把前面两个参数视为位置参数，后两个参数传给*args，
# 但缺少命名关键字参数导致报错

# 命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='Zhuhai', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可以不传入city参数：
person('Sher', 24, job='Engineer')
"""
Sher 24 Zhuhai Engineer
"""


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少*，city和job被视为位置参数
    pass


# 参数组合
"""
在python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这五种参数都可以组合使用。
但请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


# 比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 函数在调用的时候，python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=16)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 16}
f2(1, 2, d=16, ext=None)
# a = 1 b = 2 c = 0 d = 16 kw = {'ext': None}

# 神奇的是，通过一个tuple和dict，也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 16, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 16, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 17, 'y': '%'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 17 kw = {'y': '%'}


"""
所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
虽然可以组合多达5种参数，但不要同时使用太多但组合，否则函数接口但可理解性很差。
"""


# 练习：以下函数允许计算两个数的乘积，请稍加改造，变成可接一个或多个数并计算乘积：
# def mul(x, y):
#     return x * y
def mul(*nums):
    if len(nums) == 0:
        raise TypeError('input is empty!')
    product = 1
    for x in nums:
        product *= x
    return product


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 总结 函数参数的东西还挺多的
"""
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""
