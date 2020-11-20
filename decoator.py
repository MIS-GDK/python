import time
from functools import wraps


def timethis(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def cutdown(n):
    while n > 0:
        n -= 1

    return n


# cutdown(1000)
cutdown = timethis(cutdown)
cutdown(100)

