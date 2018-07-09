from games.classmethods.class_tools import ListInstance


class C1:

    def meth1(self): self.__X = 88

    def meth2(self): print(self.__X)


class C2:

    def metha(self): self.__X = 99

    def methb(self): print(self.__X)


class C3(C1, C2): pass


class Spam(ListInstance):

    def __init__(self):
        self.data = 'food'

    def doit(self, message):
        print(message)


class Number:

    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def tripple(self):
        return self.base * 3


def square(arg):
    return arg ** 2


class Sum:

    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:

    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


class Negate:

    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)

























