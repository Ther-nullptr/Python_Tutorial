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
{'name': 'linear algebra', 'credits': 4, 'time': ('Tue', '13:30-15:05')
```
