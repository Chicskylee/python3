#coding=utf-8
# 字符串是不可更改的(immutable)对象

str1_En = "this is a strings using test."
str2_En = "The TEST using of English."
str1_Ch = "这是一个字符串，用于测试。"
str2_Ch = "这是另一个字符串，用于测试中文。"

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# | 0 | 1 | 2 | 3 | 4 | 5 | 6
# |-6 |-5 |-4 |-3 |-2 |-1 |
#===================================================
print( "\n\n" + "="*50 )
#字符串打印。
print( "字符串打印：" )
print( str1_En )
print( str2_En )
print( str1_Ch )
print( str2_Ch )
print( "repr(1/3)：" + repr(1/3) )
print( "str(1/3)：" + str(1/3) )

# ----------------------------------------
# 对于相邻字符串解释器会自动连接，而且在加圆括号后会忽略相邻字符串之间的换行：
a = 'abc' 'defg'
print(a)

b = ('abc'
'defg')
print(b)

# 利用这个特性可以用于连接长字符串：
long_text = ('Put several strings within parentheses '
	            'to have them joined together.')
print(long_text)

# ----------------------------------------

#打印：欢迎alpha,beta,gamma。
print("\u6B22\u8FCE \u03b10 \u03b2 \u03b3")

#依次打印每个字。
for i in '北京上海广州':
  print(str(i))



#===================================================
print( "\n\n" + "="*50 )
print( "字符串生成：" )
#字符串生成。
f = lambda i:chr(i)
number_tuple = [ str(i) for i in range(0,10) ]
lower_tuple = [f(i) for i in range(97,123)]
capital_tuple = [f(i) for i in range(65,91)]
str_tuple = number_tuple + lower_tuple + capital_tuple

print( str_tuple )
str_tuple = "".join( str_tuple )
print( str_tuple )


#===================================================
print( "\n\n" + "="*50 )
print( "返回ASCII码值：" )
#返回ASCII码值。
ch="a"
print( "返回ord('a')：" + str(ord(ch)) )#ASCII码值。
print( "返回chr(98)：" + str(chr(98)) )#ASCII码值对应的字符。
print(ord("A"))

print("\n这是ASCII码对照表：")
table=""
for i in range(33,128):
    if i<100:k=str(" ")+str(i)
    else:k=str(i)
    this=chr(i)+":"+k
    table=table+"  "+this
print(table)

#===================================================
print( "\n\n" + "="*50 )
#字符串类型。
print( "字符串类型：" )
print( type( str1_En ) )
print( type( str2_En ) )
print( type( str1_Ch ) )
print( type( str2_Ch ) )

#===================================================
print( "\n\n" + "="*50 )
#字符串类型。
print( "字符串类型实例测试：" )
print( isinstance(str1_En, str) )

#===================================================
print( "\n\n" + "="*50 )
#字符串长度。
print("字符串长度：")
print( len( str1_En ))
print( len( str2_En ) )
print( len( str1_Ch ) )
print( len( str2_Ch ) )

#===================================================
print( "\n\n" + "="*50 )
#字符串提取。
print("字符串提取：")
#索引。
# 注重：解释器对于不存在的索引操作引发IndexError，但对于不存在的切片则可以正确处理
print( "索引：" )
print( str1_En[5] )#单个。
print( str1_En[-5] )#单个。
print( str1_En[ len(str1_En)-5 ] )
#切片。
str3_En = "This good."
print( "切片：" )
print( "用于对照的序号：" + "0123456789")
print( "str1_En[::]:\t" + str3_En[::] )#全部。
print( "str1_En[:]:\t" + str3_En[:] )#全部。
print( "str1_En[0:3]:\t" + str3_En[0:3] )#0-3个字符。共3个字符，不包括第3个字符。
print( "str1_En[0:-3]:\t" + str3_En[0:-3] )#0-负3个字符。
print( "str1_En[:-3]:\t" + str3_En[:-3] )#与[0:-3]等价。
print( "str1_En[3:]:\t" + str3_En[3:] )#3至结尾的字符。
print( "str1_En[:3]:\t" + str3_En[:3] )#头至3的字符串。共3个字符，不包括第3个字符。。
print( "str1_En[-3:]:\t" + str3_En[-3:] )#负3至结尾的字符。共3个字符。
#带步长的切片。
print( "带步长的切片：" )
print( "str1_En[::2]:\t" + str3_En[::2] )#步长为2，常规全切片。
print( "str1_En[::-1]:\t" + str3_En[::-1] )#逆序切片：字符串反转。
print( "str1_En[:-4:-1]:" + str3_En[:-4:-1] )#逆序截取。

#===================================================
print( "\n\n" + "="*50 )
print( "字符串测试：" )
#字符串测试。

#成员测试。
print( "成员测试：" )
print( "s" in str1_En )
print( "k" in str1_En )

