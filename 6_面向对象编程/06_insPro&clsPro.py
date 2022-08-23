# 实例属性和类属性

# 由于python是动态语言，根据类创建的实例可以任意绑定属性值。
# 给实例绑定属性的方法是通过实例变量，或通过self变量：
"""
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
"""''


# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类但所有实例都可以访问到。来测试一下：
"""class Student(object):
    name = 'Student'


testS = Student()  # 创建实例testS

print(testS.name)  # 打印那么属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student

print(Student.name)  # 打印类的name属性
# Student

testS.name = 'Sher'  # 给实例绑定name属性

print(testS.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Sher

print(Student.name)  # 但是类属性并没有消失，用Student.name仍然可以访问
# Student

del testS.name  # 如果删除实例name的属性

print(testS.name)  # 再次调用testS.name，由于实例的name属性没有找到，类的name属性就显示出来了
# name
"""

"""
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性

但是当你删除实例属性后，在使用相同的名称，访问到的将是类属性
"""

# 练习：为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')