# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
#
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
#
# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：
"""
>>> import os
>>> os.name
'posix'
"""''

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#
# 要获取详细的系统信息，可以调用uname()函数：
"""
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='xiafudeAir.lan', release='21.6.0', version='Darwin Kernel Version 21.6.0: Sat Jun 18 17:05:47 PDT 2022; root:xnu-8020.140.41~1/RELEASE_ARM64_T8101', machine='arm64')
"""

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
"""
>>> os.environ
environ({'PATH': '/Users/xiafu/py_workspace/les01/venv/bin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin', 'MANPATH': '/opt/homebrew/share/man::', 'HOMEBREW_PREFIX': '/opt/homebrew', 'COMMAND_MODE': 'unix2003', 'PS1': '(venv) ', 'PYDEVD_LOAD_VALUES_ASYNC': 'True', 'LOGNAME': 'sherrinford16', 'HOMEBREW_REPOSITORY': '/opt/homebrew', 'XPC_SERVICE_NAME': 'application.com.jetbrains.pycharm.ce.12753659.14022999', 'PWD': '/Users/xiafu/py_workspace/les01', 'PYCHARM_HOSTED': '1', 'INFOPATH': '/opt/homebrew/share/info:', '__CFBundleIdentifier': 'com.jetbrains.pycharm.ce', 'PYTHONPATH': '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/third_party/thriftpy:/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev:', 'SHELL': '/bin/zsh', 'OLDPWD': '/', 'HOMEBREW_CELLAR': '/opt/homebrew/Cellar', 'USER': 'sherrinford16', 'IPYTHONENABLE': 'True', 'TMPDIR': '/var/folders/43/wz85c71n5qd_4zvt8c0g_1qr0000gn/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.aIRI75YGzA/Listeners', 'VIRTUAL_ENV': '/Users/xiafu/py_workspace/les01/venv', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'LC_CTYPE': 'zh_CN.UTF-8', 'HOME': '/Users/sherrinford16'})
"""

#要获取某个环境变量的值，可以调用os.environ.get('key')：
"""
>>> os.environ.get('PATH')
'/Users/xiafu/py_workspace/les01/venv/bin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin'
>>> os.environ.get('x', 'default')
'default'
"""


# 操作文件和目录:
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
"""
# 查看当前目录的绝对路径：
>>> os.path.abspath('.')
'/Users/xiafu/py_workspace/les01'

# 在某个目录下创建新目录，首先把新目录的完整目录表示出来：
>>> os.path.join('/Users/xiafu/py_workspace/les01', 'testdir')
'/Users/xiafu/py_workspace/les01/testdir'

# 然后创建一个目录：
>>> os.mkdir('/Users/xiafu/py_workspace/les01/testdir')  # finder中可以看到les01下的新文件夹testdir

# 删掉一个目录：
>>> os.rmdir('/Users/xiafu/py_workspace/les01/testdir')  # testdir被删除
"""

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
#
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
"""
part-1/part-2
"""

# 而Windows下会返回这样的字符串：
"""
part-1\part-2
"""

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
"""
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
"""

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
"""
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')  # 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
"""

# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
"""
# 对文件重命名：
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
"""

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。


# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
"""
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['9_IO编程', '4_函数式编程', '7_面向对象高级编程', '8_错误调试测试', '3_高级特性', '5_模块', '__pycache__', '1_Python基础', '6_面向对象编程', 'venv', '2_函数', '.idea']
"""

# 要列出所有的.py文件，也只需一行代码：
"""
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['hello.py', 'main.py']
"""

# 小结：
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

# 练习：
# 1.利用os模块编写一个能实现dir -l输出的程序。
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
