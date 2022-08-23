# 元类

# type()
""" 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。"""  #


# 比方说我们要定义一个Hello的class，就写一个hello.py模版：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# 当python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，
h = Hello()
h.hello()  # Hello, world.
print('type(h):', type(h))  # type(h): <class '__main__.Hello'>
print('type(Hello):', type(Hello))  # <class 'type'>

"""
type()函数可以查看一个类或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

上面提到class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义。
"""


def fn(self, name='world'):  # 先定义函数
    print('Hola %s.' % name)


Hola = type('Hola', (object,), dict(hello=fn))  # 创建Hello class
h1 = Hola()
h1.hello()  # Hola world.
print('type(Hola):', type(Hola))  # <class 'type'>
print('type(h1):', type(h1))  # <class '__main__.Hola'>

"""
要创建一个class对象，type()函数一次传入3个参数：

1。class的名称
2。继承的父类集合，注意python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3。class的方法名称和函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为python解释器遇到class定义时，仅仅是扫描以下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，
这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
"""

# metaclass
"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，元类，简单解释为：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的"实例"。

metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。

正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
"""


# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模版，所以必须从'type'类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass


"""
当我们传入关键字参数metaclass时，魔术就生效啦，它指示python解释器在创建List时，要通过ListMetaclass.__new__()来创建，
在此我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数一次是：
1.cls 当前准备创建的类的对象；
2.name 类的名字；
3.bases 类继承的父类集合；
4.attrs 类的方法集合。
"""

# 测试一下MyList是否可以调用add()方法：
L = MyList()
L.add(1)
print(L)  # [1]

# 而普通的list没有add()方法：
L2 = list()
# L2.add(1)  # AttributeError: 'list' object has no attribute 'add'

"""
动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下确实应该直接写，通过metaclass修改纯纯bt

但是总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

ORM全称"Object Relational Mapping"，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

来尝试编写一个ORM模型。

编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User

# 期待写出的代码
class User(Model):
    id = IntergerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Sher', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由父类Model自动完成。
# 虽然metaclass的编写比较复杂，但ORM的使用者用起来却非常简单。
# 现在，我们就按上面的接口来实现该ORM。
"""


# 首先来定义Field，它负责保存数据库表的字段名和字段类型：
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField、IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 下一步,就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# 以及基类Model：
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s ' % str(args))


"""
# 当用户定义一个class User(Model)时，python解释器先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

在ModelMetaclass中，一共做了几件事情：

1.排除掉对Model类的修改；

2.在当前类（比如User）中查找定义的类的属性的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）

3.把表名保存到__table__中，这里简化为表名默认为类名。

在Model类中，就可以定义各种操作数据库的方法，比如save(), delete(), find(), update()等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
"""


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Sher', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
# 可以看到，save()方法已经打印出了可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能。

# ？？不到100行代码，我们就通过metaclass实现了一个精简的ORM框架，是不是非常简单？？


"""

# metaclass这章对ModelMetaclass的讲解有许多不理解的地方。评论区先看看大家对问题的归纳和总结：

一个分为四步解释：定义Field类、StringField类和IntegerField类；定义Model类和User类；创建User类的实例u；执行u.save();

第一步：定义Field类、StringField类和IntegerField类。
这里需要注意的是，super()的作用是调用父类的方法。Field类中的__str__方法可以让实例在print语句中打印出特定的格式。

第二步：定义Model类和User类。

首先，定义时都调用了ModelMetaclass的__new__方法。在定义Model类的时候调用了一次，定义User类的时候又调用了一次。

在定义Model类时，因为__new__方法中的if语句
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

所以直接返回了，没有执行后续的语句。

而在定义User类时，注意，User类先定义了四个属性：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

这一次调用__new__函数，跳过了if语句，继续执行：
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

执行后，mappings的值是，
{"id": IntegerField的实例, "name": StringField的实例, "email": StringField的实例, "password": IntegerField的实例}，
就相当于把User类自带的四个属性存到了mappings里。

然后：
        for k in mappings.keys():
            attrs.pop(k)
            
又把这四个属性删掉了，如果现在随便写两行，创建一个User类实例：
u = User()
print(u.id)

这时候会报错，不能用实例.属性的方法来调用这四个属性。

那可以调用什么呢？接下来：
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        
这两行在User类中新加了两个属性，__mappings__和__table__。

这时，创建一个User类的实例，是可以用实例.__mappings__来获得之前mappings存放的内容的。

至此，Model和User类创建完了，接下来开始创建实例。

第三步：创建User类的实例u。

首先，在执行u = User(id=12345, name='Sher', email='test@orm.org', password='my-pwd')的时候，
需要__init__函数来生成实例，User类中没有，它继承Model类中的__init__函数：
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

super()语句能调用父类的方法，而Model的父类是dict，因此，执行上述的u = User(...)就相当于执行：
u = dict(id=12345, name='Sher', email='test@orm.org', password='my-pwd')

现在，u就是一个字典，可以用u[id], u[name], u[email], u[password]的方式调用具体的值。

第四部：执行u.save()
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s ' % str(args))

save()的目标是，根据第一步__mappings__中保存的"类的属性"与"数据库的列"的映射，把实例的数据读取出来，变成一条数据库指令。

注意，现在还不能用实例.id，实例.username的方法读数据，而是要用实例[id]，实例[username]来读，因为现在u是一个字典。

可是，程序例却是：
    args.append(getattr(self, k, None))
而没有直接用：
    args.append(self[k])
这是为什么呢，这是因为输入的实例可能会缺少某项数据，例如这样：
u = User(id=121, name='someone')

删掉了email和password，这个时候调用u[email]或者u[password]，就会报错。

所以，更好的方式是，在Model类中设置__getattr__方法，用实例.email, 实例.password的方法来调用。这样就可以判断实例中有没有要查找的属性了。

因此，Model类中会有这一段代码：
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
            
再结合读取数据的语句：
    args.append(getattr(self, k, None))

None这一位参数表示如果拿不到参数k，自动返回None，不用担心实例中少某项数据的问题了。

最后提一下为什么在ModelMetaclass类中要：
        for k in mappings.keys():
            attrs.pop(k)

如果没有这两句，那么User类下面定义的四个属性：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    
会一直保留。这样的话，在调用args.append(getattr(self, k, None))的时候，

因为id, name, email, password这四个属性本来就有(它们是类自带的属性)，就不会执行getattr(self, k, None)，

本来是什么值就赋什么值。那这有什么问题呢？

注意，这四个属性现在对应的值是IntegerField, StringField, StringField, IntegerField，而真正要读取的数据在getattr()里：
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
            
要读的是装在self['id'], self['name'], self['email'], self['password']里的12345, 'Sher', 'test@orm.org', 'my-pwd'.

因此，必须要能执行getattr()才能拿到正确的数据。

这一句:
for k in mappings.keys():
    attrs.pop(k)
就起作用了。在创建User类的时候，把这四个类的属性踢掉，getattr就会执行，就能顺利读到self[key]的值了。

这也就是"实例的属性会遮盖类的同名属性"的含义。
"""