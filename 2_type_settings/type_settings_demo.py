from typing import List


def int_add(a: int, b: int) -> int:
    return a + b

print(int_add(1, 2))
print(int_add("aaa", "bbb"))  # 不符合注解，但不会报错！


def list_add(a: List, b: List) -> List:
    return a + b

print(list_add([1, 2], [3, 4]))
