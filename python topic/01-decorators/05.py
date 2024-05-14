class DecoratorClass:
    def __init__(self,func):
        self.func = func
    
    def __call__(self,*args, **kwargs): 
        print("before calling")
        print(self.func())
        print('after calling')

@DecoratorClass
def sum():
    return ' welcome '
sum()
