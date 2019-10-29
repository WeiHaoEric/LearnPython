from termcolor import colored

print("=== Basic Deco ===")
def log(func):
    def wrapper(*args, **kwargs):
        print('[Decorator]logging for {}'.format(func.__name__))
        return func(*args, **kwargs)   # <-- 回傳func(*args, **kwargs)
        # func(*args, **kwargs)          # <-- 也可直接呼叫func(*args, **kwargs), 不需要return
    return wrapper

@log
def hello():
    print('hello~!')

hello()

print("=== Basic Deco 2===")

def log2(data):
    def deco(func):
        def wrapper(*args, **kwargs):
            print('[Decorator]: get log2 passed data {}'.format(data))
            return func(*args, **kwargs)
        return wrapper
    return deco

@log2("Decor + data")
def foo(info):
    print('foo says {}'.format(info))

foo('bar')
