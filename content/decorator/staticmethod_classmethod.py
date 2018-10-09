import os

# 获取当前目录的上层目录
def top_path(*, p=__file__, n=1):
    p = os.path.abspath(p)
    for _ in range(n):
        p = os.path.dirname(p)
    return p

# 目录的连接和创建
def path_init(p, name):
    path = os.path.join(p, name)
    if not os.path.exists(path):
        os.mkdir(path)
    return path


# 需求一
# 1.函数可以直接调用；
# 2.函数可以被类中的属性或方法调用。
# 注意：这种方式有缺点，比如：
# 1.top_path这个函数只想被类内部的属性方法调用，
# 将其放在类外部，将导致代码维护性变差。
# 2.子类在继承该类后，不能够直接继承该函数。
class Origin(object):
    # 根目录
    root = top_path(n=1)
    def __init__(self, app_name = 'Temp'):
        self.app = path_init(self.root, app_name)


# 需求二：
# 方法(current)只能通过类被调用，禁止实例化对象调用
# 注意：这种方法缺点是：
# 1.如非特殊需要，该写法不能够被类的实例化对象调用。
class Own(object):
    def current():
        root = top_path(n=1)
        return os.listdir(root)


# 需求三
# 方法(current)只能通过实例化对象调用，禁止类直接调用
# 注意：这个方法并不是真的禁止调用了
# 注意：该方法传入了一个看起来没有使用的参数self，
# 这将导致编辑器产生警告，通常不建议这么做。
class UserComplex(object):
    def current(self):
        root = top_path(n=1)
        return os.listdir(root)


# 需求三：暂时没有找到好的解决办法
# 方法(current)只能通过实例化对象调用，禁止类直接调用
class User(object):
    pass




# 需求四
# 注意：使用静态方法的场景：
# 1.写的方法既想通过类名直接调用，也想通过实例化对象调用；
# 2.方法中引用的变量没有涉及到类名本身。
# 方法既可通过类调用，也可通过实例化对象调用
class Manager(object):
    @staticmethod
    def current():
        root = top_path(n=1)
        return os.listdir(root)


# 以上代码相当于：
class Manager(object):
    def current():
        root = top_path(n=1)
        return os.listdir(root)
    current = staticmethod(current)

# 官网上纯Python版的staticmethod定义如下：
class StaticMethod(object):
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

# 需求五
# 注意：使用类方法的场景：
# 1.写的方法既想通过类名直接调用，也想通过实例化对象调用；
# 2.写的方法中引用的变量涉及到了类名本身。
# 为了防止出现硬编码的情况出现，故使用。
class Chairman(object):
    @classmethod
    def pursuit(cls):
        return cls.__name__


# 以上代码相当于：
class Chairman(object):
    def pursuit(cls):
        return cls.__name__
    pursuit = classmethod(pursuit)

# 官网上的纯Python版的classmethod定义如下：
class ClassMethod(object):
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc


# 官网上给出了一个classmethod的使用场景：
class Dict(object):
    ...
    def fromkeys(klass, iterable, value=None):
        "Emulate dict_fromkeys() in Objects/dictobject.c"
        d = klass()
        for key in iterable:
            d[key] = value
        return d
    fromkeys = classmethod(fromkeys)

if __name__ == '__main__':
    # 注意：此处仅是调用办法的示例，
    # 由于代码部分省略，并不能真的调用，
    # 如果想调用，还需要实现其它方法。
    #print(Dict.fromkeys('abc'))
    # 以上调用将打印：
    # {'a': None, 'b': None, 'c': None}
    pass


if __name__ == '__main__':
    # 需求一
    #print(top_path(n=1))
    #origin = Origin()
    #print(Origin.root)
    #print(origin.root)
    #print(origin.app)
    # 需求二
    #print(Own.current())
    #own = Own()
    #print(own.current())  # TypeError
    # 需求三
    #user_complex = UserComplex()
    #print(user_complex.current())
    #print(UserComplex.current())  # TypeError
    # 实际上还是可以调用的，比如这样调用：
    #print(UserComplex.current(UserComplex))
    # 还可以这样调用：
    #print(UserComplex.current(UserComplex()))
    # 甚至可以这样调用：
    #print(UserComplex.current(Origin))
    # 可以这样调用：
    #print(UserComplex.current(Origin()))
    # 只要传入了一个类或对象，就都可以调用
    #print(UserComplex.current(str))
    #print(UserComplex.current(type))
    #print(UserComplex.current('abc'))
    # 需求三：此处未找到实现方法
    #user = User()
    # 需求四：使用staticmethod
    #manager = Manager()
    #print(manager.current())
    #print(Manager.current())
    # 这个时候再想随意传个类或实例调用就不行了：
    #print(Manager.current(str))  # TypeError
    # 需求五：使用classmethod
    #chairman = Chairman()
    #print(chairman.pursuit())
    #print(Chairman.pursuit())
    pass





