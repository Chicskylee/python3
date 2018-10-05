#coding=utf-8
# ========================================
# 注意0：列表、字符串和元组都属于序列，但仅列表是可变对象
# 注意1：列表是一种可变(mutable)对象
# 注意2：列表方法，将直接改变列表结构
# 注意3：对列表的引用被修改，将直接改变原列表
# 注意4：在函数中引用列表，也将改变原列表
# 注意5：如果要禁止修改原列表，可在函数中生成对列表的完全拷贝
# 注意6：列表的插入和删除除非尾部元素时会涉及列表中大量元素的移动，效率较低
# 警告0：列表的可变性可能造成意想不到的bug！
# ========================================
# 注意：列表的元素可以是包含列表在内的任何类型数据
# 举例：
# [1, 2, 3, 4, 5]
# ['Tom', 'Joy', 'Lily', 'Harry']
# [5, 3.2, 'hello', ('a', 2, 3), [5, 6.2, 'world']]
# ["a", 3, "c", 1, "b", 2, "d", 4, "e"]
# ========================================
# 列表的索引和切片操作
# 注意：索引操作返回非独立于列表的元素
# 注意：切片操作返回独立于列表的元素拷贝列表

# 列表的索引
def list_index():
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # 列表的每个元素都有一个序号，叫索引值，它标志元素的位置
    # 列表有两套标记索引值的方法，一套正着数，一套倒着数
    # 元素的索引值正着数(从左到右)依次为0, 1, 2, 3,...
    # 元素的索引值倒着数(从右到左)依次为-1, -2, -3,...
    # 获取列表的元素，要用索引操作
    # 例如，要获取元素的第一个值，可以用正索引值：
    print(L[0])
    # 也可以用倒索引值：
    print(L[-5])
    # 而要获取元素的最后一个值，可以用正索引值：
    print(L[4])
    # 也可以用倒索引值：
    print(L[-1])
    # 注意：用不存在的索引值进行索引操作将引发异常IndexError
    # print(L[7])
    # 注意：索引操作，返回列表元素的非独立拷贝！与切片不同！
    # 例如，以下结果返回True：
    print(L[-1] is L[-1])
    print(id(L[-1]) == id(L[-1]))

# 列表的切片
def list_slice():
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # 获取列表的多个元素，可以使用列表的切片操作
    # 切片操作有多种形式，如：
    # 获取索引值在0~4(不含)区间的元素
    print(L[0:4])
    # 当起止切片的索引值在开头或结尾时，也可省略起止索引值
    print(L[:4])
    # 或者，用倒索引值也可以
    print(L[-7:-3])
    # 同样，使用倒索引也可以省略起止索引值
    print(L[:-3])
    # 甚至，还可以混合使用正索引值和倒索引值
    print(L[0:-3])
    # 或
    print(L[-7:4])
    # 注意：与索引操作不同，切片操作对不存在的索引值比较宽容
    # 例如，获取索引值在0~4(不含)区间的元素，还可以用
    print(L[-100:4])
    # 因为会使写代码意图不明确，因此并不推荐如上用法
    # --------------------
    # 获取列表的完全拷贝，可以用
    print(L[0:])
    # 也可以利用切片操作对不存在的索引值宽容的特性写成
    print(L[0:7])
    # 或者，直接用省略起止索引值的办法(推荐)进行操作
    print(L[:])
    # --------------------
    # 若需要获取列表中具有固定间隔的元素时，可以增加第三个数字
    # 这种切片操作叫“步进式切片操作”
    # 例如，每两个元素获取一个元素
    print(L[0:7:2])
    # 也可以用省略起止索引值的办法(推荐)进行操作
    print(L[::2])
    # --------------------
    # 当第三个参数为负数时，将会进行逆序切片操作
    # 例如，获取原列表的完整逆序拷贝
    print(L[::-1])
    # --------------------
    # 这样，获取原列表的方法其实还有不传入第三个参数的办法
    print(L[::])
    # --------------------
    # 注意：与索引操作不同，所有切片操作获得列表元素的浅拷贝
    # 例如，以下结果返回False
    print(L[0:1] is L[0:1])
    print(id(L[0:1]) == id(L[0:1]))


if __name__ == '__main__':
    list_index()
    list_slice()
    pass

#__import__("sys").exit()
# ========================================
# 列表方法
def list_method():
    # 列表的方法，用于实现对列表元素的排序，以及增、删、改、查
    # 列表的排序方法：sort(对混合列表无效)
    # 注意：sort方法在原内存地址修改列表
    # 注意：sort不能对['b', 1, 'a', 2]这样的混合列表排序
    L1 = [1,3,2]
    # 注意：修改操作在原内存地址进行，返回值为None
    L1.sort()
    print(L1)
    L2 = ['c', 'a', 'b']
    L2.sort()
    print(L2)
    # --------------------
    # 列表的反转：reverse
