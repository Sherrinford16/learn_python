"""
2022/7/11
开始啃廖雪峰的python课程
"""

# print('''start
# 1
# 2
# 3''')

# print(r'''hello,\n
# world''')

# a = 'abc'
# b = a
# a = 'ABC'
# print(b)

# r' 不需要转译来输出字符
# n = 123
# f = 456.789
# s1 = 'Hello, World'
# s2 = 'Hello, \'Sher\''
# s3 = r'Hello, "John"'
# s4 = r'''Hello,
# Lly!'''
# print(s2)

# 编码
# print('包含中文的str')
# print(ord('夏'))
# print(chr(22799))
# print('\u590f')

# print('abc'.encode('ascii'))
# print('夏福'.encode('utf-8'))
# print(b'\xe5\xa4\x8f\xe7\xa6\x8f'.decode('utf-8'))

"""
格式化
1. 输出格式化的字符串 %
'Hi %s, your score is %d.' %('Sher', 16)
常见占位符
%d %f %s %x
%%转译为%

2. format(): 用传入的参数依次替换字符串内的占位符 ps. {0} 不从零开始会报错
3. f-string: 以f开头的字符串, 字符串如果包含{xxx}, 就会以对应的变量替换
"""
# print('%03d-%03d' % (10, 3))
# print('some message {0} {1} {2:.2f}%'.format('a', 'b', 3.1415))
# r = 1.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')

# 练习
# s1 = 75
# s2 = 85
# r = ((s2 - s1) / s1) * 100
# print(f'上涨了{r:.1f}%')
# print('上涨了{0:.1f}%'.format(r))
# print('上涨了%.1f%%' % r)
