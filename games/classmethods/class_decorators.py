
# mothod decorator
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
