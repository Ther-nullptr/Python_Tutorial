# Python 异常处理
## 传统异常处理
在Python中，传统的异常处理格式如下：
```python
try:
    f = open('foo.txt')
    print("No error occurs!")
except FileExistsError: # 按照不同的异常类型捕获异常
	print('There is a FileExistsError!')
except FileNotFoundError:
	print('There is a FileNotFoundError!')
else:
    print(f.readlines()) # 当未触发异常时，将会执行else中的语句
finally:
    print("Operations are Finished!") # finally定义无论在任何情况下都会执行的清理行为
```
结果1：
```
There is a FileNotFoundError!
Operations are Finished!
```
结果2：
```
No error occurs!
['Hello World!']
Operations are Finished!
```

## `With`

`with`语句可以极大地简化这种`try-except-else-finally`模式。例如，如果我们想要实现文件的安全读写，传统的写法是这样的：
```python
file = open('foo.txt', 'w+')
try:
    file.write('hello world !')
finally:
    file.close()
```
而使用`with`语句后是这样的：
```python
with open('foo.txt', 'w+') as file:
    file.write('hello world !')
```

要想使用`with`语句，我们需要实现一个上下文管理器类(contextmanager)。上下文管理器中含有`__enter__`和`__exit__`两个方法。with语句开始运行时，会在上下文管理器对象上调用`__enter__`方法。with语句运行结束后，会在上下文管理器对象上调
用`__exit__`方法。例如，我们可以写一个简单的文件管理类：
```python
class MessageWriter:
    def __init__(self, file_name):
        self.file_name = file_name
      
    # 解释器在调用__enter__时，除了隐式的self之外，不会传入任何参数
    def __enter__(self):
        self.file = open(self.file_name, 'w+')
        return self.file
    
    # 传给__exit__方法的三个参数列举如下：exc_type(异常类)；exc_value(异常实例)；traceback(traceback对象)
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
  
with MessageWriter('foo.txt') as f:
    f.write('a test for MessageWriter')
```

## `@contextmanager`
相比于实现一个上下文管理器类，装饰器`@contextmanager`能减少创建上下文管理器的样板代码量，因为不用编写一个完整的类，定义`__enter__`和`__exit__`方法，而只需实现有一个`yield`语句的生成器。

在此用法中，`yield`语句前面的所有代码在`with`块开始时（即解释器调用`__enter__`方法时）执行，`yield`语句后面的代码在`with`块结束时（即调用`__exit__`方法时）执行。

使用`@contextmanager`重写上面的代码：
```python
from contextlib import contextmanager

@contextmanager
def myopen(file_name):
    f = open(file_name,'w+')
    yield f
    f.close()

with myopen('foo.txt') as f:
    f.write('a test for contextmanager')
```
