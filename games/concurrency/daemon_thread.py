import threading, time


def standart_thread():
    print("Starting my thread")
    time.sleep(20)
    print(threading.main_thread())
    print("End standart thread")



def daemon_thread():
    while True:
        print('Sended hartbeat from first daemon')
        print("Total Number of Active Threads: {}".format(threading.active_count()))
        time.sleep(2)


def daemon_thread2():
    while True:
        print('Sended hartbeat from second daemon')
        time.sleep(1)


def main():
    standart = threading.Thread(target=standart_thread)
    daemon = threading.Thread(target=daemon_thread)
    daemon2 = threading.Thread(target=daemon_thread2)

    daemon.setDaemon(True)
    daemon2.setDaemon(True)

    daemon.start()
    daemon2.start()

    standart.start()

main()
