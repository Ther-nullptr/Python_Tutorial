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

# 以字典的方式呈现namedtuple
print(Linear_Algebra._asdict())