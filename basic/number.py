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


# 其它相关内容：
# 注意：这些内容将留待模块部分介绍
# 模块：math、decimal、fractions、statistics、random、difflib
# 注意：这些内容将留待异常捕获部分介绍
# 异常类型：ArithmeticError(及其子类FloatingPointError、OverflowError、ZeroDivisionError)



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


if __name__ == '__main__':
    print('数字的基本操作：')
    show_operators_for_number()
    print('不同时进制数的转换：')
    hexadecimal_conversion()
    print('按位操作：')
    show_operators_only_for_integer()



