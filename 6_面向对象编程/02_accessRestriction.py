# 访问限制

"""
在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

但是，从前面的Student类的定义上来看，外部代码还是可以自由地修改一个实例的name，score属性：
"""''


# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# bart = Student('Bart Simpon', 59)
# print(bart.score)  # 59
# bart.score = 99
# print(bart.score)  # 99

"""
如果要让内部属性不被外部访问，可以把属性的名称前面加上两个下划线__，在python中，实例的变量名如果以__开头，就变成了一个私有变量（private），

只有内部可以访问，外部不能访问，所以，我们把Student类改一改。
"""

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

"""
class Student(object):
    ...
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
"""

# 如果又要允许外部代码修改score怎么办

"""
class Student(object):
    ...
    def set_score(self, score):
        self.__score = score
"""

# 提问？原先那种直接通过 bart.score = 99 也可以修改啊，为什么要定义一个方法大费周折？
# 因为在方法中，可以对参数做检查，避免传入无效参数。

"""
class Student(object):
    ...
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score') 
"""

"""
需要注意的是，在python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量

特殊变量是可以直接访问的，不是private变量，所以不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定成俗的规定，

当看到这样的变量时，意思就是，"虽然我可以被访问，但是，请把我视为私有变量，不要随意访问。"

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。

不能直接访问__name是因为python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

# print(bart._Student__name)  # 'Bart Simpon'

# 但是强烈建议不要这么干，因为不同版本的python解释器可能会把__name改成不同的变量名。

总的来说就是，python本身么有任何机制阻止你干坏事，一切全靠自觉。

--------------------------
at last 注意下面这种错误写法：

# >>> bart = Student('Bart Simpon', 59)
# >>> bart.get_name()
# 'Bart Simpon'
# >>> bart.__name = 'New Name'  # 设置__name变量！
# >>> bart.__name
# 'New Name'

表面上看，外部代码"成功"地设置了__name变量， 但实际上这个__name变量和class内部的__name变量不是一个变量！！

内部的__name变量已经被python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。调用一下：

# >>> bart.get_name()  # get_name()内部返回self.__name
# 'Bart Simpon'

"""''


# 练习：请把下面Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')