print( "字符串开头字符测试：" )
#字符串开头字符测试。
#是否以prefix开头：S.startswith(prefix[,start[,end]])
print( str1_En.startswith("this") )
print( str1_En.startswith("is",2) )
print( str1_En.startswith("tring",11,16) )

print( "\n\n" + "-"*30 )
print( "字符串结尾字符测试：" )
#字符串结尾字符测试。
#以suffix结尾：S.endswith(suffix[,start[,end]])
print( str1_En.endswith("est.") )
print( str1_En.endswith("t.",-2) )
print( str1_En.endswith("es",-10,-2) )


print( "\n\n" + "-"*30 )
print( "大小写和标题形式测试：" )
#字符串大小写和标题形式测试："
#字母是否全是小写。
print( "llsyenlargemum".islower() )
#字母是否全是大写。
print( "ATMLOTKILLGOTTA".isupper() )
#是否是首字母大写的。
print( "This Is A Test".istitle() )

print( "\n\n" + "-"*30 )
print( "字符串包含类型测试：" )
#字符串包含类型测试。
#是否为Python标识符。
#print( "False".isidentifier() )#仅python3有效。
#是否全是字母和数字，并至少有一个字符。
print( "strings123".isalnum() )
#是否全是字母，并至少有一个字符。
print( "bullockslotsjoke".isalpha() )
#是否全是数字，并至少有一个字符。
print( "12355586".isdigit() )
#是否只包含空白字符，并至少有一个字符。
print( "    ".isspace() )
#是否以纯十进制数字组成。
#print( "12354680".isdecimal() )  # 仅Python3
#是否只包含数字字符。
#print( "5868".isnumeric() )  # 仅Python3
# 注意：负数不是isnumeric的
#print('-258'.isnumeric())
#是否只包含可打印字符。
#print("abc".isprintable())  # 仅Python3

#===================================================
print( "\n\n" + "="*50 )
print( "字符串查找：" )
#字符串查找。
#S.find(substr, [start, [end]])
#返回最先出现的substr的首字母标号。
#注意：若不存在substr则返回-1。
print( str1_En.find("st") )
print( str1_En.find("k") )

#S.rfind(substr, [start, [end]])
#返回最后出现的substr的首字母标号。若不存在substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号。

#从查找到的某个字符串提取。
print( str1_En[str1_En.find(" ") + 1:] )

print( "\n\n" + "="*50 )
#返回字符串的第一索引值。
#S.index(substr, [start, [end]])
#与find()相同，只是在S中没有substr时，会返回一个运行时错误
#注意：当索引不存在时，抛出ValueError。
print( "字符串的第一索引值：" )
print( str1_En.index( "s" ) )
print( str1_En.index( "in" ) )
print( str1_Ch.index( "个" ) )
print( str1_Ch.index( "用于" ) )
#类似index，只是从右侧开始查找。
#S.rindex(substr, [start, [end]])

#===================================================
print( "\n\n" + "="*50 )
#字符串统计。
print( "字符串统计：" )
#S.count(substr, [start, [end]]) #计算substr在S中出现的次数
print( str1_En.count("s") )

#===================================================
print( "\n\n" + "="*50 )
#字符串替换。
#S.replace(oldstr, newstr, [count])：把S中的oldstar替换为newstr，count为替换次数。
#注意：不标明次数的replace方法将多次替换！
print( "字符串替换：" )
print( str1_En.replace("i","!") )
# S.expandtabs(n)：将每个制表符替换为n个空格，默认为8个空格。
print("字符串中制表符的替换：")
print("a\tb\tc".expandtabs(5))

#===================================================
print( "\n\n" + "="*50 )
print( "英文字符串的大小写转换：" )
#英文字符串的大小写转换。
#所有英文字符变成小写。
print( str2_En.lower() )
#所有英文字符变成大写。
print( str1_En.upper() )
#将所有英文字符的大小写反转。
print( str2_En.swapcase() )
#将字符串的首字母设置为大写。
print( str1_En.capitalize() )
#返回标题化的字符串（所有单词首字母大写，其余小写）
print("This Is A Test".title() )
#将字符串的每个单词的首字母大写：string.capwords(S)。
#等价于：把S用split()函数分开，然后用capitalize()把首字母变成大写，最后用join()合并到一起。
import string
print( string.capwords(str1_En) )#这是模块中的方法。

