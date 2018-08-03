import time


instances = {}


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


def Tracer(cls):

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, attrname):

            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)

    return Wrapper


class InstTracer:

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args):
        self.wrapped = self.cls(*args)
        return self

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


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


def new_timer(label=''):

    def decorator(func):
        # multilevel state retention
        def on_call(*args):
            ...
            func(*args)
        return on_call
    return decorator


def singleton(cls):
    instance = None

    def on_call(*args, **kwargs):
        nonlocal instance

        if instance is None:
            instance = cls(*args, **kwargs)

        return instance

    return on_call


class singleton:

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)

        return self.instance


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


@InstTracer
class Spam:

    def display(self):
        print('Spam!' * 8)


@InstTracer
class Person:

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


trace_me = False


def trace(*args):
    if trace_me: print('[' + ' '.join(map(str, args)) + ']')


def private(*privates):

    def on_decorator(cls):

        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return OnInstance
    return on_decorator


@private('data', 'size')
class Doubler:

    def __init__(self, label, start):
        self.label = label
        self.data = start

    def size(self):
        return len(self.data)

    def double(self):
        for i in range(self.size()):
            self.data[i] = self.data[i] * 2

    def display(self):
        print('%s => %s' % (self.label, self.data))


registry = {}


def register(obj):

    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return x ** 2


@register
def ham(x):
    return x ** 3


@register
class Eggs:

    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)
