import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time()-t)
        return res
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print('{0} has been used: {1}x'.format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
print(reverse_string(text))
print(reverse_string(text * 1000))