# ========================================
# @staticmethod 和 @classmethod 的使用

# 根据上面所述(请查看帮助：help(staticmethod))，
# 静态方法和类方法是为了解决以下问题而设置的：
# 1.防止仅被该类使用的代码外露，有益于代码维护；
# 2.静态方法避免显式传入self，更符合编码规范；
# 3.类方法避免硬编码类名，更符合编码规范；
# 4.可使子类更好地继承这些相关函数功能；
# 因为有装饰器标识，可以让代码更易阅读：
# 6.一看就知道哪些是和类无关的代码(专指静态方法)，
# 7.哪些又是和类有关的代码(专指类方法)。
# 8.可以使调用更加方便：既可以用类名调用，
# 也可以总类的实例化对象调用。
# ----------------------------------------
# 以下我将依次说明这些问题：
# 类方法：classmethod

# 首先，我们编写一个日期类用于说明此问题：

class Date(object):
    def __init__(self, years=0, months=0, days=0):
        self.years, self.months, self.days = years, months, days

    def __str__(self):
        return '({years}, {months}, {days})'.format(**self.__dict__)

    @classmethod
    def fromstr(cls, strdate):
        return cls(*map(int, strdate.split('-')))

if __name__ == '__main__':
    #print(Date(2018, 10, 9))
    #print(Date.fromstr('2018-10-01'))

    #date = Date(2018, 10, 5)
    #print(date)
    # 如果想要更改日期，则创建一个新实例对象：
    #new_date = date.fromstr('2018-10-03')
    #print(new_date)
    # 并不会影响原来的实例：
    #print(date)
    del Date

# 因fromstr方法中引用的变量涉及到类名，
# 防止硬编码类名等问题，故使用classmethod。
# 如果不使用classmethod，可能要这样写：

class Date(object):
    def __init__(self, years=0, months=0, days=0):
        self.years, self.months, self.days = years, months, days

    def __str__(self):
        return '({years}, {months}, {days})'.format(**self.__dict__)

    def fromstr(strdate):
        return Date(*map(int, strdate.split('-')))

if __name__ == '__main__':
    #print(Date(2018, 10, 9))
    #print(Date.fromstr('2018-10-01'))
    del Date

# 以上是硬编码示范，这种编写方式不利于代码维护，
# 如果某人更改了名称，是很难意识到会改变代码功能的。
# 或者这样写：

class Date(object):
    def __init__(self, years=0, months=0, days=0):
        self.years, self.months, self.days = years, months, days

    def __str__(self):
        return '({years}, {months}, {days})'.format(**self.__dict__)

    def fromstr(self, strdate):
        return self(*map(int, strdate.split('-')))

# 以上的写法看起来不再硬编码了吧？
# 但是！如果想要调用，就必须硬编码了：

if __name__ == '__main__':
    #print(Date(2018, 10, 9))
    #print(Date.fromstr(Date, '2018-10-01'))
    date = Date(2018, 9, 12)
    # 想要用实例化对象调用吗？然而并不能：
    # print(date.fromstr('2018-05-03')) # TypeError
    del Date

# 这样导致使用这个类的代码硬编码了，自然也不利于维护。
# 可能，仔细思考一下，干嘛不直接自己处理前期工作呢：

def fromstr(cls, strdate):
    return cls(*map(int, strdate.split('-')))

class Date(object):
    def __init__(self, years=0, months=0, days=0):
        self.years, self.months, self.days = years, months, days

    def __str__(self):
        return '({years}, {months}, {days})'.format(**self.__dict__)

if __name__ == '__main__':
    #print(Date(2018, 10, 9))
    #print(fromstr(Date, '2018-10-01'))
    # 如果想创建新日期，只能这样：
    del Date

# 看起来fromstr是个未涉及类自身变量(self.years等)，
# 也未涉及类本身的名称，可以欣然接受了，
# 但是，一方面这种办法导致和类相关的预处理函数外露，
# 另一方面又对子类的继承造成了麻烦(需要重写)，
# 同时，又需要频繁使用类名称创建新日期。


# ========================================
# 静态方法：staticmethod









