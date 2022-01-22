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

# 用于对比：经典写法，直接打印，可控性较差
def fibo(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # print b
        a, b = b, a + b
        n = n + 1

fibo(5)