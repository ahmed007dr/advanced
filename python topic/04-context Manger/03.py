class FileManger:
    def __init__(self, filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    #can use it to database 

    def __exit__(self,exc_type,exc_value,exc_tb):
        self.file.close()



with FileManger('data.txt','w') as file:
    file.write('hello ahmed')
    #TypeError: FileManger.__exit__() takes 1 positional argument but 4 were given



