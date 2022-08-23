# 文档测试
# python的官方文档中，许多文档都有实例代码。比如re模块就带了很多示例代码：
"""
# PyDev console: starting.
# Python 3.9.1rc1 (v3.9.1rc1:88db374422, Nov 24 2020, 17:00:47) 
# [Clang 12.0.0 (clang-1200.0.32.27)] on darwin

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
'def'
"""''

# 可以把这些示例代码在python的交互环境下输入并执行，结果与文档中的实例代码显示的一致。

# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？

# 可以的，下面是例子：
def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)

# 无疑更明确地告诉函数的调用者该函数的期望输入和输出。

# 并且，python内置的"文档测试(doctest)"模块可以直接提取注释中的代码并执行测试。

# doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。

# 在mydict2.py中测试上次编写的Dict类。
"""
**********************************************************************
1 items had failures:
   2 of   9 in __main__.Dict
***Test Failed*** 2 failures.

注意到最后三行代码。当模块正常导入时，doctest不会执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。
"""

# 练习：对函数fact(n)编写doctest并执行：

# 小结：
# doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。
# 用户看文档的时候，同时也看到了doctest