# RegisterSprite  Copyright (C) 2020  jessenhua (h1657802074@gmail.com)

# This file is part of RegisterSprite
#   ____ ____  _      __     _______  ___
#  / ___|  _ \| |     \ \   / /___ / / _ \
# | |  _| |_) | |      \ \ / /  |_ \| | | |
# | |_| |  __/| |___    \ V /  ___) | |_| |
#  \____|_|   |_____|    \_/  |____(_)___/
#
# RegisterSprite is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import **************************************************
import time
from functools import wraps
from lib import _color_operations

'''
    @file: _debug.py
    @author: hz
    @version: v1.1
    @date: 2020-10-22
    @brief: 调试相关
'''
ONE_SPACE = " "
TWO_SPACE = "  "
THREE_SPACE = "   "


def timer_start(self):
    """ 启动计时器 """
    global g_time_start

    g_time_start = time.time()


def timer_stop(self):
    global g_time_delta, g_time_end

    g_time_end = time.time()
    g_time_delta = g_time_end - g_time_start
    print((g_time_delta * 1000))


class printk(object):

    def __init__(self, *args, **kwargs):
        self.fontstyle = _color_operations.FontStyle()
        pass

    def __call__(self, func):

        @wraps(func)
        def wrapped_function(*args, **kwargs):
            t = get_current_time()
            mutil_time = f"{t[0]}:{t[1]}:{t[2]}"
            styled_time = self.fontstyle.color_font(mutil_time, 1,33)
            if t[2] < 10:
                sec = '0' + str(t[2])
            else:
                sec = t[2]

            program_status = self.fontstyle.color_font('OK', 1, 32)
            log_string = func.__code__
            print(f'[{THREE_SPACE}{styled_time}{TWO_SPACE}] {program_status} ', log_string, " was called")
            return func(*args, **kwargs)

        return wrapped_function


def get_current_time():
    this_time = time.localtime(time.time())
    hour = this_time.tm_hour
    min = this_time.tm_min
    sec = this_time.tm_sec
    return [hour, min, sec]


def _timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        hour, min, sec = get_current_time()

        print(f'[{THREE_SPACE}{hour}:{min}:{sec}{TWO_SPACE}]' + ONE_SPACE \
              + 'Function ** {} ** executed in {:.4f} seconds'.format(func.__name__, (end - start)))
        return result

    return wrapper
