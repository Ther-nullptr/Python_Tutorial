def outer(x):
    def inner(y):
        return x + y
    return inner

print(outer(1)(2))