#===================================================
print( "\n\n" + "="*50 )
#将字符串用指定字符(字符串)分割成列表。
#S.split([sep, [maxsplit]])：以sep为分隔符，把S分成一个list。maxsplit表示分割的次数。默认的分割符为空白字符。
#注意：必须传入分割符sep，且分隔符不能是''，即空白字符。
print( "将字符串用指定字符(字符串)分割成列表：" )
print( str1_En.split(" ") )
#将字符串分割。
#S.rsplit([sep, [maxsplit]])
print( str1_En.rsplit("s"))
#S.splitlines([keepends])：把S按照行分割符分为一个list，keepends是一个bool值，如果为真，每行后而会保留行分割符。
print( str1_En.splitlines() )
#S.partition(substr)
#从substr出现的第一个位置起，将str分割成一个3元组。
print( str1_En.partition(" ") )
#类似partition函数，不过从右边开始查找。
print( str1_En.rpartition(" ") )


#===================================================
print( "\n\n" + "="*50 )
#将列表元素用指定字符串连接。
#注意：如果将字符串增加以后返回同一个变量名，可用a += a
print( "将列表元素用指定字符串连接：" )
a = str1_En.split(" ")
print( "**".join(a) )

def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print( s )
print( addslashes(s) )



#===================================================
print( "\n\n" + "="*50 )
print( "字符串输出格式化：" )
#字符串输出格式化(对齐)。
print( "\n\n" + "-"*30 )
print( "字符串输出对齐：" )
#字符串输出对齐。
#左对齐：S.ljust(width,[fillchar])。
#输出字符宽度width，不足部分在右侧用fillchar填充，默认用空格。
print( str1_En.ljust(40,"*") )
#右对齐：S.rjust(width,[fillchar])。
#输出字符宽度width，不足部分在左侧用fillchar填充，默认用空格。
print( str1_En.rjust(40,"*") )
#中间对齐：S.center(width, [fillchar])。
#输出字符宽度width，不足部分在两侧用fillchar填充，默认用空格。
print( str1_En.center(40,"*") )
#加长字符串：S.zfill(width)，不足部分用0补全。
#注意：这种方法类似于ljust()。
print( str1_En.zfill(40) )
print( "\n\n" + "-"*30 )

#把字符串的tab转为空格，默认为8个
print( "abc\tdef".expandtabs() )


#S.strip(strings)
#删除S字符串开头、结尾处的字符strings，默认删除空白符。
#注意：空白符指空格，换行符，制表符等。
print("去掉字符两边的空格和换行符：")
print( repr("\n\n abc  \n \n".strip()) )
#删除路径左右两边的路径分隔符。
print("去除路径左右两边的路径分隔符(/)：")
print("/myfile/myfile2/myfile3/".strip("/"))
#删除字符串两端的指定字符。
print("删除字符串两端的指定字符(xy)：")
print("xxyxyyPythonxxyyyxxy".strip("xy"))
#警告：小心使用该方法！！请仔细看下面的例子！！！！
# 将删除左右两端的'.'、'm'、'p'、'3'，
#但是实际上想要返回'3_1'，却返回了'_1'
print(repr('3_1.mp3'.rstrip('.mp3')))
# 这个例子将删除左右两端的'.'、'w'、'a'，
#但是实际上想要返回'a'，却返回了空字符串''
print(repr('a.wa'.strip('.wa')))

#S.lstrip(strings)
#删除S字符串开头处的字符strings，默认删除空白符。
print("去掉字符左边的空格和换行符：")
print( repr("\n   abc\n".lstrip()) )

#S.rstrip(strings)
#删除S字符串结尾处的字符strings，默认删除空格和换行符。
print("去掉字符右边的空格和换行符：")
print( repr("\n\n abc  \n \n".rstrip()) )


#===================================================
print( "\n\n" + "="*50 )
print( "各种转义符：" )
#各种转义符：
#注意：当Python无法识别反斜杠后面是什么转义符时，将原样输出。
print(r"00.这个字符串原先是这样的:"+"\nThis is a test.")
print(r"01.\t水平制表符(空6个英文空格):"+"\nTh\tis is a test.")
print(r"02.\f换页:"+"\nTh\fis is a test.")#换页。
print(r"03.\v垂直制表符:"+"\nTh\vis is a test.")
print(r"04.\n换行:"+"\nTh\nis is a test.")#换行。
print(r"05.\b回退:"+"\nTh\bis is a test.")#回退。
print(r"06.\r返回:"+"\nTh\ris is a test.")

#===================================================
print( "\n\n" + "="*50 )
print( "字符串拼接：" )
#字符串拼接。
pieces = ["the", " ", "test"]
#法一：超级低效的方法。
larger_strings = ""
for i in pieces:
    larger_strings += i
print(larger_strings)

#法二：高效的方法：推荐使用。
larger_strings = "".join(pieces)

#法三：
#注意：reduce在python2中是自带的。
import operator
import functools
larger_strings = functools.reduce(operator.add, pieces, '')
print(larger_strings)

