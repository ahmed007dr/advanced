

def decorator(func):
    def wrapper_function(*arg,**kwargs):
        result = func(*arg,**kwargs)
        return result.upper()
    
    return wrapper_function


@decorator
def sum(x,y):
    return 'welcome'
