import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Run time of '{func.__name__}' was {end-start} seconds.")
        return result
    return wrapper


@timer
def do_something(number):
    """Toy function to keep Python busy"""
    return "-".join(str(n) for n in range(number))


do_something(100000)
