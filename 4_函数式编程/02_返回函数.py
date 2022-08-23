# 返回函数
# 闭包详解：  https://zhuanlan.zhihu.com/p/453787908
"""
# 函数作为返回值
# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果返回。
"""

# 下面实现一个可变参数的求和，通常情况下，求和函数的定义是这样的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # <function lazy_sum.<locals>.sum at 0x102fd7280>
# 调用函数f时，才真正计算求和结果：
print(f())  # 25

"""
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以调用外部函数lazy_sum中的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为"闭包(Closure)"的程序结构拥有极大的威力。
"""

# 注意！当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)  # False
# f1()和f2()的调用结果互不影响。


# 闭包
"""
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
# 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
"""

# 另一个需要注意的问题，返回的函数并没有立刻执行，而是直到调用了f()才执行。例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print('f1():', f1(), 'f2():', f2(), 'f3():', f3())  # f1(): 9 f2(): 9 f3(): 9
"""
# 上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
# 期待调用f1()，f2()和f3()的结果应该是1，4，9，但实际得到的是f1(): 9 f2(): 9 f3(): 9
# why？
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变为了3。因此最终结果为9。

# ！！！返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。！！！
"""
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def new_count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = new_count()
print('f4():', f4(), 'f5():', f5(), 'f6():', f6())  # f4(): 1 f5(): 4 f6(): 9
# 这样做的缺点就是代码较长，可利用lambda函数缩短代码。


# nonlocal 非局部的
# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读取外层变量的值，我们会发现返回的闭包函数调用一切正常：
def inc():
    x = 0
    print('外层局部变量x:', x)
    print('outer x before call inner:', x, 'at', id(x))
    def fn():
        # 仅读取x的值：
        print('fn()内的x:', x)
        print('inner x:', x, 'at', id(x))
        return x + 1
    return fn

f_inc = inc()
print('1, f_inc():', f_inc(), '2, f_inc():', f_inc())  # 1, f_inc(): 1 2, f_inc(): 1

# 但是如果对外层变量赋值，由于python解释器会把x当作函数fn()的局部变量，它会报错：

def non_inc():
    x = 0
    def fn():
        nonlocal x  # 当加如这个声明时，正常运行，而注释掉这个函数会报下面的错误
        x = x + 1  # local variable 'x' referenced before assignment
        return x
    return fn

f_non = non_inc()
print('1, f_non:', f_non(), '2, f_non:', f_non())  # 1, f_non: 1 2, f_non: 2
"""
# 报错原因是x作为局部变量并没有初始化，直接计算x+1是不行的。但我们其实是想引用inc()函数内部的x，
# 所以需要在fn()函数内部加一个nonlocal x的声明。加上这个声明后，解释器把fn()的x看作是外层函数的局部变量。
# 它已经被初始化了，可以正确计算x+1。

# ！！！使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。！！！
"""

# 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x = 0
    print('外层局部变量x:', x)
    print('outer x before call inner:', x, 'at', id(x))
    def counter():
        nonlocal x
        print('未计算前的变量x:', x)
        print('inner x:', x, 'at', id(x))
        x = x + 1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# https://zhuanlan.zhihu.com/p/453787908
# 对 x = 0 的疑问，借用下面一个解释：
# counterA = createCounter()，第一次counterA()之后，返回counter，counterA就变成counter了
# 第二次counterA()就相当于counter()了，就只执行了counter()中的代码