# 注意：效果与切片操作list[::-1]相同，但是切片生成一个拷贝。
L = [1,3,2]
L.reverse()
print(L)
mixed_L = ["a", 3, "c", 1, "b", 2]
mixed_L.reverse()
#__import__("sys").exit()
# 插入list.insert()：指定索引之前插入元素，其它元素后移。
# 注意：list[n] = "something"替换索引元素。
L = ["c","a","b"]
L.insert(2,"k")
print(L)


# 扩展list1.extend(list2)。改变原列表。
# 注意：合并操作list1 + list2生成一个拷贝。
L = [1,2]
L.extend(["a", "b"])
print(L)

# 追加list.append(item)：在列表末尾增加元素。改变原列表。
L = [1,2]
L.append("abc")
print(L)

# 统计list.count(item)：返回某个元素在列表中出现的频率。
# 注意：想一次统计多个元素，可参考模块collections。
L = ["a","b","c","c","d","c"]
print(L.count("c"))

# 索引list.index(item)：返回列表中首次出现的索引。
#注意：对不存在的元素索引将引发ValueError。
L = ["a","b","c","c","d","c"]
print(L.index("c"))

# 列表值弹出list.pop(index)：弹出指定索引元素并返回弹出元素。
# 注意：默认弹出最后一个元素。可用pop(3)弹出索引为3的元素。
# 注意：对于字典，pop(key)指弹出指定的键所对应的值。
L = ["a","b","d","c"]
print(L.pop(2))
print(L)

# 元素删除list.remove(item)：移除某个值的首个匹配项。
L = ["a","b","c"]
L.remove("c")
print(L)

#同时遍历列表的索引和值：enumerate(list)
print(["%s:%s"%(index,item) for index,item in enumerate(["c", 'a', 'b'])])

# ========================================
print("\n\n"+"="*50)
print("列表解析：")
#列表解析：在Python2中返回列表，在Python3中返回生成器。
# 注意：在Python3中，可用list()收集元素到列表中。
#结构：
"""
[expression for target1 [if condition1]
            for target2 [if condition2]
            for target3 [if condition3]
            ...
            for targetN [if conditionN]]
"""
# 注意：一个for语句后仅可使用一个if测试。
# ========================================
# 嵌套列表解析：
print([p+q for p in "defg" for q in "abc"])
# 生成具有某种特征的列表。
print([x % 2 == 0 for x in range(1, 11)])
# 使用None生成列表。
print([None]*10)
# 带有条件表达式的列表解析。
print([x for x in range(10) if x % 2 == 0])
# 获取指定值。
L = [("bob",35,"mgr"),("mel",40,"dev")]
print([name for (name,age,job) in L])  # 取出姓名。

# ----------------------------------------
# 用列表解析获取嵌套列表的值。
L = [ [1,3,5,7], [2,4,6,3], [3,1,2,8], [6,4,0,7] ]
print([row[2] for row in L])  # 获取第三列。
print([L[row][2] for row in [0,1,2,3]])  # 获取第三列。
print([row[2] for row in L if row[2]%2 == 0]) #第三列的偶数。
print([L[i][i] for i in [0,1,2,3]])# 获取对角元素值。
print([sum(row) for row in L])  # 求每行元素的和。

M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[2,2,2],[3,3,3],[4,4,4]]
print([M[row][i]*N[row][i] for row in range(3) for i in range(3)])
print("M与N对应元素乘积：%s" % [[M[row][i]*N[row][i] for row in range(3)] for i in range(3)])

# ----------------------------------------
print( "\n\n" + "-"*40 )
print( "用列表解析除去文件中每行末尾的换行符：" )
#[line.rstrip() for line in open(filename).readlines()]
#[line.rstrip() for line in open(filename)]
#注意：后一种方法使用了文件迭代器。《Python学习手册4》
# ========================================
# ----------------------------------------
# 集合解析：{f(x) for x in S if P(x)}  # 仅Python3可用。
# 类似生成器表达式set(f(x)for x in S if P(x))
print({row[0] for row in L})  # 集合解析。

# 字典解析：{key:val for (key,val) in zip(keys_list,vals_list)}  # 仅Python3可用。
# 类似dict(zip(keys,vals))。
# 类似生成器表达式dict((x,f(x))for x in items)
print({i:ord(i) for i in "abcdef"})  # 字典解析。

# ========================================
print("\n\n"+"="*50)
print("列表的多重嵌套：" )
# 列表的多重嵌套。
print("展平(展开、合并)二重列表：")
# 展平(展开、合并)二重列表
# 仅含数字的列表
# 注意：这样的不行：[[1,2], [3], [4,5,6], [7,8,9,0], 11]
L = [[1,2], [3], [4,5,6], [7,8,9,0]]
print(sum(L, []))
import itertools  # 用来展开一般嵌套列表
# 利用itertools库展平嵌套列表
print(list(itertools.chain(*L)))
print(list(itertools.chain.from_iterable(L)))
import itertools
data = [[1, 2, 'b'], ['a', 5, 6]]
print(list(itertools.chain.from_iterable(data)))
# 再或者

from functools import reduce
from operator import add
data = [[1, 2, 'b'], ['a', 5, 6]]
print(reduce(add, data))
# 仅含字符串的列表
# 注意：这样的不行：[["a","b","c"],["d","e"],["f"],"g"]
L = [["a","b","c"], ["d","e"], ["f"]]
print(sum(L, []))

