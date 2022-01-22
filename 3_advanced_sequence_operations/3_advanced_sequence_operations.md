# Python高级序列操作
Python中有许多Pythonic的序列操作，也许它们可以用更加基础的方式实现，但这样写往往更加简洁。

## 列表推导
列表推导(listcomps)是一种构建列表的快捷方式。
```python
numbers = [2022,1,22,20,38]
numbers_1 = [bin(s) for s in numbers] # 将所有数字转换为二进制，并存入列表
numbers_2 = [hex(s) for s in numbers if s%2 == 0] # 将所有偶数数字转换为十六进制，并存入列表
print(numbers_1)
print(numbers_2)
```
运行结果如下：
```
['0b11111100110', '0b1', '0b10110', '0b10100', '0b100110']
['0x7e6', '0x16', '0x14', '0x26']
```
列表推导相对于之前的`for`循环写法，显然更加紧凑。由于列表推导支持映射变换和条件判断，我们也可以用`map`(映射)和`filter`(过滤器)来实现相似的功能。此两个函数的具体用法不在此阐述。
```python
numbers_1 = list(map(hex,filter(lambda x:x%2==0,numbers)))
```
有多个列表参与推导时，将会返回它们的[笛卡尔积](https://zh.wikipedia.org/wiki/%E7%AC%9B%E5%8D%A1%E5%84%BF%E7%A7%AF)
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
result = [(color, size) for color in colors for size in sizes]
print(result)
```
```
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
```
## 生成器语法
相比于列表推导直接返回一个列表，生成器语法(genexps)可以逐个生成元素。而在语法上，生成器只不过是将`[]`换为了`()`。
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for result in (f'{c},{s}' for c in colors for s in sizes):
    print(result)
```
```
black,S
black,M
black,L
white,S
white,M
white,L
```

## 解包器
在Python函数的说明文档中，常常可以看到`foo(...,*args,**kwargs)`这样的说明。此处的\*就代表解包器。\*表示为列表和元组解包，\*\*表示为字典解包。它们可以用于获取不确定数量的参数，从而实现一些较为优雅的写法。
```python
# 元组解包
a, b, *rest = range(5)
print(a, b, rest)

a, *body, b = range(5)
print(a, body, b)

# 利用字典解包实现字典拼接
a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}
print({**a, **b})

# 当参数的数量不确定时，*args表示位置参数，**kwargs表示键值对参数
def advanced_print(val, *args, **kwargs):
    print(val)
    for v in args:
        print(f'args:{v}')
    for k, v in kwargs.items():
        print(f'kwargs:{k}->{v}')

advanced_print(0, 1, 2, 3, param1=4, param2=5)
```
```
0 1 [2, 3, 4]
0 [1, 2, 3] 4
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
0
args:1
args:2
args:3
kwargs:param1->4
kwargs:param2->5
```
## yield
`yield`用于构造生成器。从某种意义上来讲，`yield`和`return`有一定的相似之处，但有`return`的函数直接返回所有结果，程序终止不再运行，并销毁局部变量；而有`yield`的函数则返回一个可迭代的 `generator`（生成器）对象，你可以使用`for`循环或者调用`next()`方法遍历生成器对象来提取结果。

在调用生成器函数的过程中，每次遇到`yield`时函数会暂停并保存当前所有的运行信息（保留局部变量），返回`yield`的值, 并在下一次执行`next()`方法时从当前位置继续运行，直到生成器被全部遍历完。

`yield`用法使得程序在迭代时免于生成列表，可以节省内存。

```python
# 一个用于生成Fibonacci数列的迭代器
def fibo_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

f = fibo_generator(5)
for val in f:
    print(val)
```
```
1
1
2
3
5
```
可以将上一写法与以下写法进行对比：
```python
# 用于对比：经典写法，直接打印，可控性较差
def fibo(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # print b
        a, b = b, a + b
        n = n + 1

fibo(5)
```
```
1
1
2
3
5
```

以上说明参考自[https://zhuanlan.zhihu.com/p/268605982](https://zhuanlan.zhihu.com/p/268605982)

## 字典推导和集合推导
字典推导和集合推导与列表推导有着相似的语法，只不过将`[]`换为了`{}`（字典为键值对，集合为值）。
```python
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
]

# 字典推导
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

# 带有映射和判断的字典推导
country_code = {
    code: country.upper()
    for country, code in country_code.items() if code > 50
}
print(country_code)

# 集合推导
s = {country for _, country in DIAL_CODES}
print(s)

```
```
{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55}
{86: 'CHINA', 91: 'INDIA', 62: 'INDONESIA', 55: 'BRAZIL'}
{'India', 'China', 'United States', 'Brazil', 'Indonesia'}
```
