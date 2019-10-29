from datetime  import datetime
from functools import wraps

def showDateTime(data=None):
    # check deco info
    if not data is None:
        print('[Deco]: info is {}'.format(data))

    def deco(func): 
        @wraps(func)
        def wrapper(*args, **kwaargs):
            print("[Deco]: now time is {}".format(datetime.now()))
            return func(*args, **kwaargs)
        return wrapper
    return deco

@showDateTime()
def func1():
    print('this is func1')

@showDateTime(data=1234)
def func2(info):
    print('this is func2 with info={}'.format(info))

func1()
func2('okla')