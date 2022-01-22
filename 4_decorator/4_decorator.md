# Python 装饰器
函数装饰器(decorator)用于在源码中“标记”函数，在不修改原函数的前提下，以某种方式增强函数的行为。

Python的装饰器基于闭包实现。**闭包**是指函数中再嵌套一个函数，并且引用外部函数的变量。
```python
# 在该示例中，outer函数内又定义了一个inner函数，并且inner函数又引用了外部函数outer的变量x，形成一个闭包
def outer(x):
    def inner(y):
        return x + y
    return inner

# outer(1)(2)中，第一个括号传进去的值返回inner函数，其实就是返回1 + y，所以再传第二个参数进去，就可以得到返回值，1 + 2
print(outer(1)(2))
```
```
3
```
装饰器本质上就是一种闭包。我们可以用如下的方式实现一个装饰器：
```python
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
```
```
[0.00000050s] factorial(1) -> 1
[0.00004400s] factorial(2) -> 2
[0.00008740s] factorial(3) -> 6
[0.00012330s] factorial(4) -> 24
[0.00013580s] factorial(5) -> 120
```

## 内置装饰器
实际上，我们自定义Python装饰器的情况还是比较少的。我们大多数时候使用Python所内置的一些装饰器来管理函数。如`@contextmanager`, `@staticmethod`, `@classmethod`, `@abstractmethod`, `@property`等。这些装饰器的用法将在后续教程中陆续介绍。