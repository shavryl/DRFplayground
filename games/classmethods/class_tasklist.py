

class Adder(object):

    def add(self, x, y):
        return 'not implemented'


class ListAdder(Adder):

    def add(self, x, y):
        return x + y


class DictAdder(Adder):

    def add(self, x, y):
        data = dict()

        data['x'] = x
        data['y'] = y

        return data
