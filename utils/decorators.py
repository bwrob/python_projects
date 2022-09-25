import time


def timed(func):
    def handler(*args):
        start_time = time.time()
        output = func(*args)
        end_time = time.time()
        name = getattr(func, '__name__', repr(callable))
        duration = end_time-start_time
        print(f"\nRuntime of {name} was {duration} seconds.")
        return output
    return handler
