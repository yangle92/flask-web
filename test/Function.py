# def fun():
#     x = 10
#     def add():
#         nonlocal x
#         x+=1
#         print(x)
#     add()
#     return x
#
# x=fun()
# print(x)


'''
函数里面不能修改外部函数的值
    x=10
    def fun():
        x=x+1
        print(x)
global 修改全局变量
        x=10
        def fun():
            global x
            x=x+1
            print(x)
            return x
        x=fun()
        print(x)
nonlocal让嵌套函数能够修改嵌套函数之外的值
    def fun():
        x = 10
        def add():
            nonlocal x
            x+=1
            print(x)
        add()
    x=fun()
    print(x)
内置函数
all any  abs
max min sort reverse sum 
ascii
 ord 字符转换成编码
 chr 编码转换成字符
zip 拉链函数
exec 

'''

# *a,b,c=[1,2,3,4,5,6]
# print(*a)
# print(b)
# print(c)

# 匿名函数

# lambda  arg1,arg2:表达式
# 调用 lambda  arg1,arg2:表达式  （1,2）

# salaries={
#     'Tom':10000,
#     'Andy':2000,
#     'Bob':3000
# }
# print(max(salaries,key= lambda  name:salaries[name]))


#递归函数
#直接调用
# def foo():
#     print('test')
#     foo()
# foo()

#间接调用
# def foo():
#     print('test')
#     bar()
# def bar():
#     print('tset')
#     foo()
# foo()


#闭包函数
#闭：该函数的一个内部函数
#包：内部函数的函数名在外部被引用
# def outer(x,y):
#     def inner():
#         print(x+y)
#     return inner
# inner=outer(1,2)
# inner()

#装饰器就是一个特殊的闭包函数
#不改源代码，不改对象的调用方式
name='David'

def run(name):
    print('%s is running......'% name)

def declator(run):
    def new_fun(name):
        print('Before')
        run(name)
        print('Later')
    return new_fun

run=declator(run)
run(name)



@declator
def dance(name):
    print('%s is danceing' % name)


dance(name)