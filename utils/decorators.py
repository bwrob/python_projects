from time import time
from functools import wraps


def time(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def handler(*args, **kwargs):
        start_time = time.perf_counter()
        output = func(*args, **kwargs)
        end_time = time.perf_counter()
        name = getattr(func, '__name__', repr(callable))
        duration = end_time-start_time
        print(f"\nRuntime of {name} was {duration} seconds.")
        return output
    return handler
