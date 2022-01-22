# Python数据结构进阶
每一篇Python基础教程中，几乎都会提到`list`,`set`,`dict`等内置数据结构。除此之外，Python还有一些进阶数据结构，它们大部分储存在`collections`库中，除此之外
还有`array.array`等数据结构。你可以将它们与C++的STL相比较。

这些高级数据结构在第三方库中也有着广泛应用。例如，在pytorch中，我们可以用`collections.OrderedDict`来建立一个神经网络，并为每一层网络命名：
```python
model = nn.Sequential(OrderedDict([
          ('conv1', nn.Conv2d(1,20,5)),
          ('relu1', nn.ReLU()),
          ('conv2', nn.Conv2d(20,64,5)),
          ('relu2', nn.ReLU())
        ]))
```
接下来，本文将重点介绍几种较为常见的高级数据结构，想要了解更多，可以访问[https://docs.python.org/3.8/library/collections](https://docs.python.org/3.8/library/collections)

## `collections.namedtuple`
我们知道，元组(tuple)可以将不同类型的变量组合在一起，就像`(1,'A',[0.1,0.2])`这样。从某种意义上，元组和C++中的结构体(struct)在应用上有一定的相似之处。但元组本身不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义。`collections.namedtuple`解决了这一问题。

该数据结构的定义方式如下：
```python
collections.namedtuple(typename, field_names)
# typename: 元组名称
# field_name: 元组中元素的名称，可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
```
更多用法见以下代码：
```python
#! /usr/bin/python3
from collections import namedtuple

# 新建namedtuple
Course = namedtuple('Course', ['name', 'credits', 'time'])

# 获取namedtuple的属性
print(Course._fields)

# 实例化Course
Linear_Algebra = Course('linear algebra',4,('Tue','13:30-15:05'))
print(Linear_Algebra)

# 获取属性
print(Linear_Algebra.time)

# 以字典的方式呈现namedtuple（严格地来说是OrderedDict，下文会讲）
print(Linear_Algebra._asdict())
```
运行结果如下：
```
('name', 'credits', 'time')
Course(name='linear algebra', credits=4, time=('Tue', '13:30-15:05'))
('Tue', '13:30-15:05')
{'name': 'linear algebra', 'credits': 4, 'time': ('Tue', '13:30-15:05') }
```

## `collections.OrderedDict`
众所周知，Python中的`dict`是基于hash table实现的（详细的机制可以浏览*Fluent Python*一书），这使得`dict`在实现高性能查找的同时，舍弃了有序性（Python3.6之前）。而`collections.OrderedDict`在添加键的时候会保持顺序，保证了键的迭代次序的一致性。

其用法见以下代码：
```python
#! /usr/bin/python3
from collections import OrderedDict

print("Before deleting:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5
od['f'] = 6

for key, value in od.items():
	print(key, value)

print("After deleting:")
od.pop('c') # 删除操作
for key, value in od.items():
	print(key, value)

print("After re-inserting:")
od['c'] = 3 # 赋值操作
for key, value in od.items():
	print(key, value)
```
运行结果如下：
```
Before deleting:
a 1
b 2
c 3
d 4
e 5
f 6
After deleting:
a 1
b 2
d 4
e 5
f 6
After re-inserting:
a 1
b 2
d 4
e 5
f 6
c 3
```

可以看到，`OrderedDict`会根据放入元素的先后顺序进行排序。除此之外，`OrderedDict`和`dict`并无太大区别。

> 注：在Python3.6及之后的版本，所有的普通`dict`都变为有序的了，故两者将无区别。

## `collections.defaultdict`
在使用字典时，如果访问字典中不存在的键值对，程序会报错，就像这样：
```python
GPAdict = {'A+':4.0,'A':4.0}
print(GPAdict['A-'])
```

```
Traceback (most recent call last):
  File "/home/nullptr/open-source/advanced_python/1_advanced_data_structure/defaultdict_demo.py", line 2, in <module>
    print(GPAdict['A-'])
KeyError: 'A-'
```
而`collections.defaultdict`可以解决这一问题。它在创建时可以传入一个可调用对象（可以是一般函数，也可以是lambda函数等），作为字典中没有键时的默认选择。
```python
from collections import defaultdict

GPAdict = defaultdict(lambda:4.0)
GPAdict['A+'] = 4.0
GPAdict['A'] = 4.0
print(GPAdict['B+'])

# 以下写法也可以
'''
def foo():
    return 4.0
GPAdict = defaultdict(foo)
GPAdict['A+'] = 4.0
GPAdict['A'] = 4.0
print(GPAdict['B+'])
'''
```
运行结果如下：
```
4.0
```