from functools import wraps

def log2(data):
    def deco(func):
        @wraps(func)  # <-- switch commend
        def wrapper(*args, **kwargs):
            print('[Decorator]: get log2 passed data {}'.format(data))
            return func(*args, **kwargs)
        return wrapper
    return deco

@log2("Decor + data")
def foo(info):
    """ Desc: foo func """
    print('foo says {}'.format(info))

# 注意: 以下foo回傳的是wrapper物件, 而非原本的foo, 
#       解決方法, 可以用functools.wraps來解決
#       嘗試著commend掉第5行
print(foo.__name__) 
help(foo)




