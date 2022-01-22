numbers = [2022,1,22,20,38]
numbers_1 = [bin(s) for s in numbers] # 将所有数字转换为二进制，并存入列表
numbers_2 = [hex(s) for s in numbers if s%2 == 0] # 将所有偶数数字转换为十六进制，并存入列表
print(numbers_1)
print(numbers_2)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
result = [(color, size) for color in colors for size in sizes]
print(result)