def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with args {args_values if len(args_values) > 0 else 'null'} and kwargs {kwargs_values if len(args_values) > 0 else 'null'}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("Hello Amit")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("Amit", greeting="Hi")