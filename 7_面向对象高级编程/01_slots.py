# 使用__slots__

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性，先定义class：
class Student(object):
    pass


# 然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Sher'  # 动态给实例绑定一个属性
print(s.name)  # Sher


# 还可以尝试给实例绑定一个方法：
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print('s.age:', s.age)  # 25

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
""" s2.set_age(25)  # AttributeError: 'Student' object has no attribute 'set_age' """


# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
print(s.score)  # 100
s2.set_score(60)
print(s2.score)  # 60

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言很难实现。


# 使用__slot__
"""
如果想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slot__变量，来限制该class实例能添加的属性：
"""


class Student1(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 试试：
newS = Student1()  # 创建新的实例
newS.name = 'Sher'  # 绑定属性'name'
newS.age = '24'  # 绑定属性'age'
# newS.score = '60'  # 绑定属性'score'  # 报错：AttributeError: 'Student1' object has no attribute 'score'
"""
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
"""


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student1):
    # __slots__ = ('a', 'b')
    pass


g = GraduateStudent()
g.socre = 9999
print(g.socre)  # 9999
# g.name = 'A'  # AttributeError: 'GraduateStudent' object has no attribute 'socre'
""" 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__ """
