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