# 利用itertools
print(list(itertools.chain(*L)))
print(list(itertools.chain.from_iterable(L)))

# 混合列表
L = [["a","b","c"], [1,2,"d","e"], [3,4]]
print(sum(L, []))

# 利用itertools
# 注意：itertools.chain()对下面的多重嵌套列表无效
print(list(itertools.chain(*L)))
print(list(itertools.chain.from_iterable(L)))
#----------------------------------------------
print("\n\n"+"-"*50)
print("展开多重嵌套列表：")
# 展开多重列表
L = [["a","b",["c",[1,[2],"d"],"e"]],[3,'f'],4,"g",5]
# 递归遍历。
def flattenList(L,new_list=[]):
    # 展平多重列表
    for i in L:
        if not isinstance(i,list):
            new_list.append(i)
        else:
            flattenList(i,new_list)
    return new_list
print(flattenList(L))

# 方法三：用递归中的奇技淫巧。
func = lambda L: sum(map(func,L),[]) if isinstance(L,list) else [L]
new_str = func(L)
print(new_str)

s = [["a","b",["c",[1,[2],"d"],"e"]],[3,'f'],4,"g",5]
flat=lambda L: sum(map(flat,L),[]) if isinstance(L,list) else [L]
print(flat(s))
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
print(flatten(s))

LIST = [1, "a", ["b", 2, [3, "c", 4], "d", 5], 6, "e", [7, "f", 8], 9, "g", 0]
print(flatten(LIST))
# 将以下递归函数写到一个类中：
def printList(L, newList=list()):
    # 展平多元列表
    for x in L:
        if isinstance(x, list):
            printList(x,newList)
        else:
            newList.append((x))
    return newList

print(printList(LIST))

# 写到类中：
class PrintList(object):
    def printList(self, L, newList=list()):
        self.L = L
        for x in L:
            if isinstance(x, list):
                self.printList(x,newList)
            else:
                newList.append((x))
        return newList

a = PrintList()
print(a.printList(LIST))
#----------------------------------------------
# 类似列表解析的例子：
# 例子：
S = set()
for i in [1,2,3,4]:
    S.add(i)
print(S)

# 相当于：
S = {i for i in [1,2,3,4]}
print(S)

# ======================
# 例子：
D = dict()
for key, value in [('a',1), ('b',2)]:
    D[key] = value
print(D)

# 相当于：
D = {key:value for key,value in [('a',1), ('b',2)]}
print(D)

#==============================================
print("\n\n"+"="*50)
print("使用map函数：")
#map(func,iterable1,iterable2,...)函数的使用。
#传入单参数函数：map(lambda x: x+1, num_list)
#传入多参数函数：map(lambda x,y: x+y, numlist1, numlist2)
# 注意：map()函数的第一个参数是函数
# 对应元素想加：
print(list(map(lambda x,y: x+y, [1,2,3], [4,5,6])))
#print(list(map(sum, list_in_list)))
print(list(map(abs,[-1,3,-5,4,2])))
#----------------------------------------------
print("\n\n"+"-"*50)
print("使用reduce函数：")
# reduce(func,sequence)   # 仅Python2,Python3移在functools模块
#reduce(functhon,sequence[,initializer])函数的使用。
#注意：在Python3中，该函数被移至functools。
#用reduce计算出所有数字的和：
import functools
print(functools.reduce(lambda x,y:x+y, [1,2,3]))
#----------------------------------------------
print("\n\n"+"-"*50)
print("使用filter函数：")
# filter(func, iterable)  # 过滤器。返回iterable中所有使func的返回值为真的元素。注意：若func是None，则返回值等价于True的元素。
#filter(func,sequence)过滤器函数。
# 返回iterable中所有使function返回值为真的元素组成的列表。
seasons = ["Spring||","|","Summer||","|","Fall||","Winter||"]
print(list(filter(lambda x:x!="|",seasons)))
#----------------------------------------------
print("\n\n"+"-"*50)
print("使用zip函数：")
#zip()函数的使用。
#zip(list1,list2)
#用zip将先压缩，再还原。
L_zip = [(2,11),(4,13),(6,15),(8,17)]
print(list(zip(*L_zip)))
L_zip2 = [(2, 4, 6, 8), (11, 13, 15, 17)]
print(list(zip(*L_zip2)))
#将字典的键和值颠倒：一旦值有重复，将丢弃多余的。
D = {1:"a",2:"c",3:"c"}
print(dict(zip(D.values(),D.keys())))

#==============================================
print("\n\n"+"="*50)

# 这里两个结果并不一样，具体原因我暂时也不知道
def list_feature01():
    def func1():
        a = ['a', 'b', 'c']
        m = a[1:2]
        n = a[1:2]
        print(m is n)
        print(id(m) == id(n))
    def func2():
        a = ['a', 'b', 'c']
        print(a[1:2] is a[1:2])
        print(id(a[1:2]) == id(a[1:2]))
    func1()
    func2()





