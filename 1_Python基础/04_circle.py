# 循环 for / while

# 1.for...in循环 依次把list或tuple中的每个元素迭代出来
# items = ['goodsA', 'goodsB', 'goodsC']
# for item in items:
#     print(item)

# Sum = 0
# for num in [1, 2, 3, 4, 5]:
#     Sum += num
# print(Sum)

# python提供了range()2_函数, 可以用来生成整数序列
# 再通过list()函数转换为list
# newList = list(range(-4, 0))
# print(range(5))
# print(newList)

# 高斯来计算一下1-100累加
# newSum = 0
# for x in range(101):
#     newSum += x
# print(newSum)

# 2.while循环 只要条件满足, 就不断循环, 直至条件不满足跳出循环
# newSum = 0
# n = 99
# while n > 0:
#     newSum += n
#     n -= 2
# print(newSum)

# 练习 请利用循环依次对list中的每个名字打印出Hello, xxx!
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print(name)

# 3.break 在循环中, break语句可以提前退出循环
# n = 1
# while n <= 16:
#     print(n)
#     n += 1
# print('end: ', n)
#
# m = 1
# while m <= 16:
#     if m > 10:
#         break
#     print(m)
#     m += 1
# print('end: ', m)

# 4.continue 跳过当前的这次循环, 直接开始下一次循环
# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)