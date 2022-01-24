try:
    f = open('foo.txt')
    print("No error occurs!")
except FileExistsError: # 按照不同的异常类型捕获异常
	print('There is a FileExistsError!')
except FileNotFoundError:
	print('There is a FileNotFoundError!')
else:
    print(f.readlines()) # 当未触发异常时，将会执行else中的语句
finally:
    print("Operations are Finished!") # finally定义无论在任何情况下都会执行的清理行为