#定义函数
# def move():
#     print('moving...')
# move()
'''
list = [0,1,2,3,4,5,6,6,7]
def add(L):
    sum = 0
    for index in list:
        sum  = sum + index
    print(sum)
    return sum

add(list)
add2 = add(list)
print(add2)
'''
'''
a = 1 
def turn():
    global a  #只有这样才知道a是个全局变量
    a = 5
    #return a
turn()
print(a)
'''
def add(a,b=5):
    return a+b

#print(add(b=2,a=8))
#偏函数
'''
import functools
add_ = functools.partial(add,b=10)
print(add_(a=10))
add_ = functools.partial(add,b=20)
print(add_(a=10))
'''
#高阶函数
'''
def jian(a,b):
    return a-b
def oper(a,b,fun):
    return fun(a,b)
print(oper(2,3,jian))
'''

#返回函数  闭包（1、嵌入函数  2、子函数调用父函数的变量  3、父函数返回子函数）
'''
def sum(a,b):
    def oper():
        print(a+b)
    return oper
sum(2,3)()
'''

#装饰器
'''
def valid(fun):
    #def inner(a,b):
    def inner (*args):   #装包
        print("是否登录？")
        #print(args)      #解包
        fun(args[0],args[1])
        print("录入日志...")
    return inner
@valid
def apply(a,b):
    #print("是否登录？")
    c = a + b
    print("执行业务逻辑")
    #print("录入日志...")
    return c
@valid
def apply2(a,b):
    print("apply2...")
#valid(apply)(4,5)
apply(2,3)
#apply2(2,3)
'''

def valid(fun):
    def inner (*args):   #装包
        print("是否登录？")
        #print(args)      #解包
        fun(*args)
        print("录入日志...")
    return inner
@valid
def apply(*args):
    #print("是否登录？")
    c = 0
    for i in args:
        c = c + i
    print("执行业务逻辑")
    #print("录入日志...")
    return c
@valid
def apply2(a,b):
    print("apply2...")
#valid(apply)(4,5)
apply(2,3)