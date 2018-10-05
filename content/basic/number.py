# coding=utf-8

# 注意：与Python2不同，在Python3中，不存在long int，
# 在Python3中只有 int 这一种整数类型。
# 长整形：long()，此类型在Python3中被弃用！！

# 数的类型
# 整数类型：int()
# 浮点数类型：float()
# 复数类型：complex()
# 布尔类型：bool()   ——特殊的整数


# 数类型的数学运算
# 四则运算：加(+)、减(-)、乘(*)、除(/)；
# 整除(//)、
# 取余(%)，不能应用于复数
# 方幂运算(**) 或 pow(integer1, integer2)
# 按位运算(仅整数)：和(&)、或(|)、异或(^)、左移(<<)、右移(>>)、取反(~)


# Python自带的函数：
# 幂运算 pow(integer1, integer2)
# 绝对值运算 abs(integer)
# 商和余数运算 divmod(integer1, integer2)
# 四舍五入 round()
# 求和运算 sum()


# 进制转换(仅整数)：
# 10转16进制 hex(integer)
# 10转8进制 oct(integer)
# 10转2进制 bin(integer)


# 浮点数转换

# Python自带的其它函数
# 格式化函数：format()


# =====================================
# 浮点数丢失精度问题：
# 0.1+0.1+0.1-0.3 = 5.5511151231257827e-17
# 1.2+2.4 = 3.5999999999999996
# 1-2.0/3 = 0.33333333333333337
# 3.1+2.3+3.4 = 8.8000000000000007

# =====================================
# 注意：
# 如果在Python2中引入了__future__模块的division
# 那么Python2中的除法，将类似于Python3中的除法，
# 请在Python2中比较：
# print(5/2)
# 和
# from __future__ import division
# print(5/2)
# =====================================
# 其它相关内容：
# 注意：这些内容将留待模块部分介绍
# 模块：math、decimal、fractions、statistics、random、difflib
# 注意：这些内容将留待异常捕获部分介绍
# 异常类型：MemoryError、ArithmeticError(及其子类FloatingPointError、OverflowError、ZeroDivisionError)



# 数的基本数学运算
def show_operators_for_number():
    print(1 + 2)      # 3
    print(5 - 9)      # -4
    print(3 * 5)      # 15
    print(9 / 3)      # 3.0
    print(9 / 5)      # 1.8
    print(9 // 3)     # 3
    print(9 // 5)     # 1
    # 注意：整除的结果不一定是整数
    print(8 // 3.5)   # 2.0
    print(16 // 7)    # 2
    print(9 % 3)      # 0
    print(9 % 5)      # 4
    print(9 % 2.5)    # 1.5
    print(9 % -2.5)   # -1.0
    print(2 ** 3)     # 8
    print(5 ** 0.5)   # 2.23606797749979
    print(5 ** (1/2)) # 2.23606797749979


# 进制转换
# 数学上的十进制转换二进制的思路是：除2取余，逆序排列
# 方法：将一个数字依次除以2，将余数写在右侧。最后从最下面依次写出即可。
# 按二进制位进行运算
def hexadecimal_conversion():
    # 10进制转16进制
    print(hex(18))  # 0x12
    # 10进制转8进制
    print(oct(9))   # 0o11
    # 10进制转2进制
    print(bin(5))   # 0b101
    # 2进制转8进制的手算方法
    # 10001011101101
    # 方法：将每三位看作一个八进制数，即
    # (010)(001)(011)(101)(101)
    #   2    1    3    5    5
    # 因此8进制为：(21355)8
    # 16进制转10进制
    print(int('0x12', base=16))  # 18
    # 8进制转10进制
    print(int('0o11', base=8))  # 9
    # 2进制转10进制
    print(int('101', base=2))  # 5
    # 据以上讨论，可将10进制作为进制转换的中间桥梁



# 按位操作
def show_operators_only_for_integer():
    # 按位和操作：相同位置处，同时满足为1，则为1
    print(5 & 23)  # 5
    # 解释：
    # 00101
    # 10111
    # 00101
    # 先将5和23换算成二进制小数，不足的用0补齐，
    # 然后按照&的定义：对齐且都为1的结果为1，否则为0。
    # 最后得出00101再换算成十进制即得。
    # 按位或操作：相同位置处，只要有一个满足为1，则为1
    print(5 | 23)  # 23
    # 00101
    # 10111
    # 10111
    # 按位异或：相同位置处，不相同，则为1
    print(5 ^ 23) # 18
    # 00101
    # 10111
    # 10010
    # 按位左移：
    print(5 << 8) # 1280，其二进制：10100000000
    # 00101
    # 10111
    # 12345678901234567890123456789--正位数标尺
    # 98765432109876543210987654321--负位数标尺
    # --------------------------
    # 00000000101----补齐11位的5的二进制形式
    # 10100000000----将每个1向左移8位，得到1280的二进制形式
    print(int('10100000000', 2)) # 1280


# =====================================
# 查看变量的id
def look_id():
    int_a = 3
    int_b = 5
    print('查看变量的id：')
    print(id(int_a))
    print(id(int_b))

# is的特性：对于-5~256之间的值用is判断不同变量值，结果为True
def is_feature00():
    for i in range(-10, 260, 1):
        print(i)
        a = i
        b = i + 1 - 1
        print('a is b:', a is b)
        print('id(a):{}, id(b):{}'.format(id(a), id(b)))





# 自带的数学函数
def int_func():
    # 次方
    print('pow(4, 3)：{}'.format(pow(4, 3)))
    print('4**3：{}'.format(4**3))
    # 绝对值
    print('abs(-2.6)：{}'.format(abs(-2.6)))
    # 圆整（向下取整，即不四舍五入，直接截断取整）
    # 注意：需要四舍五入，请用math.ceil()函数
    print('round(2.5)：{}'.format(round(2.5)))
    print('round(2.7)：{}'.format(round(2.7)))
    print('round(1.234567, 3)：{}'.format(round(1.234567, 3)))
    print('round(2.3)：{}'.format(round(2.3)))
    # 返回一个二元素元组，代表商和余数
    print('divmod(5,3)：{}'.format(divmod(5,3)))



if __name__ == '__main__':
    print('数字的基本操作：')
    show_operators_for_number()
    print('不同时进制数的转换：')
    hexadecimal_conversion()
    print('按位操作：')
    show_operators_only_for_integer()



