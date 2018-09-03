import threading, time, random


def my_thread(my_event):
    while not my_event.is_set():
        print('Waiting for event to be set')
        time.sleep(1)
    print('My event has been set')


def main():
    my_event = threading.Event()
    thread1 = threading.Thread(target=my_thread, args=(my_event, ))
    thread1.start()
    time.sleep(10)
    my_event.set()


main()
