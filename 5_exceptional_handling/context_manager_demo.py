from contextlib import contextmanager

@contextmanager
def myopen(file_name):
    f = open(file_name,'w+')
    yield f
    f.close()

with myopen('foo.txt') as f:
    f.write('a test for contextmanager')