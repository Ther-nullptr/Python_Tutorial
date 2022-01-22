from collections import defaultdict

GPAdict = defaultdict(lambda:4.0)
GPAdict['A+'] = 4.0
GPAdict['A'] = 4.0
print(GPAdict['B+'])

# 以下写法也可以
'''
def foo():
    return 4.0
GPAdict = defaultdict(foo)
GPAdict['A+'] = 4.0
GPAdict['A'] = 4.0
print(GPAdict['B+'])
'''
