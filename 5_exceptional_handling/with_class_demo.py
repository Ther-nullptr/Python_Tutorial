class MessageWriter:
    def __init__(self, file_name):
        self.file_name = file_name
      
    # 解释器在调用__enter__时，除了隐式的self之外，不会传入任何参数
    def __enter__(self):
        self.file = open(self.file_name, 'w+')
        return self.file
    
    # 传给__exit__方法的三个参数列举如下：exc_type(异常类)；exc_value(异常实例)；traceback(traceback对象)
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
  
with MessageWriter('foo.txt') as f:
    f.write('a test for MessageWriter')