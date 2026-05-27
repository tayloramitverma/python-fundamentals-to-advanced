import time

def cache(func):
    cached_data = {}
    print(cached_data)
    def wrapper(*args):
        if args in cached_data:
            return cached_data[args]
        result = func(*args)
        cached_data[args] = result
        return result
    return wrapper


@cache
def long_time_func(a, b):
    time.sleep(4)
    return a + b


print(long_time_func(2, 2))
print(long_time_func(2, 2))
print(long_time_func(2, 4))