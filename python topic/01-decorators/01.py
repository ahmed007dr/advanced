#Decorators 
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it

def mydecorator():
    if x < 0 or y < 0 :
        return ' x > 0'
    
@mydecorator
def sum(x,y):
    return x + y

def mydecorator(func):
    def wrapper(x, y):
        if x < 0 or y < 0:
            return 'x > 0'
        return func(x, y)
    return wrapper

@mydecorator
def sum(x, y):
    return x + y

print(sum(1, 2))  # prints 3
print(sum(-1, 2))  # prints 'x > 0'