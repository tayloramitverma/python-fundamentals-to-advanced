import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} excutation time is {end - start}")
        return result
    return wrapper
    
@timer
def exmpale_func(n):
    time.sleep(n)


exmpale_func(2)