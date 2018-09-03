import threading, time, random


tickets_available = 100


class TicketSeller(threading.Thread):

    tickets_sold = 0

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print('Ticket Seller Started work')

    def run(self):
        global tickets_available
        running = True
        while running:
            self.random_delay()

            self.sem.acquire()
            if tickets_available <= 0:
                running = False
            else:
                self.tickets_sold = self.tickets_sold + 1
                tickets_available = tickets_available - 1
                print('{} Sold one ({} left)'
                      .format(self.getName(), tickets_available))
            self.sem.release()
        print('Ticket Seller {} Sold {} tickets in total'
              .format(self.getName(), self.tickets_sold))

    def random_delay(self):
        time.sleep(random.randint(0, 1))


def process():
    semaphore = threading.Semaphore()
    sellers = []

    for i in range(4):
        seller = TicketSeller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


process()
