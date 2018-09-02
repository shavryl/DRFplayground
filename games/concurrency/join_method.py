import threading, time


def our_thread(i):
    print('Thread {} started'.format(i))
    time.sleep(i*2)
    print('Thread {} finished'.format(i))


def main():
    thread1 = threading.Thread(target=our_thread, args=(1, ))
    thread1.start()
    print('Is thread 1 Finished?')
    thread2 = threading.Thread(target=our_thread, args=(2, ))
    thread2.start()
    thread2.join()
    print('Thread 2 definitely finished!')


main()
