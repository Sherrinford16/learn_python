# 调试
"""
程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。

有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。
"""''
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
"""
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

>>> n = 0
...
ZeroDivisionError: division by zero

用print()最大的坏处是将来还得删除它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，有第二种方法。
"""

# 断言
"""
凡是print()来辅助查看的地方，都可以用断言(assert)来替代：
"""
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()
"""
# assert的意思是，表达式 n != 0 应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

# 如果断言失败，assert语句本身就会抛出AssertionError：
AssertionError: n is zero!

# 如果程序中到处充斥着assert，和print()相比也好不到哪去。不过，启动python解释器的时候可以用-O参数来关闭assert
$ python -O err.py
...
ZeroDivisionError: division by zero

！！注意，断言开关"-O"是英文大写字母O，不是数字0

# 关闭后，可以把所有的assert语句当成pass来看。
"""

# logging
"""
# 把print()替换为logging是第三种方式，和assert相比，logging不会抛出错误，而且可以输出到文件：
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


Traceback (most recent call last):
  File "/Users/xiafu/py_workspace/les01/8_错误调试测试/02_调试.py", line 63, in <module>
    print(10 / n)
ZeroDivisionError: division by zero

# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。咋回事？

# 在import logging之后添加一行配置再试试：
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

INFO:root:n = 0
Traceback (most recent call last):
  File "/Users/xiafu/py_workspace/les01/8_错误调试测试/02_调试.py", line 80, in <module>
    print(10 / n)
ZeroDivisionError: division by zero

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。

# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
"""

# pdb
"""
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
s = '0'
n = int(s)
print(10 / n)

# 启动，以参数-m pdb启动后，pdb定位到下一步要执行的代码 -> s = '0' 。
sherrinford16@xiafudeAir 8_错误调试测试 % python -m pdb test8.py
> /Users/xiafu/py_workspace/les01/8_错误调试测试/test8.py(1)<module>()
-> s = '0'

# 输入命令l来查看代码：
(Pdb) l
  1  ->	s = '0'
  2  	n = int(s)
  3  	print(10 / n)
[EOF]

# 输入命令n可以单步执行代码：
(Pdb) n
> /Users/xiafu/py_workspace/les01/8_错误调试测试/test8.py(2)<module>()
-> n = int(s)
(Pdb) n
> /Users/xiafu/py_workspace/les01/8_错误调试测试/test8.py(3)<module>()
-> print(10 / n)
(Pdb) n
ZeroDivisionError: 'integer division or modulo by zero'
> /Users/xiafu/py_workspace/les01/8_错误调试测试/test8.py(3)<module>()
-> print(10 / n)

# 任何时候都可以输入命令 p 变量名 来查看变量：
(Pdb) p s
'0'
(Pdb) p n
0

# 输入命令q结束调试，退出程序：
(Pdb) q
"""

# pdb.set_trace()
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)

# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
"""
> /Users/xiafu/py_workspace/les01/8_错误调试测试/02_调试.py(142)<module>()
-> print(10 / n)
(Pdb) c
Traceback (most recent call last):
  File "/Users/xiafu/py_workspace/les01/8_错误调试测试/02_调试.py", line 142, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
"""

# 这种方法比直接启动pdb单步调试效率高很多，但也高不到哪去
