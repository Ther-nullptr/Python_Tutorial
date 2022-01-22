import time

# 该装饰器可以对修饰的函数进行计时
def clock(func):
    def clocked(*args): # 
        t0 = time.perf_counter()
        result = func(*args) # 
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

factorial(5)

# 这一写法实际上等效于以下写法，可以看到装饰器就是一种更加简洁的闭包写法：
# clock(factorial)(5)

