# python内置了许多函数，我们可以直接调用
# 调用一个函数，需要知道函数的名称和参数，例如求绝对值函数abs，只有一个参数
# http://docs.python.org/3/library/functions.html#abs 官方文档
# td1 = abs(100)
# print(td1)
# td2 = abs(-13.14)
# print(td2)

# 调用函数时，若传入的参数数量不对，会报错TypeError
# td3 = abs(1, 2)
# print(td3)
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/2_函数/01_callFunction.py", line 9, in <module>
#     td3 = abs(1, 2)
# TypeError: abs() takes exactly one argument (2 given)

# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报错TypeError
# td4 = abs('a')
# print(td4)
# Traceback (most recent call last):
#   File "/Users/xiafu/py_workspace/les01/2_函数/01_callFunction.py", line 22, in <module>
#     td4 = abs('a')
# TypeError: bad operand type for abs(): 'str'

# max()函数可以接收任意多个参数，并返回最大的那个：
# td5 = max(1, 2, 0, -4, -5)
# print(td5)

# 数据类型转换
# int()函数可以把其他数据类型转换为整形 str() float() bool()
# td6 = int('123')
# print(td6)
# td7 = int(1.33)
# print(td7)
# td8 = float('1.23')
# print(td8)
# td9 = str(1.02)
# print(td9)
# td10 = bool(1)
# print(td10)
# td11 = bool('')
# print(td11)

# 函数名其实就是指向一个函数对象的引用，完全可以吧函数名赋给一个变量，相当于给函数起了个"别名"
# a = abs
# print(a(-1))
# print(abs(-1))

# 练习 使用python内置的hex()函数把一个整数装换成十六进制表示的字符串
n1 = 255
n2 = 1000
print('n1: ', hex(n1), 'n2: ', hex(n2))
