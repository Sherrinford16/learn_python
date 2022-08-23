# 条件判断 if elif else
# age = 12
# if age > 18:
#     print('adult')
# elif age >= 14:
#     print('teenager')
# else:
#     print('child')

"""
# 一个input() 产生的error
birth = input('请输入出生年份: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
    
Traceback (most recent call last):
  File "/Users/xiafu/py_workspace/les01/03_if_else.py", line 12, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
"""
# 原因分析 input()返回的数据类型为str, 不能直接和整数比较, 必须先吧str转换成整数
# python中提供了int()函数来完成
# ori_birth = input('请输入出生年份: ')
# birth = int(ori_birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
"""
# 当输入'a'呢? 
Traceback (most recent call last):
  File "/Users/xiafu/py_workspace/les01/03_if_else.py", line 26, in <module>
    birth = int(ori_birth)
ValueError: invalid literal for int() with base 10: 'a'
int()函数发现一个字符串并不是合法的数字时就会报错, 程序就退出了
"""

# 练习
"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""

height = 1.75
weight = 80.5

bmi = weight / (height ** 2)
# print(f'{bmi:.1f}')
# print(bmi)
if bmi > 32:
    print('yzfp')
elif bmi >= 28:
    print('fp')
elif bmi >= 25:
    print('gz')
elif bmi >= 18.5:
    print('zc')
else:
    print('gq')
