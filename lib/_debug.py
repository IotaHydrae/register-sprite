# import **************************************************
import time
from functools import wraps


'''
    @file: _debug.py
    @author: hz
    @version: v1.1
    @date: 2020-10-22
    @brief: 调试相关
'''
class printk(object):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, func):
        this_time = time.localtime(time.time())
        hour = this_time.tm_hour
        min = this_time.tm_min
        src = this_time.tm_sec
        if src < 10:
            src = '0' + str(src)
        else:
            src = src

        program_status = 'OK'

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__code__
            print(f'[    {hour}:{min}:{src}  ]', log_string, " was called",end=' ')
            print(f' [\033[32m {program_status} \033[0m] ')
            return func(*args, **kwargs)

        return wrapped_function
