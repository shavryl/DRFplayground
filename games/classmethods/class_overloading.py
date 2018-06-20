

class SkipObject:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


class Squares:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


class Iters:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter => next: ', end='')
        for x in self.data:
            yield x
            print('next:', end='')


    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    alpha = 'abcde'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')

    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end=' | ')

    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
