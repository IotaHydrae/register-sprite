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

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            this_time = self.get_current_time()
            hour = this_time[0]
            min = this_time[1]
            sec = this_time[2]
            if sec < 10:
                sec = '0' + str(sec)
            else:
                sec = sec

            program_status = 'OK'
            log_string = func.__code__
            print(f'[    {hour}:{min}:{sec}  ]', log_string, " was called",end=' ')
            print(f' [\033[32m {program_status} \033[0m] ')
            return func(*args, **kwargs)

        return wrapped_function

    def get_current_time(self):
        this_time = time.localtime(time.time())
        hour = this_time.tm_hour
        min = this_time.tm_min
        sec = this_time.tm_sec
        return [hour, min, sec]
