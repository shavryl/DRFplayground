import random
from games.concurrency.decorators import timeit


def calculate_prime(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


@timeit
def main():
    print('Started number crunching')

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime(rand))


main()
