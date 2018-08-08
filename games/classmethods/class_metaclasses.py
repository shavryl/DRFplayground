from types import FunctionType
from games.classmethods.class_decorators import tracer


class MetaOne(type):

    def __new__(meta, classname, supers, classdict):
        # run by inherited type __call__
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)


class MetaTwo(type):

    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


# normal class instance serving as metaclass
class MetaObj:

    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call:', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new:', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


# instances inherit from classes and their supers normally
class SuperMetaObj:

    def __call__(self, classname, supers, classdict):
        print('In supermetaobj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


class SubMetaObj(SuperMetaObj):

    def __New__(self, classname, supers, classdict):
        print('In submeta.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In submeta.init: ', classname, supers, classdict, sep='\n...')
        print('... init class object: ', list(Class.__dict__.keys()))


class MetaOne(type):

    def __new__(meta, classname, supers, classdict):
        print('In meta.new: ', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'


class Super(metaclass=MetaOne):

    def spam(self):
        return 'spam'


class Sub(Super):

    def eggs(self):
        return 'eggs'


class Eggs:
    ...


class Spam(Eggs, metaclass=SubMetaObj()):
    data = 1

    def meth(self, arg):
        return self.data + arg


def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return obj.value + 'ham'


class Extender(type):

    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


class MetaExtend(type):

    def __new__(meta, classname, supers, classdict):
        if True:
            classdict['eggs'] = eggsfunc
        else:
            classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


# manage instances like decorator but with a metaclass
def Tracer(classname, supers, classdict):
    aClass = type(classname, supers, classdict)

    class Wrapper:

        def __init__(self, *args, **kargs):
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace:', attrname)
            return getattr(self.wrapped, attrname)
    return Wrapper


class MetaTracer(type):

    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = tracer(attrval)
        return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=MetaTracer):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]


class Client1(metaclass=Extender):

    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'
