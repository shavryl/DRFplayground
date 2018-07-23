

class Person:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('fetch ...')
        return self._name

    def set_name(self, value):
        print('change ')
        self._name = value

    def del_name(self):
        print('remove ')
        del self._name

    name = property(get_name, set_name, del_name, "name property docs")



