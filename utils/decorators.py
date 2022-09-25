from time import perf_counter
from functools import wraps


def time(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def handler(*args, **kwargs):
        start_time = perf_counter()
        output = func(*args, **kwargs)
        end_time = perf_counter()
        duration = end_time-start_time
        print(f"\nRuntime of {func.__name__!r} was {duration} seconds.")
        return output
    return handler


def debug(func):
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug
