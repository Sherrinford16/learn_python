# 获取对象信息

"""
“在python 中,变量也称为对象的引用。因为变量存储的就是对象的地址。变量通过地址引用了“对象”。”

当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
"""''


class Animal(object):
    def run(self):
        print('Animal is running...')  # 定义一个类来实现下面的调用

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Corgi(Dog):
    def run(self):
        print('Corgi is running...')


a = Animal()

# 使用Type()
# 首先，我们来判断对象类型，使用type()函数：
# 基本类型都可以用type()判断：
print(type(123))  # <class 'int'>
print(type('str'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))  # <class 'builtin_function_or_method'>
print(type(a))  # <class '__main__.Animal'>

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(1))  # True
print(type(123) == int)  # True
print(type('abc') == type('123'))  # True
print(type('a1b2c3') == str)  # True
print(type('abc') == type(123))  # False

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import types
def fn():
    pass

print(type(fn) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type((x for x in range(10))) == types.GeneratorType)  # True


# 使用isinstance()
"""
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

回顾之前的例子，如果继承关系是：

object -> Animal -> Dog -> Ein  # See you space cowboy.

那么，isinstance()就可以告诉我们，一个对象是否是某种类型。
"""

# 先创建三种类型的对象:
an = Animal()
do = Dog()
co = Corgi()

# 然后判断：
print('isinstance(co, Corgi):', isinstance(co, Corgi))  #  True
# 没问题，因为co变量指向的就是Corgi对象。接着判断：
print('isinstance(co, Dog):', isinstance(co, Dog))  # True
# co虽然自身是Corgi类型，但由于Corgi是从Dog继承下来的，所以，co也还是Dog类型。换句话说，
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

# 因此，可以确信，co还是Animal类型：
print('isinstance(co, Dog) and isinstance(co, Animal):', isinstance(co, Dog) and isinstance(co, Animal))  # True

# 但是！do不是Corgi类型：
print('isinstance(co, Dog):', isinstance(do, Corgi))  # False

# 能用type()判断的基本类型也可以用isinstance()判断：
print("isinstance('a', str):", isinstance('a', str))  # True
print("isinstance(123, int):", isinstance(123, int))  # True
print("isinstance(b'a', bytes):", isinstance(b'a', bytes))  # True

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print("isinstance([11, 2, 3], list):", isinstance([11, 2, 3], list))  # True
print("isinstance((1, 2, 3), tuple):", isinstance((1, 2, 3), tuple))  # True

""" 总是优先使用isinstance()判断类型，可以将制定类型及其子类'一网打尽'。"""


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
# print("dir('ABC'):", dir('ABC'))
# dir('ABC'): ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""
类似__xxx__的属性和方法在python中都是有特殊用途的，比如__len__方法返回长度。在python中，如果你调用len()函数试图获取一个对象的长度，

实际上，在len()函数内部，它自动去调用该对象的__len__()方法，下面的代码是等价的：

"""
print(len('ABC'))  # 3
print('ABC'.__len__())  # 3

# 我们自己写的类，如果也想用len(myobj)的话，就自己写一个__len__()方法：
class myDog(object):
    def __len__(self):
        return 16

Ein = myDog()
print('Ein_len:', len(Ein))  # Ein_len: 16

"""
剩下的都是普通属性或方法，比如lower()返回小写字符串之类的 'ABC'.lower() -> 'abc'

仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
"""

class myObject(object):
    def __init__(self):
        self.x = 16
    def power(self):
        return self.x * self.x

obj = myObject()
# 紧接着，可以测试该对象的属性：
print("有属性'x'吗", hasattr(obj, 'x'))  # 有属性'x'吗
# True
print(obj.x)
# 16
print("有属性'y'吗", hasattr(obj, 'y'))  # 有属性'y'吗
# False
setattr(obj, 'y', 17)  # 设置一个属性'y'

print("有属性'y'吗", hasattr(obj, 'y'))  # 有属性'y'吗
# True
print("获取属性'y'", getattr(obj, 'y'))  # 获取属性'y'
# 17
print("获取属性'y'", obj.y)  # 获取属性'y'
# 17

# 如果试图获取不存在的属性，会抛出AttributeError的错误
"""
getattr(obj, 'z')
AttributeError: 'myObject' object has no attribute 'z'
"""

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 'NOT FOUND'))  # 获取属性'z'，如果不存在，返回默认值'NOT FOUND'
# NOT FOUND

# 也可以获得对象的方法：
print("有属性'power'吗", hasattr(obj, 'power'))  # 有属性'power'吗？
# True

print(getattr(obj, 'power'))  # 获取属性'power'
# <bound method myObject.power of <__main__.myObject object at 0x104862670>>
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn

print(fn)  # fn指向obj.power
# <bound method myObject.power of <__main__.myObject object at 0x100d56670>>
print(fn())  # 调用fn()与调用obj.power()是一样的
# 256


# 小结
"""
通过内置的一系列函数，我们可以对任意一个python对象进行剖析，拿到其内部的数据。要注意的是，只有不知道对象信息的时候，我们才会去获取对象信息。

如果可以直接写：
sum = obj.x + obj.y

就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')

一个正确的用法例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在python这类动态语言中，根据鸭子模型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，

但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
"""

# 评论区对 k = v ;  obj.k = v的理解：
"""
# 提问
以obj为例，请问setattr(obj,'y',19)和obj.y=19有什么区别呢？
感觉后者写法上貌似更简洁直观，而且廖老师说的是在不知道对象信息的时候，
我们才用hasattr()之类的函数，但是如果通过hasattr函数确定了对象含有某个属性之后，
为什么不直接用obj.y的形式对该属性进行读取和赋值呢，
因为貌似使用getattr(obj,'y')的前提就是已经知道了obj含有属性y，
而setattr(obj,'y',19)则感觉不需要知道obj结构，相当于自行新增的一个属性y，感觉完全可以用obj.y=19替代。


# 老师举例：

# 把dict的key - value复制到obj，前提是obj有对应的property
def dict2bean(obj, d):
    for k, v in items(d):
        if hasattr(obj, k):
            setattr(obj, k, v) # 能写成obj.k = v吗？
有些时候那个property name也是变量

# 翻译

正常使用 setattr(obj,'y',19) 中的‘y’，此时并不是一个变量，它只是一个字符串，起着匹配的作用

而廖老师代码中setattr(obj, k, v）的k虽然也是匹配作用，但此时并非一个简单的字符串，而是一个变量，指向每次循环对应的dic中的key值，

若写成obj.k = v这个，obj中就会生成k这个属性，故不行
"""