#===================================================
#===================================================
print( "\n\n" + "="*50 )
print( "\n\n" + "="*50 )
print("字符串的格式化：")
# 字符串格式化。
#1.语法格式:%[(name)][flags][width][.precision]typecode
#2.操作：
#(1)标志位:左对齐-，正负号，补零。
#(2)给出数字的整体长度和小数点后的位数。
#(3)其中width和precision都可以编码为*，来指定从输入值中取得。
#3.字符串格式化代码：
#s:字符串(或任何对象)。
#r:类似s，到使用repr，而不是str。
#c:字符。
#d:十进制整数。
#i:整数。
#u:无号整数。
#o:八进制整数。
#x:十二进制整数。
#X:同x，但打印大写。
#e:浮点指数。
#E:同e，但打印大写。
#f:十进制浮点数。
#F:十进制浮点数。
#g:浮点数e或f。
#G:浮点数E或F。
#%:常量%。


print( "用%对字符串输出格式化：" )
# 左对齐。
print( "integer:%-6d" % 1234)
# 右对齐。
print( "integer:%6d" % 1234)
# 补零。
print( "integer:%06d" % 3.141592653579793)
print( "strings:%10s" % "abcdef")
#用format对字符串的输出进行格式化。
Strings10 = '%s, eggs, and %s' % ('spam', 'SPAM!')
print( Strings10 )
# 基于字典的格式化方法
Strings11 = '%(a)s, eggs, and %(b)s' % {'a':'spam', 'b':'SPAM!'}
print( Strings11 )

#===================================================
print( "\n\n" + "="*50 )
print( "用format对字符串输出格式化：" )
# 形式如下：
# '{fieldname!conversionflag:formatspec}'.format(*arg)
# 其中formatspec的形式如下：
# [[fill]align][sign][#][0][width][.precision][typecode]
# 其中align可以是<、>、=或^，分别表示左对齐，右对齐，
Strings20 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
print( Strings20 )
Strings21 = '{}, eggs, and {}'.format('spam', 'SPAM!')
print( Strings21 )
# 设置分隔符为中文名分隔符·，设置字符左对齐， 设置总字符宽度为10， 打印内容为hello
print('{:·<{:d}s}'.format('hello', 10),)

# 设置宽度
print('+'*50)
print('你好：{x:10}'.format(x='hello'))  # 宽度为10
# 设置对齐方式
print('你好：{x:>10}'.format(x='hello'))  # 右对齐，宽度为10
print('你好：{x:<10}'.format(x='hello'))  # 左对齐，宽度为10
# 设置精度。
print("3.1415={x:f}".format(x=3.1415))
print("3.1415={x:.5f}".format(x=3.1415))
print("3.1415={x:.{d}f}".format(x=3.1415,d=10))
# 传入字典。
print("My {pet} has {p}".format(pet="dog",p="fleas"))
# 设置为百分比
print("{:.2%}".format(0.0072345))
#===================================================
print( "\n\n" + "="*50 )
print( "翻译表：" )
#翻译表：String.maketrans(old, new)
#返回一个256个字符组成的翻译表，其中old中的字符被一一对应地转换成new。
# 注意：old和new必须等长度。
#print("a".maketrans("abcdefg","1234567"))  # 仅Python3
#S.translate(table)
#使用上面的函数产后的翻译表，把S进行翻译。
#此外还可以使用codecs模块的功能来创建更加功能强大的翻译表。
#print( "aacceejjff".translate( "a".maketrans("abcdefg","1234567")) )
def my_replace():
    # 字符串替换
    # 设置替换规则(None代表删除)
    table = str().maketrans({'&':None, '$':None})
    # 完成替换
    print('hel&lo wor$ld'.translate(table))
    # 你也可以自己构建映射表，而不用maketrans：
    table = {ord('&'):None,
             ord('$'):None}
    print('hel&lo wor$ld'.translate(table))

# ---------------------------------------------
print("去除字符串中不必要的成份：")
#方法一：注意：仅Python3
#delete_str = "-:= "  # 删除英文横杠，冒号，等于号和空格。
#创建一个翻译表，前两个参数未指定任何内容，即不进行任何改动。第三个参数指将要删除的内容。
#StrTable = "".maketrans( "" , "" , delete_str)
#将字符串用翻译表翻译。
#strTime = "2017-02-21 14:03:22".translate( StrTable )
#print(strTime)

#方法二：注意：仅在Python2
# 注意：Python3的string模块删除了maketrans()函数。
import string
#a_str = string.maketrans("abc","123")  # 生成翻译表。
#print(a_str)
#注意：第二个参数指要删除的内容，它是一个字符串。。
#new_str = "abkn3ucll".translate(a_str,"kn")  # 翻译字符串。
#print(new_str)


# ==================================================
print( "\n\n" + "="*50 )
# 字符串的编码与解码。
# 字符串编码：S.encode([encoding,[errors]])
#其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。
#errors默认值为"strict"，意思是UnicodeError。

#字符串解码：S.decode([encoding,[errors]])









