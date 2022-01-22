# Python 类型管理
Python是一门动态语言，在运行时检查类型，在定义变量时不需要声明类型。这样做的代价是，不利于在运行前找出可能存在的bug，也可能出现可读性较差的问题。

## 函数注释
为解决这一点问题，Python引入了函数注释(Function Annotations)。然而，python的解释器并不会为变量进行真实的“类型检查”，这种注解的作用只是为了方便阅读。这一点和TypeScript有很大的不同。

而对于列表，元组等数据结构，我们可以利用`typing`模块实现注解。
```python
from typing import List


def int_add(a: int, b: int) -> int:
    return a + b

print(int_add(1, 2))
print(int_add("aaa", "bbb"))  # 不符合注解，但不会报错！


def list_add(a: List, b: List) -> List:
    return a + b

print(list_add([1, 2], [3, 4]))

```

## 静态类型检查
虽然Python本身没有像TypeScript那样提供静态类型检查的机制，但函数注释却可用于类型检查器、IDE、静态检查器等第三方工具。常见的工具有`mypy`,`Typeguard`等。此处由于篇幅所限不再展开，感兴趣的朋友可以访问以下网址：

mypy: [http://mypy-lang.org/index.html](http://mypy-lang.org/index.html)

Typeguard: [https://typeguard.readthedocs.io/en/latest/index.html](https://typeguard.readthedocs.io/en/latest/index.html)