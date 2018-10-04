# coding=utf-8
# ==========================================
# 编写用途：介绍装饰器decorator的使用
# ==========================================
# 装饰器作用：在一个函数的调用前后执行一些代码，而不用修改函数本身
# 注意：装饰器分类：存在两种装饰器：函数装饰器、类装饰器；
# 注意：多个装饰器的调用顺序：从下到上依次调用装饰器；
# 注意：装饰器执行时机：碰到@装饰器时开始装饰，但并不调用；
# 注意：装饰器被装饰到函数上，
# 只要该函数被检测到，装饰器的第一层就会执行，
# 所以，除非必要，则必须把功能代码全部放到wrapper函数内
# ==========================================
# 用于辅助说明的模块
import time
# ---------------------------------
import functools
# ==========================================
# 给一个函数增加两个装饰器

def makebold(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"
# ==========================================
# 我的第一个装饰器：装饰器的定义和使用

# 装饰器：传入目标函数，并定义和返回包装器的函数
def my_first_decorator(func):
    # 包装器：装饰器里面用于包装目标函数的函数
    def my_first_wrapper():
        print('Before the function runs')
        # 调用传入的函数
        func()
        print('After the function runs')
    return my_first_wrapper

@my_first_decorator
def my_first_hello():
    print('hello world')

# ==========================================
# 我的第二个装饰器：同时调用多个装饰器，以及装饰器的执行顺序

def my_second_decorator(func):
    def my_second_wrapper():
        print('Nice to meet you')
        func()
        print('Good bye')
    return my_second_wrapper

# 执行顺序：
# 首先执行最上面的装饰器要求在函数执行前执行的代码，
# 然后执行下面的装饰器要求在函数执行前执行的代码；
# 接着执行最上面的装饰器要求在函数执行后执行的代码，
# 最后执行下面的装饰器要求在函数执行后执行的代码
# 注意：同一个装饰器可以同时多次使用
@my_first_decorator
@my_second_decorator
@my_first_decorator
def my_second_hello():
    print('hello world')

# ==========================================
# 装饰器的高级用法一：传入参数

def my_third_decorator(func):
    def my_third_wrapper(arg1, arg2):
        print('Today, I met two friends:{} and {}'.format(arg1, arg2))
        print('We greeted each other:')
        func(arg1, arg2)
        print('And we said goodbye to each other.')
    return my_third_wrapper


@my_third_decorator
def my_third_hello(name1, name2):
    print('Hello {}'.format(name1))
    print('Hello {}'.format(name2))

# ==========================================
# 装饰器的高级用法二：参数不定数量的装饰器

def my_fourth_decorator(func):
    def my_fourth_wrapper(*args, **kwargs):
        for arg in args:
            print('Nice to see you again, {}'.format(arg))
        func(*args, **kwargs)
    return my_fourth_wrapper



@my_fourth_decorator
def my_fourth_hello(*args, **kwargs):
    for arg in args:
        print('{}, this is your wage'.format(arg))
        for key, word in kwargs.items():
            print('{}, your salary of {} is {}'.format(arg, key, word))

# ==========================================
# 装饰器的进阶用法一：装饰一个装饰器
# 注意：最好将所有功能在包装器中完成，不要放在装饰器或装饰装饰器的函数块中完成，
# 否则，装饰装饰器的部分代码可能在被包装函数未被调用时执行，即会在定义时执行

# ！！注意！！这个是错误示范，功能代码不要放在装饰器最外层，
# 否则，其中的代码会被执行，其中的变量会被保存
def make_a_decorator():
    print('I made a decorator when {}!'.format(time.strftime('%H:%M:%S')))
    for i in range(3, 0, -1):
        print('({})Running decorator...'.format(i))
        time.sleep(1)
    def decorator(func):
        def wrapper():
            func()
            print('Goodbye')
        return wrapper
    return decorator


# 使用装饰装饰器的装饰器
# 注意：@make_a_decorator()是一个调用语句，
# 不管first_advanced_hello是否调用，
# @make_a_decorator()的外层代码都会在首次调用时被执行
'''
@make_a_decorator()
def first_advanced_hello():
    print('Hello')'''

# ==========================================
# 装饰器的进阶用法二：为装饰装饰器的装饰器传入参数
def make_a_decorator_with_argument(arg):
    def decorator(func):
        def wrapper():
            print('I made a decorator when {}!'.format(time.strftime('%H:%M:%S')))
            print('I caught a {} in forest'.format(arg))
            func()
            print('Goodbye')
        return wrapper
    return decorator

@make_a_decorator_with_argument('fox')
def second_advanced_hello():
    print('Hello')

# ==========================================
# 装饰器的进阶用法三

def retry_decorator(prompt='错误，请重试', retry=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(kwargs)
            for times in range(retry, 1, -1):
                try:
                    func(*args, **kwargs)
                    break
                except Exception as e:
                    print(f'[{times}]'+prompt)
                    print(e)
        return wrapper
    return decorator
# ==========================================
# 装饰器编写的注意事项一：被装饰函数的函数名被改变
# 用functools.wraps()
# 或用直接修改：wrapper.__name__ = fun.__name__

# ---------------------------------
# functools中的三个装饰器的实现

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
WRAPPER_UPDATES = ('__dict__',)
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    for attr in assigned:
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    return wrapper


def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)

# ---------------------------------
# 当用通常的装饰器装饰函数时，函数的函数名等会被修改
# 请看以下例子：

# 计算函数运行时间：用于评估算法效率
# 注意：此处函数名不符合PEP规范，请勿模仿
def _1_timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('----- usetime ---- funcname:result')
        print(f'{end-start:->13.5f} ---- {func.__name__}:{result}')
        return result
    return wrapper


# 运行该函数的结果表明
# 函数名被修改成了装饰器的子函数名wrapper
@_1_timeit
def test_1_timeit(n=3):
    for i in range(n, 0, -1):
        time.sleep(1)
        print('正在运行函数({})'.format(test_1_timeit.__name__))
    return n


# 为修正以上问题，可以在装饰器内部修改wrapper的属性__name__
# 计算函数运行时间：用于评估算法效率
# 注意：这里的函数名不符合PEP规范，仅作示例使用
def _2_timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('----- usetime ---- funcname:result')
        print(f'{end-start:->13.5f} ---- {func.__name__}:{result}')
        return result
    # 需要什么不变，就把什么添加上
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# 运行该函数的结果表明：函数名已经被修正
@_2_timeit
def test_2_timeit(n=3):
    for i in range(n, 0, -1):
        time.sleep(1)
        print('正在运行函数({})'.format(test_2_timeit.__name__))
    return n


# 为修正以上问题，也可在用装饰器functools.wraps
# 计算函数运行时间：用于评估算法效率
def _3_timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('----- usetime ---- funcname:result')
        print(f'{end-start:->13.5f} ---- {func.__name__}:{result}')
        return result
    return wrapper


# 运行该函数的结果表明：函数名已经被修正
@_3_timeit
def test_3_timeit(n=3):
    for i in range(n, 0, -1):
        time.sleep(1)
        print('正在运行函数({})'.format(test_3_timeit.__name__))
    return n


# ==========================================
# 装饰器编写的注意事项二：被装饰函数是递归函数时

# 注意：以上编写的timeit类函数并不能装饰递归函数
# 因为：被装饰函数在被装饰器装饰时被修改

# 递归形式的函数
# 运行该函数表明：函数会在递归周期内被多次装饰
@_3_timeit
def test_32_timeit(n=3, count=0):
    if count >= n:
        return n
    time.sleep(1)
    test_32_timeit(n, count=count+1)
    print('({})正在运行函数({})'.format(count, test_32_timeit.__name__))

# ---------------------------------

# 为了修正以上问题，需要给递归函数标记：增加count
# 计算函数运行时间：用于评估算法效率
# 注意：本装饰器可以装饰递归函数
def timeit(func, count=set()):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func not in count:
            count.add(func)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            #print('----- usetime ---- funcname:result')
            print(f'{end-start:->13.5f} ---- {func.__name__}:{result}')
            count.remove(func)
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper

# 递归形式的函数
# 运行该函数表明：函数不会再被多次装饰
@timeit
def test_timeit(n=3, count=0):
    if count >= n:
        return n
    time.sleep(1)
    test_timeit(n, count=count+1)
    print('({})正在运行函数({})'.format(count, test_timeit.__name__), flush=True)

# ---------------------------------
# 注意：以上递归函数不能实时打印运行结果
# 这是递归函数本身写的有问题，与装饰器无关
# 为了修正此问题，可将打印代码放在递归之前
# 例如：

# 递归形式的函数
@timeit
def test_timeit_new(n=3, count=0):
    if count >= n:
        return n
    time.sleep(1)
    print('({})正在运行函数({})'.format(count, test_timeit_new.__name__), flush=True)
    test_timeit_new(n, count=count+1)


# ==========================================
# ==========================================
# 装饰器的进阶用法四：用类编写装饰器
# 现在，回顾一下：
# 装饰器返回一个可以被调用的函数
# Python的@语法糖将………算了！我现在还不理解！！






# ==========================================
# 装饰器的进阶用法五：用装饰器装饰类
# 用类编写装饰器装饰类
# 用函数编写的装饰器装饰类

# ==========================================
# 装饰器的进阶用法六：用装饰器装饰类方法
# 用类编写装饰器装饰类方法
# 用函数编写的装饰器装饰类方法


# ==========================================
# 装饰器的进阶用法七：

# ==========================================
if __name__ == '__main__':
    # 同时给一个函数设置两个装饰器
    # returns <b><i>hello world</i></b>
    #print(hello())

    # 运行第一个被装饰器装饰的函数
    #my_first_hello()

    # 运行第二个被装饰器装饰的函数
    #my_second_hello()

    # 装饰器的高级用法一：被装饰的函数含有参数
    #my_third_hello('Jerry', 'Tom')

    # 装饰器的高级用法二：被装饰的函数参数不定数量
    #names = ['Jerry', 'Tom', 'Lucy', 'Huffy']
    #month_and_wage = {'January':5000, 'February':8000}
    #my_fourth_hello(*names, **month_and_wage)

    # 装饰器的进阶用法一：装饰装饰器的装饰器
    # 注意：由于此例是错误示范，请取消源代码的注释后再运行
    #first_advanced_hello()

    # 装饰器的进阶用法二：为装饰装饰器的装饰器传入参数
    #second_advanced_hello()

    # 装饰器编写的注意事项一：被装饰函数的函数名被改变
    #test_1_timeit(n=3)
    #print('函数名：', test_1_timeit.__name__)
    #test_2_timeit(n=3)
    #print('函数名：', test_2_timeit.__name__)
    # 用functools.wraps修正函数名
    #test_3_timeit(n=3)
    #print('函数名：', test_3_timeit.__name__)
    # 测试被装饰器装饰的递归函数
    #test_32_timeit(n=3)
    # 修正的多次调用的递归装饰器
    #test_timeit(n=3)
    # 修正运行时的打印内容
    #test_timeit_new(n=3)
    pass
