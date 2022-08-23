# 由于函数也是一个对象，而且函数对象可以被赋值给变量，
# 所以，通过变量也可能调用该函数。
def now():
    print('2022/7/25')

f = now  # 这个就类似前面abs函数的例子
print(f())
"""
# 2022/7/25 
# None  # 在调用f之后除了期待值2022/7/25 ，多输出了一个None，啊，我懂了，因为默认return None
"""

# 函数对象有一个__name__属性，可以拿到函数的名字
print('now.__name__:', now.__name__)  # now.__name__: now
print('f.__name__:', f.__name__)  # f.__name__: now

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为"装饰器(Decorator)"

# 本质上decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上述的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助python的 @语法 ，把decorator置于函数的定义处：

@log
def now():
    print('2022-7-25')

print(now())
print('now.__name__:', now.__name__)
# call now():
# 2022-7-25

"""
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
>>> now
call now():
2022-7-25

# 把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数

# wrapper()函数的参数定义是(*args, **kw)。因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decoratro本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
"""

# 比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2022/7/26')

print(now())
print('now.__name__:', now.__name__)
# execute now():
# 2022/7/26

"""
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
>>> now = log('execute')(now)
# 剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，
# 参数是now函数，返回值最终是wrapper函数。
"""


"""
# 以上两种decorator的定义都没有问题，但还差最后一步。因为函数也是对象它有__name__等属性，但去看经过decorator装饰后的函数，
# 它们的__name__已经从原来的'now'变成了'wrapper':
>>> now.__name__
'wrapper'

# 因为返回的那个wrapper()函数名字就是wrapper，所以,需要把原始函数的__name__等属性复制到warpper()函数中，
# 否则，有些依赖函数签名等代码执行就会出错。

# 不需要编写wrapper.__name__ == func.__name__这样的代码，
# python内置的functools.wraps就是做这个事的，
"""

# 一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 或者针对带参数的decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# import functools是导入functools模块。模块的概念后续讲解。
# 现在只需要记住在定义wrapper()的前面加上@functools.wraps(func)即可。


# 练习，请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t0 = time.time()
        a = fn(*args, **kw)
        t1 = time.time()
        print('%s executed in %s ms' % (fn.__name__, t1 - t0))
        print(a)
        return a
    return wrapper

# # 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


"""
# 小结：
# 面向对象(OOP)的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# python的decorator可以用函数实现，也可以用累实现。

# decorator可以增强函数的功能，定义起来有点复杂，但使用起来非常灵活方便。
# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考能否写出一个@log的decorator，是它既支持：
@log
def f():
    pass
    
# 又支持：
@log('execute')
def f():
    pass
"""