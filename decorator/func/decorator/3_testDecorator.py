"""


"""

from functools import wraps

def log(decVal):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('[Deco]: before func')
            result = func(*args, **kwargs)+999 # <--先呼叫
            print('[Deco]: after func, we add 999 in func result = {}'.format(result))
        return wrapper
    return deco


@log('okla')
def func(data):
    result = data+1000
    print('[func]: result is {}'.format(result))
    return result


func(6000)