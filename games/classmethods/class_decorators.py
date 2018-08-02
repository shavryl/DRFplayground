import time


# method decorator
def decorator(F):

    def wrapper(*args):
        # use F and args
        # F(*args) calls original func
        return wrapper


@decorator
def func():
    ...


def class_decorator(cls):

    class Wrapper:

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Wrapper


@class_decorator
class C:

    def __init__(self, x, y):
        self.attr = 'spam'


class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))

        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):

        def wrapper(*args, **kwargs):

            return self(instance, *args, **kwargs)

        return wrapper


def both_tracer(func):
    """
    applies to both functions
    and class methods
    """
    calls = 0

    def on_call(*args, **kwargs):

        nonlocal calls
        calls +=1
        print('call %s to %s' % (calls, func.__name__))

        return func(*args, **kwargs)

    return on_call


class timer:

    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__,
                                  elapsed, self.alltime))
        return result


@timer
def spam(a, b, c):
    print(a + b + c)


@timer
def eggs(x, y):
    print(x ** y)


spam(5, 7, 12)

eggs(2, 6)
