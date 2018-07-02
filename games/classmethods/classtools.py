

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gether_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gether_attrs())


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()      # Make two instances
    print(X)                         # Show all instance attrs
    print(Y)                         # Show lowest class name


class ListInstance:

    def __str__(self):

        return '<Instanse of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):

        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class ListTree:

    def __str__(self):

        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__, id(self), self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):

        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}Class {1}:, address {2}: (see above)>\n'.format(
                dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent +4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots, aClass.__name__, id(aClass), self.__attrnames(aClass, indent),
                ''.join(genabove), dots)

    def __attrnames(self, obj, indent):

        spaces = ' ' * (indent +4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


def factory(aClass, *args, **kwargs):

    return aClass(*args, **kwargs)
