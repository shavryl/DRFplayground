import time, random
from concurrent.futures import ThreadPoolExecutor


def some_task(n):
    print('Executing task {}'.format(n))
    time.sleep(n)
    print('Task {} Finished Executing'.format(n))


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(some_task, (1))
        task2 = executor.submit(some_task, (2))
        executor.shutdown(wait=True)
        # this will not proceed cause of shutdown
        # triggers RuntimeError
        task3 = executor.submit(some_task, (3))


main()
