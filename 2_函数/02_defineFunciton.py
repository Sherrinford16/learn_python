# 在python中，定义一个函数要使用def语句，一次写出函数名、括号、括号中的参数和冒号 :
# 然后在缩进块中编写函数体，函数的返回值用return语句返回
# 下例 自定义一个求绝对值的my_abs函数
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(-1213))
# 提示 代码规范:expected 2 blank lines after class or function definition
"""
注意！函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
因此，函数体内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。 return None可以简写为return
在python交互环境中定义函数时，注意python会出现...提示。函数定义结束后需要按两下回车重新回到>>>提示符下(PyCharm不必
"""

"""
如果已经把my_abs()的函数定义保存为abstest.py文件了，那么可以在该文件的当前目录下启动Python解释器，
用 from abtest import my_abs来导入my_abs()函数，注意abtest是文件名(不含.py扩展名)
"""

# 空函数：如果想定义一个什么也不做的空函数，可以使用pass语句
# def nop():
#     pass

# pass语句什么都不做，作用呢？实际上pass可以用来作为占位符，
# 比如未想好怎么写函数的代码，就可以先放一个pass，让代码运行起来
# pass还可以用在其他语句里，比如：
# if age1 > 18:
#     pass
# 缺少了pass就会报错

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# my_abs(1, 2)
# TypeError: my_abs() takes 1 positional argument but 2 were given
# my_abs('a')
# line 39, in < module >my_abs('a')
# line 5, in my_abs if x >= 0:
# TypeError: '>=' not supported between instances of 'str' and 'int'
# abs('a')
# TypeError: bad operand type for abs(): 'str'
"""
my_abs()和abs()报错竟然不同
原因：当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查。
会导致if语句出错，出错信息和abs不一样。所以，my_abs函数还不够完善
"""
# 修改my_abs的定义，对参数类型做检查，只允许int和float类型的参数。
# 数据类型检查可以用内置函数isinstance()实现
# def new_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(new_abs('xx'))
# TypeError: bad operand type

""" 挖坑：错误处理和异常处理 """

# 返回多个值
# 例子：游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标:
"""
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

a, b = move(10, 10, 6, math.pi / 3)
print(a, b)
# 13.0 15.196152422706632
"""
# 但其实这只是一种假象，python函数返回的仍然是单一值
"""
r = move(10, 10, 6, math.pi / 3)
print(r)
# (13.0, 15.196152422706632)
"""
# !!!原来返回值是一个tuple。但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值
# 所以，其实python的函数返回多个值，其实就是返回一个tuple，但写起来更方便


# 练习：请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax^2+bx+c=0 的两个解
import math
def quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    else:
        print('方程无解')

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
print(quadratic(2, 3, 1))