# python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
# 以内建的sys模块为例，编写一个hello的模块：
"""_"""

# !/usr/bin/env python3
# 第一行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
# -*- coding: utf-8 -*-
# 表示.py文件本身使用标准UTF-8编码；

'a test module'
# 表示模块的文档注释，任何模块的第一个字符串都被视为模块的文档注释

__author__ = 'XiaFu'
# 使用__author__把作者写进去。。
# 以上就是python模块的标准文件模版，当然也可以全部删掉不写，但是，按标准办事肯定没错。后面开始就是真正的代码部分。

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

#  __name__有两个取值：当模块是被调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为__main__
"""
# 使用sys模块的第一步，就是导入该模块：
import sys
# 导入sys模块后，我们就有了一个变量指向该模版，利用sys这个变量，就可以访问sys模块的所有功能。
# sys模块有一个arg变量，用list存储了命令行的所有参数。
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称。例如：
# 运行 python3 01_usingModule.py 获得的sys.argv就是 ['01_usingModule.py']
# 运行 python3 01_usingModule.py XiaFu 获得的sys.argv就是 ['01_usingModule.py', 'XiaFu']

if __name__ == '__main__':
    test()
# 注意这两行
# 当我们在命令行运行hello模块文件时，python解释器把一个特殊变量__name__置为__main__ ，
# 而如果在其他地方导入该hello模块文件时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。

# 我们可以用命令行运行hello.py看看效果：
$ python3 hello.py
Hello, world!
$ python hello.py XiaFu
Hello, XiaFu

# 如果启动python交互环境，再导入hello模块：
import hello
# 导入时，没有打印 Hello, world! 因为没有执行test()函数
# 调用hello.test()时，才能打印出 Hello, world!
>>>hello.test()
Hello, world!
"""

# 作用域
"""
# 在一个模块中，我们可以定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在python中，是通过_前缀来实现的。

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以直接被引用，但是有特殊用途，比如上面的__author__, __name__就是特殊变量，
# hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

# 类似_x和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如：_abc, __abc等；

# 之所以我们说，private函数和变量"不应该"被引用，而不是"不能"被引用，是因为python并没有一种方法可以完全限制访问private函数或变量，
# 但是，从编程习惯上不应该引用private函数或变量。
"""

# private函数或变量不应该被引用，那他们有什么用？例子：
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

"""    
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，
# 这也是一种非常有效的代码封装和抽象的方法，即：

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
"""