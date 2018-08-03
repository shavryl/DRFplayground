from games.classmethods.class_decorators import singleton


class Name:
    """
    example of descriptor
    """
    def __get__(self, instance, owner):
        print('fetch name: ')
        return instance._name

    def __set__(*args):
        raise AttributeError('Is not permitted to set')

    def __delete__(self, instance):
        print('remove ')
        del instance._name


@singleton
class Profile:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # setter can dynamically check conditions
        self._name = value + ' krosaucheg'

    @name.deleter
    def name(self):
        # before deletion of profile model
        # we could check child\parent relations
        # and make cases for both variants
        del self._name


class DescState:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescrState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescrState set')
        self.value = value


# client Class
class CalcAttrs:

    X = DescState(2)
    Y = 3

    def __init__(self):
        self.Z = 4


class InstState:

    def __get__(self, instance, owner):
        print('Instance get')
        return instance._X * 10

    def __set__(self, instance, value):
        print('Instance set')
        instance._X = value


class NextCalc:

    X = InstState()
    Y = 3

    def __init__(self):
        self._X = 2
        self.Z = 4


class DescBoth:

    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)

    def __set__(self, instance, value):
        instance.data = value


class Client:

    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')


class Property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("Can't get attribute")
        return self.fget

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(instance)


class Wrapper:

    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace ' + attrname)
        return getattr(self.wrapped, attrname)

    def __getattribute__(self, name):
        # prevents recursive loop
        x = object.__getattribute__(self, 'other')

    def __setattr__(self, name, value):
        # prevents recursive loop
        self.__dict__['other'] = value
        # or possible solution is
        # object.__setattr__(self, 'other', value)


class AttrSqare:

    def __init__(self, start):
        self.value = start

    def __getattribute__(self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)


class GetAttr:

    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('len : 42')
        return 42

    def __getattr__(self, attr):
        print('getattr ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:

    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('len : 42')
        return 42

    def __getattribute__(self, attr):
        print('getattribute ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattribute str]'
        else:
            return lambda *args: None


class Powers:

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square ** 2

    def set_square(self, value):
        self._square = value

    square = property(get_square, set_square)

    def get_cube(self):
        return self._cube ** 3

    cube = property(get_cube)


class DescSquare:

    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:

    def __get__(self, instance, owner):
        return instance._cube ** 3


class DescPowers:

    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
