# StringIO和BytesIO

# stringIO 比如说，这时候，你需要对获取到的数据进行操作，但是你并不想把数据写到本地硬盘上，这时候你就可以用stringIO
from io import StringIO
from io import BytesIO
def outputstring():
    return 'string \nfrom \noutputstring \nfunction'

s = outputstring()

# 将函数返回的数据在内存中读
sio = StringIO(s)
# 可以用StringIO本身的方法
print(sio.getvalue())
# 也可以用file-like object的方法
s = sio.readlines()
print('s:', s)
for i in s:
    print(i.strip())


# 将函数返回的数据在内存中写
sio = StringIO()
sio.write(s)
# 可以用StringIO本身的方法查看
s=sio.getvalue()
print(s)

# 如果你用file-like object的方法查看的时候，你会发现数据为空
""" ！问题出处！ """
sio = StringIO()  # 当使用StringIO()去初始化的时候，其指针是指向0的位置
sio.write(s)  # 而如果是用write的方法的时候，其指针则是会移动到后面的
""" ！问题出处！ """
for i in sio.readlines():
    print(i.strip())

# 这时候我们需要修改下文件的指针位置
# 我们发现可以打印出内容了
sio = StringIO()
sio.write(s)
sio.seek(0,0)
print(sio.tell())
for i in sio.readlines():
    print(i.strip())

# 这就涉及到了两个方法seek 和 tell
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦



# stringIO 只能操作str，如果要操作二进制数据，就需要用到BytesIO
# 上面的sio无法用seek从当前位置向前移动，这时候，我们用'b'的方式写入数据，就可以向前移动了
bio = BytesIO()
bio.write(s.encode('utf-8'))
print(bio.getvalue())
bio.seek(-36,1)
print(bio.tell())
for i in bio.readlines():
    print(i.strip())


"""
其实层主这里之所以文件的指针位置需要修改，是因为涉及到一个没有被提及的小知识点：

当使用StringIO()去初始化的时候，其指针是指向0的位置；而如果是用write的方法的时候，其指针则是会移动到后面的。

举例如下：

sio = StringIO('abc') 
sio.getvalue() 
'abc' 
sio = StringIO('def') 
sio.getvalue() 
'def'

上面这里显示使用StringIO()进行初始化，是覆盖原值的，指针始终是指向0的位置。

对比write的方法：

a = StringIO() 
a.write('123') 
3 
a.getvalue() 
'123' 
a.write('456') 
3 
a.getvalue() 
'123456'

可以看出，write的方法本质上是追加。

再举例如下：

sio = StringIO('abc')  # 这里是初始化，指针指向0 
sio.getvalue() 
'abc'
sio = StringIO('def')  # 这里是再次初始化，指针仍然指向0
# sio.getvalue() 
'def'  # def覆盖原值abc
# sio.write('ghi')  # 这里要注意了，虽然是追加，但是由于指针仍然是0，所以实际上仍然会覆盖掉原值3
# sio.getvalue() 
'ghi' 
sio.write('ghi')  # 上面第一次追加以后，指针就向后移动，所以此处才真正起到追加的效果3 
sio.getvalue() 
'ghighi'
"""