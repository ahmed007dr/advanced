def decorator(func):
    def wrapper_function():
        print(' >>>>>> start <<<<') # befor function
        func()
        print('>>>>>>> end >>>>>>') # after function
    return wrapper_function


@decorator
def sum():
    print('welcome')

sum()