# 定制类
"""
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

__str__
我们先定义一个Student类，打印一个实例：
"""''

class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Sher'))
# <__main__.Student object at 0x10262afd0>
# 打印出一堆<__main__.Student object at 0x10262afd0>，不好看。

# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：

class Student(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return 'Student object (name: %s)' % self.name

print(Student('Sher'))
# Student object (name: Sher)
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
s = Student('XiaFu')
# print(repr(s))
# 但是直接敲变量不用print，打印出来的实例还是不好看：
# <__main__.Student object at 0x......>
# Student object (name: Sher)
# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
"""
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
"""


# __iter__
"""
如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的一个值，知道遇到StopIteration错误时退出循环。
"""

# 斐波那契数列的for循环，Fib类：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 50:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

# 现在，试试把Fib实例作用于for循环：
for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
"""
Fib()[5]  # TypeError: 'Fib' object is not subscriptable
"""
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[5])  # 8

# 但是list有个神奇的切片方法：
print(list(range(16))[5:10])  # [5, 6, 7, 8, 9]

# 对于Fib却报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 现在试试Fib的切片：
f = Fib()
print(f[0:5])  # [1, 1, 2, 3, 5]
print(f[2:6])  # [2, 3, 5, 8]

# 但是没有对step参数做处理：
print(f[:8:2])  # [1, 1, 2, 3, 5, 8, 13, 21]
"""
也没有对负数做处理，所以，要正确实现一个__getitem__()还是有许多工作要做的。

此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__deleitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现的和python自带的list、tuple、dict没什么区别，这完全归功于动态语言的"鸭子类型"，不需要强制继承某个接口。
"""

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，比如定义Student类：
class Mate(object):

    def __init__(self):
        self.name = "somebody"

# 调用name属性没问题，但是，调用不存在的score属性，就有问题了：
m = Mate()
print(m.name)  # somebody
# print(m.score)  # AttributeError: 'Mate' object has no attribute 'score'
# 错误信息明显的告诉我们，没有找到score这个attribute。

# 要避免这个错误，除了可以加上一个score属性外，python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Mate(object):

    def __init__(self):
        self.name = 'somebody'

    def __getattr__(self, item):
        if item == 'score':
            return 16

# 当调用不存在的属性时，比如score，python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
m1 = Mate()
print(m1.score)  # 16

# 返回函数也是完全可以的，
class Mate(object):

    def __getattr__(self, item):
        if item == 'age':
            return lambda: 24

m2 = Mate()
print(m2.age)  # <function Mate.__getattr__.<locals>.<lambda> at 0x1012cb040>
print(m2.age())  # 24  # 调用方法需要改变一下。
"""
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会再有__getattr__中查找。

此外，注意到任意调用如m.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
"""

# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Mate(object):

    def __getattr__(self, item):
        if item == 'age':
            return lambda: 24
        raise AttributeError('\'Mate\' object has no attribute \'%s\'' % item)

# m3 = Mate()
# print('m3:', m3.sth)  # AttributeError: 'Mate' object has no attribute 'sth'

"""
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况做调用。

举个例子：？？？？？？？？？？？？？？？？？？？？

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
试试：

>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！

还有些REST API会把参数放到URL中，比如GitHub的API：

GET /users/:user/repos
调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：

Chain().users('sher').repos
就可以非常方便地调用API了。
"""

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？在python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

# 调用方式如下：
s = Student('Sherrinford')
print(s())  # self参数不要传入。
# My name is Sherrinford.

"""
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，你完全可以把对象看成函数，把函数看成对象，二者之间本来也没啥区别。

如果把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个callable对象。

比如函数和上面定义的带有__call__()的实例：
"""

print(callable(Student('a')))  # True
print(callable(abs))  # True
print(callable([1, 2, 3]))  # False
print(callable(None))  # False
print(callable('str'))  # False
# 通过callable()函数，我们就可以判断一个对象是否是"可调用对象"。


# 小结：
# python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
# https://docs.python.org/3/reference/datamodel.html#special-method-names 官方文档

#评论区对Chain().users('sher').repos解惑
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __call__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('sher').repos) # /users/sher/repos

# """
# 每次调用类Chain()都会运行一下类里面的__init__()函数进行初始化里面的相应属性，在这里边相当于重建实例覆盖之前的实例，具体来看
#
# Step 1：
# Chain()  # 实例化
#
# Step 2：
# Chain().users
# # 由于没有给实例传入初始化对应属性的具体信息，从而自动调用__getattr__()函数，从而有：
# Chain().users = Chain('\users') # 这是重建实例
#
# Step 3:
# Chain().users('michael')
# Chain().users('michael') = Chain('\users')('michael') # 这是对实例直接调用，相当于调用普通函数一样
# # 关键就在这步，上面的朋友没有说明晰（并不是说你们不懂），这一步返回的是Chain('\users\michael'),再一次重建实例，覆盖掉Chain('\users'),
# #记 renew = Chain('\users\michael')， 此时新实例的属性renew.__path = \users\michael;
#
# Step 4:
# Chain().users('michael').repos
# # 这一步是查询renew实例的属性repos，由于没有这一属性，就会执行__getattr__()函数，
# # 再一次返回新的实例Chain('\users\michael\repos')并且覆盖点之前的实例，
# # 这里记 trinew =Chain('\users\michael\repos')，不要忘了，一旦定义了一个新的实例，就会执行__init__方法；
#
# Step 5：
# print(Chain().users('michael').repos) = print(trinew)
# # 由于我们定义了__str__()方法，那么打印的时候就会调用此方法，据此方法的定义，打印回来的是trinew的__path属性，即——\users\michael\repos  。
# # 至此，我们也把所有定义的有特殊用的方法都用上了，完毕。
# """
