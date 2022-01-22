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
