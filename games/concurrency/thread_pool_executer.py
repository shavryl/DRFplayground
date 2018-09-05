import time, random
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print('Executing task {}'.format(n))


def task_done(fn):
    if fn.cancelled():
        print('{} Future has been cancelled'.format(fn))
    elif fn.done():
        print('Task has completed')


def next_done(fn):
    if fn.done():
        print('Next task completed')


def main():
    print('Starting PoolExecutor')
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, 2)
        future.add_done_callback(task_done)
        # chaining callbacks in a single future obj
        future.add_done_callback(next_done)


main()
