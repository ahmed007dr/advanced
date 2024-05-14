

def decorator(func):
    def wrapper_function():
        result = func()
        return result.upper()
    
    return wrapper_function


@decorator
def sum():
    return 'welcome'
