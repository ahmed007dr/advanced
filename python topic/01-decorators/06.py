import time
def calculate_exe_time(func):
    def warpper_function(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'excute time :{end_time-start_time}')
    return warpper_function


# @calculate_exe_time
# def myfunc():
#     print('start')
#     time.sleep(4)
#     print('end time ')
# myfunc()

@calculate_exe_time
def myfunc():
    for _ in range(1444440):
        pass

myfunc()