

class CardHolder:

    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def get_name(self):
        return self.__name

    def set_name(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(get_name, set_name)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid age')
        else:
            self.__age = value

    age = property(get_age, set_age)

    def get_acct(self):
        return self.__acct[:-3] + '***'

    def set_acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('Invalid acct number')
        else:
            self.__acct = value

    acct = property(get_acct, set_acct)

    def remain_get(self):
        return self.retireage - self.age

    remain = property(remain_get)


class CardHolderDesc:

    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:

        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value

    name = Name()

    class Age:

        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('Invalid age')
            else:
                self.age = value

    age = Age()

    class Acct:

        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('Invalid acct number')
            else:
                self.acct = value

    acct = Acct()

    class Remain:

        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('Cannot set remain')

    remain = Remain()
