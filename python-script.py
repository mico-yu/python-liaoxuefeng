
import math
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''调用函数
r=input("输入半径：")
r=float(r)
pi=3.14
mianji = pi*r*r
print(mianji)
'''
'''定义函数'''


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -1*x
# print(my_abs('a'))


def mov(x, y, step, angle=0):
        for m in (x, y, step, angle):
                if not isinstance(m, (int, float)):
                        raise TypeError('bad operand type')
        nx = x + step * math.cos(angle)
        ny = y + step * math.sin(angle)
        return nx, ny
# r = mov(1,1,2)
# print(r)


def quadratic(a, b, c):
        for m in (a, b, c):
                if not isinstance(m, (int, float)):
                        raise TypeError("bad operand type")
        if a == 0 and b == 0 and c == 0:
                print("任意解")
                return
        if a == 0 and b == 0:
                print("参数错误")
                return
        if a == 0:
                return 1.0*c/b
        dd = b * b - 4 * a * c
        d = float(dd)
        
        if d >= 0:
                d = math.sqrt(d)
                return (-1*b+d)/(2*a), (-1*b-d)/(2*a)
        else:
                print("无解")

# r=quadratic(1, 3, -4)
# print(r)


def my_power(x, n=2):
        for m in (x, n):
                if not isinstance(m, (int, float)):
                        raise TypeError('bad operand type')
        if n == 0:
                return 1
        sign = 0
        if n < 0:
                sign = 1
                n = -1 * n
        res = 1
        while n >= 1:
                res = res * x
                n = n - 1
        if sign == 0:
                return res
        else:
                return 1/res


# r = my_power(0,0)
# print(r)

def add_end(lo=None):
        if lo == None:
                lo = []
        lo.append("end")
        return lo


'''
L = add_end()
print(L)
L= add_end()
print(L)
'''


# 可变参数允许你输入N个参数，这些参数在函数调用时自动组装成一个tuple
def calc(*numbers):
        sum =0
        for n in numbers:
                sum = sum + n*n
        return sum

# num = [1,2,3]
# r=calc(*num)
# print(r)


# 关键字参数,允许你传入N个含参数名的参数，这些关键字参数在函数调用时自动组装成一个dict
def person(name, age, **kw):
        print("name:",name,"age:",age,"others:",kw)

# person('ysm', 27,city="beijing")
# extra={'city':'bj','job':'engineer'}
# person('ysm',27,**extra)


def new_person(name, age, *, city, zipcode):
        pass
# new_person('jack',88,city='bj',zipcode=1002)


# 命名关键字参数
# 限定了关键字只有ciy和job
def new_new_person(name, age, *, city, job):
        pass


# 如果参数中已经有一个可变参数，后面跟着的命名关键字就不再需要一个特殊分隔符*了
def new_new_new_person(name, age, *args, city, job):
        pass


# 参数组合
def f1(a, b, c=0, *args, **kw):
        print('a=',a,'b=',b,'c=',c,'args=',args, 'kw=',kw)


def f2(a, b, c=0, *, d, **kw):
        print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

'''
f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)

f2(1,2,d=99,ext=None)

args= (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(args, kw)
'''
#作业
def product(x, *args):
        res = 1
        for y in args:
                res = res *y
        return res * x

#递归函数
def fact(n):
        if n ==1:
                return n
        return n* fact(n-1)
#print(fact(5))
#尾递归-改进的递归
def new_fact(n):
        return fact_iter(n,1)
def fact_iter(n, res):
        if n == 1:
                return res
        return fact_iter(n-1, n*res)
#print(new_fact(100))

#汉诺塔

#times =0
def hanoi_move(n, a, b, c):
        global times
        if n == 1:
                #print(a,'-->',c)
                times= times+1
                return 
        
        hanoi_move(n-1,a,c,b)
        #print(a,'-->',c)
        times= times+1
        hanoi_move(n-1,b,a,c)
#hanoi_move(3,'A','B','C')
#print(times)

#去除str 前后的空格
def mytrim(s):
        while(s[:1]==' '):
               s=s[1:]
        while(s[-1:]==' '):
                s=s[:-1]
        return s
#res = mytrim('  helloworld   ')
#print(res)


def finMinAndMax(L):
    if L==None or L==[]:
         return (None,None)
    min = L[:1]
    max = L[:1]
    for x in L:
         if x<min:
             min = x
         if x> max:
             max= x
    return (min,max) 
#print(finMinAndMax([7]))


def fib(max):
        n,a,b = 0,0,1
        while n<max:
                yield b
                a,b = b,a+b
                n=n+1
        return 'done'

#f = fib(6)

#for n in fib(6):
#       print(n)
f=abs
def my_add(x,y,f):
        return f(x)+f(y)
#res = my_add(-10,-10,f)
#print(res)

def ff(x):
        return x*x
#r=map(ff,[1,2,3,4,5,6,7,8,9])
#list(r)

#test map and reduce
from functools import reduce
def str2float(s):
    m = len(s) - s.index('.') - 1
    def char2num(s):
        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, '.':None}
        return digits[s]

    def fn(x,y):
        if y == None:
            return x
        else:
            return x*10 + y

    return reduce(fn, map(char2num, s))/(10**m)

def is_odd(n):
    return n%2 == 1
#r = tuple( filter(is_odd, my_list))
def not_empty(s):
    return s and s.strip()
r = list(filter(not_empty, ['A'," B", 'C ',' ','']))
print(r)

#素数生成
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break;
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n), it)

#if __name__ == '__main__':
#main()
def triangles():
    L = [1]
    while True:
        yield(L)
        L = [1 if (i == 0 or i == len(L)) else L[i-1] + L[i] for i in range(len(L) + 1)]


def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum


def count():
    fs=[]
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
'''
f1, f2, f3 = count()
f1()
f2()
f3()
'''


def count_pro():
    def f_(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f_(i))
    return fs


# f1, f2, f3 = count_pro()

# '''
def count_pp():
    def f(j):
        return j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count_pp()
# '''
print(f1)
print(f2)
print(f3)























